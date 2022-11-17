#!/usr/bin/env python
# coding: utf-8

# # Kuljetusten optimointi

# Eräs infrarakentamisessa käytössä oleva optimointimenetelmä liittyy kuljetuksiin. Menetelmä tunnetaan nimellä **lineaarinen optimointi**.     
# 
# Sen käyttämän **Simplex -algoritmin** kehitti George Dantzig v. 1946 kehittäessään USA:n ilmavoimille  menetelmiä, joilla suunnitteluprosesseja voitaisiin mekanisoida ja automatisoida.   
# 
# Lineaarista optimointia käytetään myös teollisuudessa tuotannon optimoinnissa, sekä kaupan alalla, josta syystä lineaarista optimointia opetetaan myös ekonomiopintojen matematiikassa.  

# ## Yksinkertainen 2 muuttujan tapaus

# Lineaarisen ausekkeen a x + b y , missä vakiot , suurimman tai pienimmän arvon määrittämistä tasoalueessa nimitetään lineaariseksi optimoinniksi. Lauseke voi esittää esim. kahden eri tuotteen myyntivoittoa. 
# Näiden tuotteiden valmistusta rajoittavat ehdot, jotka aiheituvat rajallisista työaika-, valmistusmateriaali- ja tuotantokustannusresursseista, voidaan usein havainnollistaa tasoalueena.

# ```{admonition} Esim. Epäyhtälöt $x + 3 y ≤ 18,  3 x + 2 y ≤ 19, x ≥  0\text{ ja }y ≥  0$ määrittävät nelikulmion   x,y – tasossa. Määritä lausekkeen $f =  5x +4 y$ suurin arvo nelikulmiossa    
# :class: tip     
# WolframAlphalla kuva rajoitteiden määräämästä nelikulmiosta syntyy kätevästi komennolla:       
# $\color{red}{\text{plot }\{x + 3 y ≤ 18,  3 x + 2 y ≤ 19, x ≥  0, y ≥  0\}}$ 
# ![linop](images/kuva19.PNG) 
#   
# Maksimoitavan funktion f = 5 x + 4 y osittaisderivaattojen muodostamaa vektoria $(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}) = (5,4) $ kutsutaan funktion  **gradientiksi**.    
# 
# 
# Lineaarisen funktion f kuvaaja on tasopinta 3D - avaruudessa. Gradientti kertoo, mihin suuntaan x,y - tasossa funktio f = 5x+4y kasvaa jyrkimmin.   
# 
# Kuvaan on piirretty gradientin suuntaisia vektoreita. Kuvan perusteella on ilmeistä, että funktio f saavuttaa suurimman arvonsa pisteessä P, joka on gradientin suunnassa kauimmainen nelikulmion piste.      
# 
#     
# Piste P on kahden nelikulmion  rajaviivan x + 3 y = 18 ja 3 x + 2 y = 19 risteyskohdassa. Ratkaisemalla yhtälöpari esim. laskinkomennolla $\color{red}{\text{solve }x + 3 y = 18,  3 x + 2 y = 19}$, saadaan P:n koordinaateiksi x = 3 ja  y = 5.      
# 
# Funktion f  suurin arvo on siten $f(3,5) = 5\cdot 3 + 4\cdot 5 = 35$  
# 
# ```

# ## Usean muuttujan lineaarinen optimointi  

# ![linop](images/kuva20.PNG) 
#   
# 

# ```{admonition} Maksimoitava tai minimoitava ns. **tavoitefunktio** f on lineaarinen muuttujien $x_1,x_2,....,x_n$ lauseke $f = a_1 x_1+a_2 x_2+....+a_n x_n$. Rajoitteet ovat muuttujien välisiä lineaarisia yhtälöitä tai epäyhtälöitä.  
# :class: tip     
# 1. Edellisen esimerkin monikulmiota vastaa moniulotteisen avaruuden monitahokas. 
# 
#   
# 2. Tavoitefunktion f gradientti $(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},....) = (a_1,a_2,...,a_n) $ muodostuu muuttujien kertoimista.      
# 
# 
# 3. Tavoitefunktion f maksimi löytyy monitahokaan gradientin suunnassa kauimmaisesta kärkipisteestä. Minimi löytyy gradientille vastakkaisessa suunnassa olevasta kauimmaisesta kärkipisteestä.     
# 
# 
# 4. Simplex - algoritmissa valitaan lähtökohdaksi jokin kärkipiste. Algoritmissa edetään piste pisteeltä kohti tavoitetta gradientin suuntaisesti.      
# 
# 
# 5. Käsin laskettuna algoritmi on hidas toteuttaa, mutta tietokoneelle koodattuna tehokas. Simplex algoritmi on mukana lukuisissa tietokoneohjelmissa, mm. Excel taulukkolaskentaohjelmassa.  Netistä löytyy lineaariseen ohjelmointiin ilmaisia online  -laskimia, joita käytämme tämän osuuden tehtävän ratkaisemiseen.   
#     
# ```

# ## Kuljetusprobleema

# Kuljetusten optimoinnissa tavoite on säästää kuljetuskustannuksia vähentämällä ajokilometrit minimiin. Minimoitava funktio on lineaarinen, muuttujina ovat kuljetettavat määrät ja kertoimina kilometrimäärät.  

# ```{admonition} Esimerkki  
# :class: tip     
# Kuljetusyritys toimittaa soraa tierakennuskohteisiin. Sillä on kolme soravarastoa  V1, V2 ja V3 joissa on soraa 1500 $m^3$, 3000 $m^3$ ja 2000 $m^3$.   Toimituskohteita on myös kolme:   K1, K2 ja K3, joihin toimitettavat määrät ovat 1200 $m^3$, 1900 $m^3$ ja 2100 $m^3$.   Alla olevassa taulukossa on ruutuihin kirjoitettu etäisyydet soravarastojen ja kohteiden välillä.    Määritä kustakin soravarastosta kuhunkin kohteeseen toimitettavat määrät siten, että kuljetusten kokonaiskilometrimäärä on mahdollisimman pieni.
# ![sora](images/kuva21.PNG)
# 
# ```

# ## Ongelman matemaattinen muotoilu

# Merkitään varastoista kohteisiin kuljetettavia kuutiomääriä muuttujilla x1,x2,...,x9 ao. taulukon mukaisesti:        
# 
# 
# |    | V1 | V2 | V3 |
# |----|----|----|----|
# | K1 | x1 | x2 | x3 |
# | K2 | x4 | x5 | x6 |
# | K3 | x7 | x8 | x9 |
# 
# Ongelma voidaan esittää matemaattisessa muodossa seuraavasti.    
# 
# **Minimoi** 32x1 +54x2 +17x3 +26x4 +41x5 +19x6 +38x7 +17x8 +24x9       
# **ehdoilla**          
# x1 + x2 + x3 = 1200          
# x4 + x5 + x6 = 1900         
# x7 + x8 + x9 = 2100          
# x1 + x4 + x7 ≤ 1500        
# x2 + x5 + x8 ≤ 3000       
# x3 + x6 + x9 ≤ 2000         
# x1,x2,x3,x4,x5,x6,x7,x8,x9 ≥ 0    
# 
# Osa ehdoista on yhtälöitä johtuen siitä että kohteisiin tarvitaan täsmälleen oikea määrä soraa.    
# Toiset ehdot ovat epäyhtälöitä, joiden rajoitteina on varastojen sisältämät maksimimäärät.  

# ## Ratkaisu online laskimella  http://www.phpsimplex.com/en/ 

# 1. Siirryttyäsi linkin sivulle, käynnistä 1. rivillä olevasta linkistä **PHPSimplex** laskimeen       
# 
# 2. Aloitussivulla kysytään muuttujien $x_i$ määrää ja rajoitteiden määrää.  Rajoitteiden määrään lasketaan varastohin liittyvät 3 epäyhtälöä ja kohteisiin liityvät 3 yhtälöä.     
# 
# $\color{blue}{\text{    How many decision variables are the problem? }}   \color{red}9$  
# $\color{blue}{\text{    How many constraints? }}   \color{red}6$
# 
# 3. Paina Continue - painiketta. Avautuvassa lomakkeessa kysytään aluksi, haetaanko funktiolle maksimia vai minimiä. Oletusarvona on maksimi, mikä kuljetusprobleemassa pitää muistaa vaihtaa.     
# 
# $\color{blue}{\text{   What is the objective of the function? }}   \color{red}{minimize}$       
# 
# 4. Täytä kohtaan **Function:** tavoitefunktion kertoimet 32, 54, 17, 26, ....      
# 
# 5. Täytä kohtaan **Constraints:** kutakin ehtoa vastaavat kertoimet, yhtäsuuruus tai erisuuruusmerkki, sekä rajoitteen oikean puolen arvo. 
# 
# Esim. ensimmäinen rajoite on yhtälö x1 + x2 + x3 = 1200.     
# Kirjoita lomakkeeseen muuttujien x1, x2 ja x3 kertoimiksi luku 1,  muuta ≤ -merkki = - merkiksi, kirjoita rivin loppuun 1200.  Muiden muuttujien kertoimet ovat nollia, ne voi jättää tyhjäksi.   
# 
# Täytetty lomake näyttää seuraavalta:     
# ![simp](images/kuva22.PNG) 
# 
# 6. Paina **Continue** painiketta
# 
# 7. Valitse **Direct Solution**  ja saat ratkaisun, jonka ylärivillä on tavoitefunktion maksimiarvo, ja alemmilla riveillä optimia vastaavat muuttujien arvot  (kuljetusmäärät kustakin varastosta kuhunkin kohteeseen)    
# 
# The optimal solution value is Z = 99900      
# X1 = 0                 
# X2 = 0                
# X3 = 1200               
# X4 = 1100                
# X5 = 0               
# X6 = 800             
# X7 = 0              
# X8 = 2100              
# X9 = 0            

# Optimiratkaisua vastaavat kuljetusmäärät taulukkoon täydennettyinä          
# ![optimi](images/kuva25.PNG)
