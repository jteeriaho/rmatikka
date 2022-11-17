#!/usr/bin/env python
# coding: utf-8

# # Derivaatta   

# Differentiaalilaskennan keskeinen käsite on **derivaatta**, joka kuvaa funktion muutosnopeutta annetussa pisteessä.    
# Derivaatta voidaan määritellä algebrallisesti raja-arvona.    
# Seuraavassa kuitenkin määritellään derivaatta sen geometrisen tulkinnan kautta.     
# 

# ```{admonition} **Derivaatan geometrinen tulkinta**
# :class: tip
# Funktion f(x) derivaatta kohdassa $x_0$ on sen kuvaajan tangentin kulmakerroin ko. kohdassa. Sitä merkitään $f'(x_0)$
# 
# ![deri1](images/kuva1.PNG)
# ```

# 
# ## Funktion derivaatan laskeminen annetussa pisteessä

# ```{admonition} Määritä käyrän $y =f(x) = x^2 -1$ tangentin kulmakerroin kohdassa x = 2
# :class: tip
# Tarkastellaan pisteen (2,3) ja sen lähellä olevan pisteen $(2+h, (2+h)^2-1)$ kautta kulkevan sekantin kulmakerrointa     
# 
# $k=\frac{y_2-y_1}{x_2-x_1}=\frac{(2+h)^2-1-3}{h}=\frac{(2+h)^2-4}{h}$      
# 
# ![dergraf](images/kuva2.PNG)
# 
# Kun x-koordinaattien erotus h lähestyy arvoa 0, saadaan kulmakertoimen raja-arvona tangentin kulmakerroin 
# 
# $f'(2) = \underset{h\to 0}{lim}\frac{(2+h)^2-4}{h}=\underset{h\to 0}{lim}\hspace{2mm}(h+4)=0+4=4$
# 
# ```

# > Em. raja-arvo voidaan laskea paitsi laskimella, myös sieventämällä osoittajaa:     
# >
# >    $(2+h)^2 - 4 = (2+h)(2+h)- 4 = 4 + 2h + 2h + h^2 - 4 = h^2 + 4h$  =>  
# >   
# >  $\frac{(2+h)^2-4}{h}= \frac{h^2+4h}{h}= \frac{h(h+4)}{h}=h+4$  , joka lähestyy arvoa 4, kun h-> 0

# ## Käyrän derivaatan numeerinen määrittäminen (x,y) - datasta 

# Mm. fysiikassa tarvitaan menetelmää, jolla voidaan määrittää käyrän y = f(x) derivaatta annetussa kohdassa perustuen (x,y) dataan tarkasteltavan kohdan ympäristössä.  Seuraavassa sovelletaan tätä menetelmää edelliseen esimerkkiin. 

# ```{admonition} Määritä käyrän $y =f(x) = x^2 -1$ tangentin kulmakerroin kohdassa x = 2 perustuen ao. taulukkoon funktion arvoista tarkastelukohdan ympäristössä.     
# :class: tip
# | x   | f(x)  |
# |-----|-------|
# | 1.8 | 2.24  |
# | 1.9 | 2.61  |
# | 2.0 | 3.00  |
# | 2.1 | 3.41  |
# | 2.2 | 3.84  |
#      
# 
# Menetelmä perustuu siihen, että säännöllisellä käyrällä tarkastelupisteen tangentin arvo on yleensä likimain sama kuin tarkastelupisteen molemmilta puolilta valittujen lähimpien pisteiden välisen sekantin kulmakerroin. Ts.
# 
# $f'(2)\approx \frac{f(2.1)-f(1.9)}{2.1-1.9}=\frac{3.41-2.61}{0.2}=4.0$
# 
# ```

# ##  Derivaattafunktio

# Derivaatan laskeminen kullekin käyrän pisteelle erikseen vaikkapa edellä esitetyllä raja-arvomenettelyllä on hankalaa.  Se ei ole edes tarpeellista, jos löydetään käyrälle ns. **derivaattafunktio** eli lauseke, josta voidaan laskea käyrän tai funktion derivaatta missä tahansa kohdassa x.

# ```{admonition} Määritä käyrän $y = x^2 - 1$  derivaattafunktio 
# :class: tip
# Tarkastellaan käyrän mielivaltaisen pisteen $(x,x^2-1)$ ja viereisen pisteen $(x+h,(x+h)^2-1)$ välisen sekantin kulmakerrointa     
# 
#    $k=\frac{y_2-y_1}{x_2-x_1}=\frac{(x+h)^2-1-(x^2-1)}{h}=\frac{(x+h)^2-x^2}{h}$    
# 
# ![der3](images/kuva3.PNG)
#    
# Derivaatta kohdassa x saadaan kulmakertoimen raja-arvona kun h lähestyy 0:aa  
# 
# $f'(x)=\underset{h\to 0}{lim}\frac{(x+h)^2-x^2}{h}=\underset{h\to 0}{lim}\hspace{2mm}(h+2x)=0+2x=2x$     
# 
# Tulos: funktion $f(x)=x^2-1 $   derivaattafunktio $f'(x) = 2x$

# Em. raja-arvo voidaan laskea ilman laskinta sieventämällä osoittajaa:     
# 
#    $(x+h)^2 - x^2 = (x+h)(x+h)- x^2 = x^2 + 2xh + 2xh + h^2 - x^2 = h^2 + 2xh$  =>  
#    
#  $\frac{(x+h)^2-x^2}{h}= \frac{h^2+2xh}{h}=\frac{h(h+2x)}{h}= h+2 x$ , joka lähestyy arvoa 2x, kun h-> 0

# ## Derivaatan algebrallinen määritelmä

# Merkitsemällä tarkastelupistettä, jossa derivaatta lasketaan $(x_0,f(x_0))$ ja viereistä pistettä
# $(x_0+h,f(x_0+h))$ = $(x,f(x)$, voidaan derivaatta laskea raja-arvona $f'(x_0)=\underset{h\to 0}{lim}\frac{f(x_0+h)-f(x_0)}{h}$ tai yhtäpitävästi raja-arvona
# $f'(x_0)=\underset{x\to x_0}{lim}\frac{f(x)-f(x_0)}{x-x_0}$      
# 
# Sekantin kulmakertoimen lauseketta $\frac{f(x)-f(x_0)}{x-x_0}$ kutsutaan **erotusosamääräksi**

# ```{admonition} **Derivaatan algebrallinen määritelmä**
# :class: tip
# Funktion f(x) derivaatta kohdassa $x_0$ on erotusosamäärän raja-arvo     
# 
# $f'(x_0)=\underset{x\to x_0}{lim}\frac{f(x)-f(x_0)}{x-x_0}$
#      
#  
# ```

# ## Derivaatan merkintätapoja

# Funktion y = f(x) derivaattaa voidaan merkitä useilla tavoilla.
# 
# 1.   $f'(x)$     
# 
# 
# 2.    $y'$     
# 
# 
# 3.    Df(x)  
# 
# 
# 4.    $\frac{dy}{dx}$      
# 
# 
# 5.    $\frac{df(x)}{dx}$       
# 
