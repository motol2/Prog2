import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# ── Barvy & font ────────────────────────────────────────────────────────────
BG        = "#1a1a2e"
PANEL     = "#16213e"
ACCENT    = "#e94560"
ACCENT2   = "#0f3460"
TEXT      = "#eaeaea"
MUTED     = "#7a7a9d"
DONE_COL  = "#3a3a5c"
FONT_HEAD = ("Georgia", 22, "bold")
FONT_BTN  = ("Courier New", 10, "bold")
FONT_ITEM = ("Courier New", 12)
FONT_SUB  = ("Courier New", 9)

SAVE_FILE = os.path.join(os.path.dirname(__file__), "todo_data.json")


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✦ TO-DO LIST ✦")
        self.root.geometry("560x700")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.tasks = []       # [{"text": str, "done": bool, "priority": int}]
        self.selected = None  # index

        self._build_ui()
        self._load()
        self._refresh()

    # ── UI ──────────────────────────────────────────────────────────────────

    def _build_ui(self):
        # Hlavička
        hdr = tk.Frame(self.root, bg=BG)
        hdr.pack(fill="x", padx=24, pady=(24, 0))

        tk.Label(hdr, text="✦ TO-DO LIST ✦", font=FONT_HEAD,
                 bg=BG, fg=ACCENT).pack(side="left")
        self.count_lbl = tk.Label(hdr, text="", font=FONT_SUB,
                                  bg=BG, fg=MUTED)
        self.count_lbl.pack(side="right", anchor="s", pady=6)

        # Oddělovač
        tk.Frame(self.root, bg=ACCENT, height=2).pack(fill="x", padx=24, pady=(8, 0))

        # Vstupní řádek
        entry_frame = tk.Frame(self.root, bg=PANEL, pady=14, padx=16)
        entry_frame.pack(fill="x", padx=24, pady=12)

        self.entry = tk.Entry(entry_frame, font=FONT_ITEM,
                              bg=ACCENT2, fg=TEXT, insertbackground=ACCENT,
                              relief="flat", bd=0)
        self.entry.pack(side="left", fill="x", expand=True, ipady=7, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self._add())

        self._btn(entry_frame, "＋ PŘIDAT", self._add, ACCENT).pack(side="left")

        # Tlačítkový panel
        btn_frame = tk.Frame(self.root, bg=BG)
        btn_frame.pack(fill="x", padx=24, pady=(0, 8))

        buttons = [
            ("✔ HOTOVO",    self._toggle_done,  "#2a9d8f"),
            ("✏ UPRAVIT",   self._edit,         "#e9c46a"),
            ("⇑ NAHORU",    self._move_up,      ACCENT2),
            ("⇓ DOLŮ",      self._move_down,    ACCENT2),
            ("✕ VYMAZAT",   self._delete,       ACCENT),
            ("⌫ VYČISTIT",  self._clear_done,   "#6d4c7d"),
            ("⚑ PRIORITA",  self._toggle_priority, "#f4a261"),
            ("⟳ RESET",     self._reset_all,    "#555577"),
        ]

        for i, (label, cmd, color) in enumerate(buttons):
            self._btn(btn_frame, label, cmd, color).grid(
                row=i // 4, column=i % 4, padx=3, pady=3, sticky="ew"
            )

        for c in range(4):
            btn_frame.columnconfigure(c, weight=1)

        # Seznam úkolů
        list_frame = tk.Frame(self.root, bg=BG)
        list_frame.pack(fill="both", expand=True, padx=24, pady=(4, 0))

        scrollbar = tk.Scrollbar(list_frame, bg=PANEL, troughcolor=BG,
                                 relief="flat", width=8)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            list_frame,
            font=FONT_ITEM,
            bg=PANEL, fg=TEXT,
            selectbackground=ACCENT, selectforeground="#fff",
            activestyle="none",
            relief="flat", bd=0,
            highlightthickness=0,
            yscrollcommand=scrollbar.set,
            cursor="hand2",
        )
        self.listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)
        self.listbox.bind("<Double-Button-1>", lambda e: self._toggle_done())

        # Stavový řádek
        tk.Frame(self.root, bg=ACCENT, height=1).pack(fill="x", padx=24, pady=(8, 0))
        self.status_lbl = tk.Label(self.root, text="", font=FONT_SUB,
                                   bg=BG, fg=MUTED, anchor="w")
        self.status_lbl.pack(fill="x", padx=26, pady=(4, 16))

    def _btn(self, parent, text, cmd, color):
        return tk.Button(
            parent, text=text, command=cmd,
            font=FONT_BTN,
            bg=color, fg="#fff",
            activebackground="#fff", activeforeground=color,
            relief="flat", bd=0,
            padx=10, pady=6,
            cursor="hand2",
        )

    # ── Akce ────────────────────────────────────────────────────────────────

    def _add(self):
        text = self.entry.get().strip()
        if not text:
            self._status("⚠ Zadejte text úkolu.")
            return
        self.tasks.append({"text": text, "done": False, "priority": False})
        self.entry.delete(0, "end")
        self._refresh()
        self._status(f"✔ Přidáno: {text}")
        self._save()

    def _delete(self):
        idx = self._get_sel()
        if idx is None: return
        removed = self.tasks.pop(idx)
        self._refresh()
        self._status(f"✕ Odstraněno: {removed['text']}")
        self._save()

    def _toggle_done(self):
        idx = self._get_sel()
        if idx is None: return
        self.tasks[idx]["done"] = not self.tasks[idx]["done"]
        self._refresh(idx)
        state = "hotovo" if self.tasks[idx]["done"] else "nedokončeno"
        self._status(f"Označeno jako {state}: {self.tasks[idx]['text']}")
        self._save()

    def _edit(self):
        idx = self._get_sel()
        if idx is None: return
        new_text = simpledialog.askstring(
            "Upravit úkol",
            "Nový text:",
            initialvalue=self.tasks[idx]["text"],
            parent=self.root,
        )
        if new_text and new_text.strip():
            self.tasks[idx]["text"] = new_text.strip()
            self._refresh(idx)
            self._status(f"✏ Upraveno: {new_text.strip()}")
            self._save()

    def _toggle_priority(self):
        idx = self._get_sel()
        if idx is None: return
        self.tasks[idx]["priority"] = not self.tasks[idx]["priority"]
        self._refresh(idx)
        state = "vysoká" if self.tasks[idx]["priority"] else "normální"
        self._status(f"⚑ Priorita změněna na {state}: {self.tasks[idx]['text']}")
        self._save()

    def _move_up(self):
        idx = self._get_sel()
        if idx is None or idx == 0: return
        self.tasks[idx], self.tasks[idx-1] = self.tasks[idx-1], self.tasks[idx]
        self._refresh(idx-1)
        self._save()

    def _move_down(self):
        idx = self._get_sel()
        if idx is None or idx >= len(self.tasks)-1: return
        self.tasks[idx], self.tasks[idx+1] = self.tasks[idx+1], self.tasks[idx]
        self._refresh(idx+1)
        self._save()

    def _clear_done(self):
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t["done"]]
        removed = before - len(self.tasks)
        self._refresh()
        self._status(f"⌫ Odstraněno {removed} dokončených úkolů.")
        self._save()

    def _reset_all(self):
        if not self.tasks: return
        if messagebox.askyesno("Reset", "Opravdu vymazat VŠECHNY úkoly?",
                               parent=self.root):
            self.tasks.clear()
            self._refresh()
            self._status("⟳ Seznam byl kompletně vymazán.")
            self._save()

    # ── Pomocné ─────────────────────────────────────────────────────────────

    def _get_sel(self):
        sel = self.listbox.curselection()
        if not sel:
            self._status("⚠ Nejprve vyberte úkol.")
            return None
        return sel[0]

    def _on_select(self, _event=None):
        self.selected = self._get_sel()

    def _refresh(self, reselect=None):
        self.listbox.delete(0, "end")
        done_count = sum(1 for t in self.tasks if t["done"])
        total = len(self.tasks)

        for i, task in enumerate(self.tasks):
            prefix = "⚑ " if task["priority"] else "   "
            check  = "✔ " if task["done"] else "○ "
            label  = f"{prefix}{check}{task['text']}"
            self.listbox.insert("end", label)

            if task["done"]:
                self.listbox.itemconfig(i, fg=MUTED, bg=DONE_COL)
            elif task["priority"]:
                self.listbox.itemconfig(i, fg="#f4a261", bg=PANEL)
            else:
                self.listbox.itemconfig(i, fg=TEXT, bg=PANEL)

        self.count_lbl.config(
            text=f"{done_count}/{total} hotovo"
        )

        if reselect is not None and total > 0:
            idx = min(reselect, total - 1)
            self.listbox.selection_set(idx)
            self.listbox.see(idx)

    def _status(self, msg):
        self.status_lbl.config(text=msg)

    # ── Uložení / načtení ────────────────────────────────────────────────────

    def _save(self):
        try:
            with open(SAVE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def _load(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except Exception:
                self.tasks = []


# ── Spuštění ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
