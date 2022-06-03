![Tests](https://github.com/elPytel/TGHE-Segmentace_obrazu/actions/workflows/main.yml/badge.svg)

# TGHE
# Problém Segmentace obrazu
Karel Najman, Jaroslav Körner

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

## Ukázka interakce s programem

### Příklad vstupu

```bash
5
0 0 1 0 0
0 1 4 5 0
0 5 5 6 1
0 6 6 3 2
1 0 1 2 2 
```

### Očekávaný výstup

```bash
0 0 0 0 0
0 0 1 1 0
0 1 1 1 0
0 1 1 0 0
0 0 0 0 0
```


## Grafová formulace problému
Formulace úlohy pomocí grafové reprezentace, vrcholy, hrany, ohodnocení

Obrázek n x n pixelů ve stupních šedi v hodnotách  0…255. Převedeme na graf G kde vrcholy odpovídají pixelům a hodnoty pro každý vrchol od 0…255. Hrany tvoří křížové okolí vrcholu/pixelu s ohodnocením hrany rovno rozdílů hodnot vrcholů |V1-V2|. Hodnoty hran jsou tedy vždy nezáporné.

- **G** obecný, rovinný, souvislý, neorientovaný, cyklický graf
- |V| = n^2
- |E| = S/4*|V|
- val(E)=|Vi-Vj|

## Vhodný algoritmus pro řešení daného problému
Nejvhodnějším algoritmem pro danou úlohu je Borůvkův algoritmus s vynecháním závěrečného kroku propojení posledních dvou souvislých komponent. 

## Úpravy učebnicového algoritmu pro úlohu segmentace obrazu
My jsme se však rozhodli vydat cestou jinou a prošlapat dosud neodhalené slepé uličky algoritmizace. Z toho důvodu jsme si za cíl vytyčili použít Jarníkův algoritmus, který sice kostru najde, ale přidá nám ještě další zbytečné kroky na víc. 
Úprava algoritmu spočívala například v tom, že nemusíme převádět graf na seznam sousedů (hash map), díky pravidelnosti grafu, tedy sousedé libovolného vrcholu jsou dohledatelní podle “křížových” souřadnic v matici zpracovávaného obrazu.
Po nalezení (minimální) kostry je zapotřebí odstranit nejdražší hranu z kostry a tak jí rozdělit na dvě souvislé komponenty, jedna tvoří popředí a druhá pozadí. 

## Použité datové struktury
- Souřadnice - coord = [x,y]
  - jako prostý list
- Vrchol - Vertex(coord).
- Hrana - Edge(vertex1, vertex2).
- Matice vrcholů je reprezentovaná v poli (list listů)
  - umožňuje přístup na daný vrchol v O(1).
- Prioritní fronta hran implementovaná pomocí knihovny heapq “heap-queue”
  - z důvodu optimalizace pro odebrání nejmenšího prvku.
- Minimální kostra je ukládána jako list hran.

## Proč ukládat kostru jako list?
Máme rozdělit kostru na dvě komponenty přes nejcennější hranu. Kostru vytváříme postupným přidáváním nejlevnější hrany, proto se nemůže stát že by hrana z popředí byla přidána do listu až po překročení nejdražší hrany a tudíž nám stačí u hran tvořící kostru pouze zaznamenat jejich pořadí přidání a na to nám stačí prostý list.
Na výsledné rozdělení na popředí a pozadí využijeme funkce řezu listu přes “půlící” index (index nejcennější hrany).

## Časová složitost implementovaného algoritmu
Složitost načtení vstupu/výstupu zanedbáváme.
1. Jarníkův algoritmus - O(|E|*log |V|) 
1. Rozdělení grafu na dvě komponenty - O( |V|-1) , strom má  |V|-1 hran, aplikace lineárního vyhledávání maxima na nesetříděné množině.
1. Obarvení popředí/pozadí - O(|V|-1), průchod listem.

Součet jednotlivých kroků: O(|E|*log |V| +2*(|V|-1) ) 
Násobení konstantou ve složitosti zanedbáváme a uplatňují se jen nejvyšší mocniny členů. Výsledná složitost: O(|E|*log |V|) 

