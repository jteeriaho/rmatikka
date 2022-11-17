#!/usr/bin/env python
# coding: utf-8

# # Määrätty integraali    

# Olkoon f(x) välillä $[a,b]$ määritelty jatkuva funktio, joka saa positiivia arvoja ko. välillä.    
# 
# Pinta-ala, joka käyrän y = f(x) ja x- akselin väliin välillä $[a,b]$ voidaan määrittää seuraavasti:      
# Jaetaan väli $[a,b]$ n:ään yhtäsuureen osaväliin, joiden leveys $\Delta x = \frac{b-a}{n}$.       
# ![integ](images/kuva27.PNG)        
# 
# 
# Pinta-alan likiarvo saadaan laskemalla summa $\sum_{i=0}^{n}f(x_i)\Delta x$, missä $x_i$:t ovat osavälien keskipisteitä.    
# 
# Kun osavälien lukumäärä n lähestyy ääretöntä, saadaan raja-arvona kysytty pinta-ala.    
# 
# $A = \underset{\Delta x \to 0}{lim}\hspace{3mm} \Sigma f(x_i)\Delta x$         
#         
# Summalauseketta kaavan oikella puolen kutsutaan **Riemannin summaksi**.

# ## Määrätyn integraalin määritelmä

# ```{admonition} **Määritelmä**
# :class: tip
# 
# Funktion f(x) määrätty integraali a:sta b:hen $\int_{a}^{b}f(x)dx$ määritellään Riemannin summan raja-arvona         
# 
# $\int_{a}^{b}f(x)dx = \underset{n\to \infty }{lim}\hspace{3mm} \overset{n}{\underset{i=0}{\Sigma}}f(x_i)\Delta x$
# 
# 
# ```

# ```{admonition} Esim. Laske integraalin $\int_{0}^{4} \sqrt(x) dx$ likiarvo kaavalla $\sum_{i=0}^{n}f(x_i)\Delta x$ jakamalla väli $[0,4]$ kahdeksaan osaan.
# :class: dropdown
# Osavälin leveys $\Delta x$ = 0.5.  Osavälien keskipisteet $x_i $ovat 0.25, 0.75, 1.25, ...., 3.75      
# 
# $\int_{0}^{4} \sqrt(x) dx \approx (\sqrt {0.25}+ \sqrt {0.75} + ... + \sqrt {3.25}  + \sqrt {3.75})\cdot 0.5 = 5.352 $      
# 
# (vrt. Algebralaskimella saatu tarkka arvo =  5.333
#  
# ```

# Määrätty integraali lasketaan tarkasti **määrittämällä funktion f(x) integraalifunktio F(x)** ja käyttämällä seuraavaa lausetta:

# ## Määrätyn integraalin laskeminen integraalifunktion avulla

# ```{admonition} **Määrätyn integraalin laskeminen integroimalla**
# :class: tip
# 
# Olkoon F(x) funktion f(x) integraalifunktio, ts. $F'(x) = f(x) $. Tällöin määrätty integraali voidaan laskea kaavalla        
# 
# 
#  $\int_{a}^{b}f(x)dx = F(b) - F(a)$        
#  
# Erotusta F(b)- F(a) on tapana merkitä laskuissa  $\overset{b}{\underset{a}{/}} F(x)$ , jolloin merkitään         
# 
# $\int_{a}^{b}f(x)dx = \overset{b}{\underset{a}{/}} F(x)$ 
# 
# ```

# ```{admonition} Esim. Laske $\int_{1}^{2} 2x dx$
# :class: dropdown
# Funktion 2x integraalifunktio F(x) = $\int 2x dx = x^2$     
# (*vakion C voi olettaa nollaksi, koska se häviää laskettaessa erotusta F(b)-F(a)*)      
# 
# $\int_{1}^{2} 2x dx = \overset{2}{\underset{1}{/}} x^2 =2^2 - 1^2 = 3 $
#  
# ```

# ```{admonition} Esim. Laske $\int_{0}^{4} e^x dx$
# :class: dropdown
# Funktion $e^x$ integraalifunktio F(x) = $\int e^x dx = e^x$        
# 
# $\int_{0}^{4} e^x dx = \overset{4}{\underset{0}{/}} e^x =e^4 - e^0 = e^4 - 1 \approx 53.6 $
#  
# ```

# ```{admonition} Esim. Laske $\int_{0}^{\frac {\pi}{2}} cos(x) dx$
# :class: dropdown
# Funktion cos(x) integraalifunktio F(x) = sin(x)         
# 
# $\int_{0}^{\frac {\pi}{2}} cos(x) dx = \overset{\frac {\pi}{2}}{\underset{0}{/}} sin(x) = sin(\frac {\pi}{2}) - sin(0) = 1 - 0 = 1 $
#  
# ```

# ## Määrätyn integraalin ominaisuuksia

# ```{admonition} **Määrätyn integraalin ominaisuuksia**
# :class: tip
# 
# $1.$ Integroimisrajat yhtä suuret   
# 
# $\int_{a}^{a}f(x)dx = 0$
# 
# $2.$ Integroimisrajojen vaihto muuttaa etumerkin         
# 
# $\int_{a}^{b}f(x)dx = - \int_{b}^{a}f(x)dx$
# 
# $3.$ Yhteenlaskuominaisuus      
# 
# $\int_{a}^{c}f(x)dx + \int_{c}^{b}f(x)dx  = \int_{a}^{b}f(x)dx$           
# 
# Ominaisuuden nojalla funktion määrätty integraali voidaan laskea myös paloittain. Pisteen c ei välttämättä tarvitse olla välillä $[a,b]$
# 
# ```

# ## Määrätty integraali laskimissa 

# Mm. lukioissa käytetyissä laskimissa on toiminto määrätyn integraalin laskemiseen.      
# 
# WolframAlphassa edellisten esimerkkien integroinnin suoritetaan seuraavilla komennoilla:       
# 
# $\color {red} {\text{integrate 2x from 1 to 2}}$       
# 
# $\color {red} {\text{integrate e^x from 0 to 4}}$    
# 
# $\color {red} {\text{integrate cos(x) from 0 to pi/2}}$
