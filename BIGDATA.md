# 🎨 Zpracování dat

Ukázky zpracování zvoleného datového souboru.
Každý student má vlastní sekci se svým jménem, odkazem na GitHub
a náhledy obrázků uložených ve složce `images/`.

**Zadání**

S pomocí generativního AI chatbotu (Claude), GitHub Copilot, ChatGPT, Gemini ) vytvořte seznam s vnořeným seznamem, řetězcem nebo tuple, např. seznam tramvají z Prahy ve formátu: (typ, maximální_rychlost_km_h, rok_první_výroby) a databázi smysluplným způsobem zpracujte:

filtrování seznamu, řazení podle různých atributů, výpočet popisných statistik, grafická reprezentace - histogram.
Popište databázi se kterou jste pracovali a vložte histogram s krátkým komentářem. Ve dvou větách napište závěr vašeho průzkumu. 

Základy práce ze seznamy - sdílený soubor <a href="https://colab.research.google.com/drive/1IX0X1sry5NnNvipQ6ETWMmxATD_Ig9pm?usp=sharing" target="_blank">Tramvaje.ipynb</a>


**Rychlá navigace:**  
[Balanets](#anastasiia-balanets) ·
[Bartuněk](#michael-bartuněk) ·
[Borovička](#ondřej-borovička) ·
[Brož](#adam-brož) ·
[Fenynets](#vitalii-fenynets) ·
[Filip](#tomáš-filip) ·
[Garčic](#vojtěch-garčic) ·
[Horáček](#daniel-horáček) ·
[Hron](#michal-hron) ·
[Jandák](#tomáš-jandák) ·
[Jiránek](#lukáš-jiránek) ·
[Kravets](#maksym-kravets) ·
[Kreperát](#šimon-kreperát) ·
[Kryvka](#karyna-kryvka) ·
[Kubala](#šimon-kubala) ·
[Kubát](#pavel-kubát) ·
[Mandziuk](#mykola-mandziuk) ·
[Mayrhofer](#hynek-mayrhofer) ·
[Miláček](#marek-miláček) ·
[Nahornyi](#mark-nahornyi) ·
[Pavelka](#dominik-pavelka) ·
[Povolný](#antonín-povolný) ·
[Procházka](#vincent-procházka) ·
[Řehák](#marek-řehák) ·
[Sauer](#matyáš-sauer) ·
[Suchánsky](#jakub-suchánsky) ·
[Sunkovský](#tomáš-sunkovský) ·
[Škarvan](#petr-škarvan) ·
[Štěpán](#tomáš-štěpán) ·
[Viták](#jáchym-viták)

---

## Anastasiia Balanets
🔗 https://gist.github.com/qqqwwwaaarr/8836721a765b9ab68eea0549dbb75a66

![Obrázek 1](images/balanets/obrazek2.png)

---

## Michael Bartuněk
🔗 https://github.com/SkyGod934/Michael-Barunek

![Obrázek 1](images/bartunek/obrazek2.png)

---

## Ondřej Borovička
🔗 https://github.com/dedeczech/Borovicka

![Obrázek 1](images/borovicka/obrazek2.png)

---

## Adam Brož
🔗 https://github.com/Brozovec/broz

Popis práce a dosažené výsledky
Tento notebook provádí základní analýzu jednoduchého datasetu autobusů a demonstruje klíčové kroky při práci s daty pomocí knihoven pandas a matplotlib.

1. Import knihoven
V úvodu notebooku byly importovány potřebné knihovny: pandas pro práci s datovými rámci a matplotlib.pyplot pro vizualizaci dat.

2. Vytvoření datasetu
Byl vytvořen malý dataset obsahující informace o autobusech (typ, kapacita osob, rok první výroby). Tento dataset byl následně převeden do datového rámce df knihovny pandas, což umožnilo jeho snadnější manipulaci a analýzu. Zobrazením datového rámce jsme si ověřili jeho správné načtení a strukturu:

                 typ  kapacita  rok_vyroby
0        Karosa B732        95        1982
1        Karosa B952       100        2002
2           SOR NB12       105        2008
3           SOR NB18       160        2009
4  Solaris Urbino 12       110        2014
3. Filtrování dat
Data byla filtrována tak, aby zobrazovala pouze autobusy vyrobené po roce 2000. Tímto krokem jsme získali podmnožinu dat, která splňuje specifickou podmínku. Výsledek filtrace je následující:

                 typ  kapacita  rok_vyroby
1        Karosa B952       100        2002
2           SOR NB12       105        2008
3           SOR NB18       160        2009
4  Solaris Urbino 12       110        2014
4. Řazení dle kapacity
Dataset byl seřazen podle kapacity autobusů sestupně (od největší po nejmenší). To nám umožnilo rychle identifikovat autobusy s nejvyšší kapacitou. Seřazený datový rámec vypadá takto:

                 typ  kapacita  rok_vyroby
3           SOR NB18       160        2009
4  Solaris Urbino 12       110        2014
2           SOR NB12       105        2008
1        Karosa B952       100        2002
0        Karosa B732        95        1982
5. Vizualizace – histogram kapacit
Pro lepší pochopení distribuce kapacit autobusů byl vytvořen histogram. Tento graf vizuálně zobrazuje, jak často se jednotlivé rozsahy kapacit v datasetu vyskytují, a poskytuje rychlý přehled o rozložení dat.

Celkově notebook demonstruje základní operace s daty jako je vytváření, filtrování, řazení a vizualizace, které jsou klíčové pro jakoukoliv datovou analýzu.


![Test_gradiant](images/broz/img.png))

---

## Vitalii Fenynets
🔗 https://github.com/Ekzarmfs/Fenynets.git

![Obrázek 1](images/fenynets/obrazek2.png)

---

## Tomáš Filip
🔗 https://github.com/tomasfilip2009-ship-it/Tom-Filip

![Obrázek 1](images/filip/obrazek2.png)

---

## Vojtěch Garčic
🔗 https://github.com/JouJoumanCZ/skola
Analýza dvanácti českých řek v Pythonu pomocí seznamu toulů ukázala průměrnou délku 232 km a průtokovou dominanci Labe. Histogram odhaluje, že většina toků měří 100–250 km, přičemž pouze tři hlavní tepny přesahují 300 km, což dokládá soustředění sítě do několika klíčových koryt. Závěrem lze říci, že česká říční síť sestává z mnoha středních přítoků napájejících pár hlavních tepen. Vodnatost toku přitom závisí více na ploše povodí než na jeho celkové délce.
![Obrázek 1](images/garcic/obrazek2.png)

---

## Daniel Horáček
🔗 https://github.com/Dndskid/Horacek
vytváří barevný sloupcový histogram popularity filmových žánrů (Akční, Komedie, Drama, Horor, Sci-Fi, Romantické) od 1980s do 2020s s detailními statistikami.
![Obrázek 1](images/horacek/obrazek2.png)

---

## Michal Hron
🔗 https://github.com/michal670/Hron---repozit-

![Obrázek 1](images/hron/obrazek2.png)

---

## Tomáš Jandák
🔗 https://github.com/Tjandak/Jandak

![Obrázek 1](images/jandak/obrazek2.png)

---

## Lukáš Jiránek
🔗 https://github.com/MentysTV/Jir-nek-Luk-
<img width="986" height="737" alt="Snímek obrazovky 2026-01-09 100638" src="https://github.com/user-attachments/assets/d15e88ef-15ad-4187-8d31-454ca221f3f6" />

![Obrázek 1](images/jiranek/obrazek2.png)

---

## Maksym Kravets
🔗 https://github.com/Maomi0906/Kravets-Maksym

![Obrázek 1](images/kravets/obrazek2.png)

---

## Šimon Kreperát
🔗 https://github.com/Simanski7/Kreperat

![Obrázek 1](images/kreperat/obrazek1.png)

---

## Karyna Kryvka
🔗 https://github.com/moonlight-898/Karina

![Obrázek 1](images/kryvka/obrazek2.png)

---

## Šimon Kubala
🔗 https://github.com/S-1man/ZacatkyPythonu---Kubala

![Obrázek 1](images/kubala/obrazek2.png)

---

## Mykola Mandziuk
🔗 https://github.com/pepsikolya/stocks

![Obrázek 1](images/mandziuk/obrazek2.png)
Vizualizace Hustoty Zalidnění

Tento projekt je jednoduchý Python skript pro analýzu demografických dat. Jeho hlavním cílem je vypočítat hustotu zalidnění (počet obyvatel na km²) pro různé země světa a vizualizovat výsledky formou přehledného grafu.
---

## Hynek Mayrhofer
🔗 https://github.com/hynekmayrhofer1/Hynek-Mayrhofer

![Obrázek 1](images/mayrhofer/Obrazek2.png)

---

## Marek Miláček
🔗 https://github.com/marek-milacek/MMilacek

![Obrázek 1](images/milacek/obrazek2.png)

---

## Mark Nahornyi
🔗 https://github.com/MarkQTN/SPSD-Nahornyi

![Obrázek 1](images/nahornyi/obrazek2.png)

---

## Pavel Kubát
🔗 https://github.com/Piratesk1/Kubat

Histogram vlastností letadel

Graf zobrazuje dolet jednotlivých letadel v kilometrech. Je vidět, že Airbus A380 a Boeing 747 mají největší dolet, zatímco MiG-21 a Cessna 172 patří k letadlům s nejkratším doletem.
![Graf](images/kubat/graf.png)

---

## Dominik Pavelka
🔗 https://github.com/dominikpavelka1515/Dominik-Pavelka/tree/main

![Obrázek 1](images/pavelka/obrazek2.png)

---

## Antonín Povolný
🔗 https://github.com/TondaPovolny/Povolny

Histogram hodnocení filmů z minulého století

Graf zobrazuje kolik filmů má stejné hodnoce a průměrné hodnocení. Je vidět že průměrné hodnocení je lehce po 9 body z 10.
![Obrázek 1](images/povolny/obrazek2.png)

---

## Vincent Procházka
🔗 https://github.com/VincentProchazka/Vincent-Prochazka

![Obrázek 1](images/prochazka/obrazek2.png)

---

## Marek Řehák
🔗 https://github.com/MarekRehak/-eh-k.git

![Obrázek 1](images/rehak/obrazek2.png)


---

## Matyáš Sauer
🔗 https://github.com/MatyaSau/Sauer

![Obrázek 1](images/sauer/obrazek2.png)

---

## Petr Škarvan
🔗 https://github.com/Petr-Skarvan/skarvan.py

![Obrázek 1](images/skarvan/obrazek2.png)

---

## Tomáš Štěpán
🔗 https://github.com/Tomas120cz/Stepan

![Obrázek 1](images/stepan/obrazek2.png)

---

## Jakub Suchánsky
🔗 https://github.com/jakubsuchansky/Suchansky
Histogram Denních Teplot Během Roku
![Obrázek 1](https://github.com/jakubsuchansky/Suchansky/blob/main/obrazek2.png)

Histogram denních teplot během roku znázorňuje rozložení průměrných teplot za všech 365 dní. Z grafu je patrné několik vrcholů odpovídajících jednotlivým ročním obdobím – nejvíce dní se soustředí kolem jarních a podzimních teplot, zatímco extrémně nízké zimní a vysoké letní teploty se vyskytují méně často.

---

## Tomáš Sunkovský
🔗 https://github.com/TomyssCZ/Tomas-Sunkovsky

![Obrázek 1](images/sunkovsky/obrazek2.png)

---

## Jáchym Viták
🔗 https://github.com/Jachy47/Vitak2

![Obrázek 1](https://github.com/motol2/Prog2/blob/main/images/vitak/disky.png?raw=true)
Graf znázorňuje porovnání cen různých SSD a HDD disků v českých korunách.
Je vidět, že SSD disky jsou obecně dražší než HDD při stejné nebo podobné kapacitě.
Nejlevnější variantou v grafu je HDD 2TB s 7200 otáčkami, který stojí přibližně 980 Kč.
Naopak nejdražší položkou je SSD 1TB s cenou okolo 1900 Kč.
SSD 1TB NVMe je o něco levnější než klasické SSD 1TB, ale stále výrazně dražší než HDD disky.
HDD 1TB a HDD 2TB mají poměrně podobné ceny, přestože se liší kapacitou.
Celkově graf ukazuje, že vyšší rychlost a modernější technologie u SSD disků se odráží ve vyšší ceně.
---

🗳️ **Hlasování:**  
Použijte reakce (👍 ❤️ 🚀) u obrázků nebo mentimeter 23. 1..
