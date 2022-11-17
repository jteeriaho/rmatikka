#!/usr/bin/env python
# coding: utf-8

# # Tilastollinen virheenarviointi   

#        
# Mittausvirheet voidaan jakaa kahteen tyyppiin:     
# 
# Tyyppi A: virheet, jotka johtuvat satunnaisista tekijöistä     
# Tyyppi B: virheet, jotka vaikuttavat määrättyyn suuntaan (esim. mittarin kalibrointivirheet)       
# 
# 
# ![virhelajit](images/kuva55.PNG)       
# 
#       
#       
# Satunnaisvirheen vaikutus tulokseen voidaan eliminoida toistamalla mittausta, jolloin mittaustulosten keskiarvo lähestyy suureen todellista arvoa. Systemaattisen virheen vaikutusta ei voi eliminoida toistolla.
# 

# ## Otannalla saadun tuloksen virhemarginaali

# ### Otantavirheet

# ```{admonition} Otantavirhe  
# :class: tip
# **Otantavirhe on otosten poiminnan satunnaisuudesta aiheutuva virhelähde.**
# ```

# #### Esimerkki otantavirheistä

# Oletetaan, että miespuolisten varusmiesten pituus noudattaa Gaussin normaalijakaumaa, jonka keskiarvo on 180 cm ja keskihajonta 8 cm.       
# 
# Tutkittaessa varusmiesten pituuksia käyttämällä 25 henkilön otoksia, otosten pituusjakaumat poikkeavat toisistaan johtuen otantavirheestä.       
# Kuvassa on kolmen otoksen jakaumat.
# 
# ![otantavirhe](images/kuva56.PNG)       
# 
# Huolimatta eroavaisuuksista, otoskeskiarvot 180.3 cm, 180.7 cm ja 181.3 cm ovat lähellä toisiaan.  
# 
# Voidaan todistaa, että kun otoskokoa kasvatetaan, otoskeskiarvo lähestyy populaatiokeskiarvoa (tässä esimerkissä siis 180 cm).       
# 
# Lisäksi otoskeskiarvot ovat normaalisti jakautuneet. 
# > Otoskeskiarvojen keskihajonta on $\frac{s}{\sqrt{n}}$ ,missä s on populaation keskihajonta ja n on otoskoko.   
# >
# >    
# > Otoskokoa (= mittauksen toistojen lukumäärää) kasvattamalla saadaan otantavirhe pienentymään halutulle tasolle. 
# 
# ![otosvirhe](images/kuva57.PNG)

# ###  Mittaussarjan keskiarvon keskivirhe

# ```{admonition} **Otoskeskiarvon keskivirhe**
# :class: tip
# Olkoon X tilastomuuttuja, jonka arvoista otetaan n:n kappaleen otos.Tällöin    
# 
# 1.  Paras arvio muuttujan X keskiarvoksi on otoskeskiarvo
# 
# 2.  Otoskeskiarvojen keskihajonta eli keskivirhe on $\frac{s}{\sqrt{n}}$, 
# missä n on otoskoko ja s on muuttujan X keskihajonta            
# (jos X:n keskihajonta ei tunneta, käytetään otoksen keskihajontaa)
# 
# 3.  Muuttujan X  keskiarvon virhemarginaali riippuu vaaditusta luottamustasosta, joka määritellään todennäköisyytenä, että oikea keskiarvo on virhemarginaalin sisäpuolella.
# 
# X:n virhemarginaali $\Delta X = t \frac{s}{\sqrt{n}}$  , missä 
# t = otoskoosta ja luottamustasosta riippuva **kattavuuskerroin**    
# 
# > Suurilla otoskoon arvoilla ( n > 50) 95% luottamustasoa vastaa t = 1.96, ja       
# > 99% luottamustasoa vastaa t = 2.58    (perustuvat normaalijakauman kertymäfunktioon)   
# > 
# > **Merkitsevyystaso.** Luottamustason sijasta esim. Excel-funktioissa käyttää sen komplementtia, jota sanotaan *merkitsevyystasoksi*.     
# > Ts.  95% luottamustaso vastaa 5% merkitsevyystasoa, 99% luottamustasoa vastaa 1% merkitsevyystaso
# 
# ```

# ```{admonition} **Numeerisen muuttujan mittaussarjan virhemarginaali**
# :class: tip
# 
# $\Delta X = t \frac{s}{\sqrt{n}}$  , missä 
# t = kattavuuskerroin, s = populaatiokeskihajonta (tai otoskeskihajonta, jos em. ei tiedossa), n = otoskoko    
# 
# Kattavuuskerroin t riippuu otoskoosta ja luottamustasosta (yleensä joko 95% tai 99%).      
# Ilman laskinta tai Exceliä kattavuuskertoimet eri otoskoille löytyvät taulukkokirjoista tai netistä. Alla taulukko kattavuuskertoimista eri suuruisille otoksille.  
# 
# ```

# **Kattavuuskertoimia** t tavallisimmille merkitsevyystasoille, n - 1 =  otoskoko - 1      
# 
# ![ttaulu](images/kuva58.PNG)   
# 
# > Taulukon sijasta virhemarginaali voidaan laskea Excel- funktiolla LUOTTAMUSVÄLI.T.

# ###  Excel -funktio LUOTTAMUSVÄLI.T (engl. CONFIDENCE.T)

# Pienillä otoksilla (n < 50) otoskeskiarvojen jakauma noudattaa ns. Studentin T -jakaumaa, joka lähestyy suuremmilla otoksilla normaalijakaumaa.       
# 
# Excel -funktio **LUOTTAMUSVÄLI.T(merkitsevyystaso; keskihajonta; otoskoko)** laskee virhemarginaalin otoksesta saadulle muuttujan X keskiarvolle käyttäen kaavaa $\Delta X = t \frac{s}{\sqrt{n}}$.      
# 

# ```{admonition} Asfaltin tiheys määritettiin kymmenestä näytteestä, joiden tiheydet olivat 2468, 2431, 2569, 2518, 2667, 2608, 2494, 2334, 2629ja 2570.  Otoskeskiarvo ja -keskihajonta ovat $2529 g/cm^3$ ja $101 g/cm^3$. Mikä on mittaussarjan perusteella asfaltin tiheys? 
# :class: dropdown      
# 1) Asfaltin tiheydeksi annetaan otoskeskiarvo eli 2529     
# 
# 2) Tiheyden absoluuttinen virhe 95% merkitsevyystasolla saadaan Excel funktiolla    
# **= LUOTTAMUSVÄLI.T(5%;101;10)**, joka antaa virheeksi **72.2**      
# 
# (Ilman Exceliä tulos saadaan kaavalla $\Delta X = t \frac{s}{\sqrt{n}} = 2.262\frac{101}{\sqrt{10}}= 72.2$.      
# Kattavuuskerroin 2.262 löytyy yo. taulukosta riviltä n - 1 = 10 - 1 = 9) 
# 
# ```

# ###  Suhteellisen osuuden luottamusväli

# Gallup - tutkimuksissa tutkittava muuttujana on jonkin ehdokkaan tai ajatuksen kannatusprosentti, ts. **suhteellinen osuus**.   Otoskoot Gallup tutkimuksissa ovat suuria, yleensä 500 - 2500. Satunnaistettujen otosten tulokset noudattavat ns. binomijakaumaa.    
# 
# Suhteellisen osuuden virhemarginaali riippuu otoskoosta n ja ehdokkaan kannatuksesta p seuraavasti:  

# ```{admonition} **Suhteellisen osuuden virhemarginaali**
# :class: tip
# 
# $\Delta p = t \sqrt\frac{p(1-p)}{n}$
# 
# n = otoskoko, p = kannatusprosentti desimaalilukuna (esim. 0.35 vastaa 35% kannatusta), 
# kattavuuskerroin t = 1.96 (95% luottamustaso) tai t = 2.34 (99% luottamustasolla)
# 
# ```

# ```{admonition} Sähköauton hankintaa harkitsi 38.4 % kyselyyn osallistuneista. Otoskoko oli 1000 henkeä. Mikä oli kyselyn virhemarginaali? 
# :class: dropdown
# $\Delta p = t \sqrt\frac{p(1-p)}{n} = 1.96 \sqrt\frac{0.384(1-0.384)}{1000} = 0.030 = 3.0\%$      
# 
# Vastaus: virhemarginaali on $\pm 3.0$ prosenttiyksikköä
# ```

# Jos asetetaan Gallup- tutkimukselle etukäteen vaatimus tietystä virhemarginaalista, voidaan tarvittava otoskoko n ratkaista em. yhtälöstä seuraavassa muodossa:  

# ```{admonition} **Otoskoon määrittäminen, kun virhemarginaali on annettu**
# :class: tip
# 
# Otoskoko $n=\frac{p(1-p)t^2}{\Delta p^2}$
# 
# p = kannatusprosentti desimaalilukuna, t = kattavuuskerroin, $\Delta p$ = virhemarginaali
# 
# 
# ```

# ```{admonition} Presidenttigallupissa eniten kannatusta omaavan ehdokkaan on 23 % luokkaa. Kuinka suuri otoskoko tarvitaan seuraavassa gallupissa, jotta ehdokkaan kannatusmittauksessa päästäisiin 2 % virhemarginaaliin?   
# :class: dropdown
# Otoskoko $n=\frac{0.23(1-1.023)1.96^2}{0.02^2} = 1701$      
# 
# Vastaus: Otoskoon on oltava n. 1700
# ```

# Huom!  Otoskoko riippuu kannatusprosentista siten, että suurin otoskoko tarvitaan n. 50 % kannatusta mitattaessa tiettyyn virhemarginaaliin pääsemiseksi.

# ### Ratkaistuja esimerkkejä

# ```{admonition} Tavaratalon asiakkaiden keski-ikää selvitettiin kysymällä ikä 200 satunnaisesti valitulta asiakkaalta.  Otoskeskiarvo oli 41.3 v  ja keskihajonta 23.5 v. Ilmoita tutkimuksen perusteella asiakkaiden keski-ikä ja sen virhemarginaali (95% luottamustasolla) 
# :class: dropdown
# Keski-iäksi annetaan otoskeskiarvo 41.3       
# 
# Virhemarginaali saadaan Excel-kaavalla      
# **=LUOTTAMUSVÄLI.T(5% ; 23,5 ; 200)** antaa tuloksen 3.3      
# 
# Vastaus: Keski-ikä on $(41.3 \pm 3.3)$ vuotta
# ```

# ```{admonition} 500 satunnaisesti valitulta suomalaiselta kysyttiin, käyttävätkö he pankkikortin lähimaksuominaisuutta kaupan kassalla. Kyllä – vastauksia oli  47.5 %. Ilmoita tämän perusteella lähimaksua käyttäjien prosenttiosuus Suomessa virherajoineen. 
# :class: dropdown
# $\Delta p = t \sqrt\frac{p(1-p)}{n} = 1.96 \sqrt\frac{0.475(1-0.475)}{500} = 0.044 = 4.4\%$     
# 
# Vastaus: Lähimaksua kannattaa $(47.5 \pm 4.4)\%$ 
# ```
