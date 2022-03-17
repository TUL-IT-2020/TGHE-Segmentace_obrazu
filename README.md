
# TGHE

## Zadání
<p style="text-align: justify;">
Pro daný obrázek <b>n*n</b> pixelů ve stupních šedi <b>0...255</b> je třeba odlišit pixely vyobrazeného objektu O od kontrastního pozadí B (problém segmentace obrazu). Přitom není známo zda jde o tmavý objekt na světlém pozadí nebo naopak, ani není znám nějaký odstup intenzit objektu a pozadí. Předpokládáme však, že maximální rozdíl intenzit sousední pixelů <b>a</b> a <b>b</b> v rámci objektu <b>(a, b € O)</b> i v rámci pozadí <b>(a, b € B)</b> je alespoň o <b>2</b> stupně šedi menší než minimální rozdíl intenzit sousedních pixelů z nichž jeden je z objektu a druhý z pozadí <b>(a € O, b € B)</b>. Předpokládáme, že po obvodu obrázku jsou pouze pixely patřící k pozadí a detekovaný objekt nemá díry.

</p>

<p style="text-align: justify;">
Navrhněte a popište algoritmus založený na hledání minimální kostry, kde ohodnocení hran je dáno rozdílem intenzit sousedících pixelů. Formulujte problém jako grafovou úlohu. Co budou vrcholy, co hrany?
Určete složitost vaší implementace vzhledem k počtu pixelů obrázku.
</p>

<p style="text-align: justify;">
Vstup je textový soubor, kde na prvním řádku je velikost obrázku <b>n</b> a na dalších <b>n</b> řádcích je vždy <b>n</b> čísel udavajících intenzity v obrázku. Intenzity jsou čísla od 0 do 255. Výstup je ve stejném formátu jako vstup, jen místo intenzit je uvedena <b>0</b> pro pixel pozadí a <b>1</b> pro pixel objektu.
</p>

## Ukázka interakce s programem:
### Příklad vstupu:
```
5
0 0 1 0 0
0 1 4 5 0
0 5 5 6 1
0 6 6 3 2
1 0 1 2 2 
```
### Očekávaný výstup:
```
0 0 0 0 0
0 0 1 1 0
0 1 1 1 0
0 1 1 0 0
0 0 0 0 0
```
