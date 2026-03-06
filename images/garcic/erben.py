from collections import Counter

# Otevření souboru pro čtení (ujisti se, že název souboru je alice.txt)
with open('alice.txt', 'r', encoding='utf-8') as file:
    obsah = file.read()
    
    # Rozdělení textu na jednotlivá slova podle mezer a odřádkování
    slova = obsah.split()
    
    # --- 1. ZADÁNÍ: Celkový počet slov ---
    pocet_slov = len(slova)
    print(f"1. Celkový počet slov: {pocet_slov}")
    
    # --- 2. ZADÁNÍ: 16. nejčastější slovo ---
    pocetnost_slov = Counter(slova)
    nejcastejsi_slova = pocetnost_slov.most_common(16)
    
    sestnacte_slovo = nejcastejsi_slova[15][0]
    pocet_vyskytu_slova = nejcastejsi_slova[15][1]
    print(f"2. 16. nejčastější slovo je: '{sestnacte_slovo}' (výskyty: {pocet_vyskytu_slova})")
    
    # --- 3. ZADÁNÍ: Počet výskytů nejčastějšího písmene ---
    # Odstraníme mezery a odřádkování, abychom počítali jen písmena
    pismena = obsah.replace(" ", "").replace("\n", "")
    pocetnost_pismen = Counter(pismena)
    
    nejcastejsi_pismeno = pocetnost_pismen.most_common(1)[0]
    pismeno = nejcastejsi_pismeno[0]
    pocet_vyskytu_pismena = nejcastejsi_pismeno[1]
    print(f"3. Nejčastější písmeno je '{pismeno}' a odpověď do formuláře (počet výskytů) je: {pocet_vyskytu_pismena}")

    # --- 4. ZADÁNÍ: Počet různých osmipísmenných slov ---
    # Funkce set() z našeho seznamu odstraní všechny duplikáty (nechá jen unikátní slova)
    unikatni_slova = set(slova)
    
    # Vytvoříme seznam jen z těch slov, která mají přesně 8 znaků
    osmipismenna_slova = [slovo for slovo in unikatni_slova if len(slovo) == 8]
    pocet_osmipismennych = len(osmipismenna_slova)
    print(f"4. Počet různých osmipísmenných slov: {pocet_osmipismennych}")