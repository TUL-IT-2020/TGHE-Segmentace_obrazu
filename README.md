# TGHE

## Zadání
Pro daný obrázek **n*n** pixelů ve stupních šedi **0...255** je třeba odlišit pixely vyobrazeného objektu O od kontrastního pozadí B (problém segmentace obrazu). Přitom není známo zda jde o tmavý objekt na světlém pozadí nebo naopak, ani není znám nějaký odstup intenzit objektu a pozadí. Předpokládáme však, že maximální rozdíl intenzit sousední pixelů **a** a **b** v rámci objektu (**a,b € O**) i v rámci pozadí (**a,b € B**) je alespoň o **2** stupně šedi menší než minimální rozdíl intenzit sousedních pixelů z nichž jeden je z objektu a druhý z pozadí (**a € O, b € B**). Předpokládáme, že po obvodu obrázku jsou pouze pixely patřící k pozadí a detekovaný objekt nemá díry.

Navrhněte a popište algoritmus založený na hledání minimální kostry, kde ohodnocení hran je dáno rozdílem intenzit sousedících pixelů. Formulujte problém jako grafovou úlohu. Co budou vrcholy, co hrany?
Určete složitost vaší implementace vzhledem k počtu pixelů obrázku.

Vstup je textový soubor, kde na prvním řádku je velikost obrázku **n** a na dalších**n** řádcích je vždy **n** čísel udavajících intenzity v obrázku. Intenzity jsou čísla od 0 do 255. Výstup je ve stejném formátu jako vstup, jen místo intenzit je uvedena **0** pro pixel pozadí a **1** pro pixel objektu.
