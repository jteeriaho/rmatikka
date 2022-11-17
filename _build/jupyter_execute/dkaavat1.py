#!/usr/bin/env python
# coding: utf-8

# # Derivoimiskaavoja   

#        
# Derivaattafunktion määrittämisen eli **derivoinnin** perinteinen menetelmä on derivoimiskaavojen käyttäminen. Derivoimiskaavoja löytyy matematiikan taulukkokirjoista. Derivoimiskaavat on johdettu derivaatan raja-arvomääritelmää käyttäen. Osa kaavoista on ilmeisiä.    
# 
# Nykyisin derivaatan laskeminen on vielä helpompaa, koska se voidaan tehdä algebralaskimilla.    
# 

# ## Potenssifunktion derivaatta

# ```{admonition} **Vakiofunktion ja potenssifunktion derivaatta**
# :class: tip
# Seuraavissa kaavoissa käytetään derivaatasta merkintää Df(x)    
# 
# 1.  D(c) = 0                 (vakiofunktion f(x) = c derivaatta = 0)
# 
# 2.  $Dx^n = n x^{n-1}$     (potenssifunktion derivaatta)
# 
# 3.  D(x) = 1 
# 
# 4.  $D\frac {1}{x^n}$ =  $- \frac {n}{x^{n+1}}$  
# 
# ```

# Kaavojen perusteluja:
# 1. Vakiofunktion f(x) = c kuvaaja on vaakasuora viiva, jonka kulmakerroin = 0    
#        
# 
# 2. Jaollisuusopin kaavan mukaan derivaatan määritelmän mukainen erotusosamäärä sievenee muotoon       
# $f'(x_0)=\underset{x\to x_0}{lim}\frac{x^n-x_0^n}{x-x_0}= \underset{x\to x_0}{lim}(x^{n-1}+x^{n-2}x_0+x^{n-3}x_0^2+...+x_0^{n-1})$      
# $\hspace{36mm}= x_0^{n-1}+x_0^{n-1}x_0+... + x_0^{n-1} = nx_0^{n-1}$      
#          
# 
# 3. Suoran f(x) = x  kulmakerroin eli derivaatta on 1. Kaavan voi myös johtaa sijoittamalla n=1 kaavaan (2), jolloin saadaan $Dx^1 = 1\cdot x^0 = 1$     
#         
# 
# 4. Kaavaa (2) voidaan soveltaa myös, kun potenssi n on negatiivinen.  Tällöin $D\frac {1}{x^n} = Dx^{-n}=-n x^{-n-1} = -\frac {n}{x^{n+1}}$

# ````{admonition} Laske funktion $f(x) = x^5$ a) derivaattafunktio, b) tangentin kulmakerroin kohdassa x=2, c) tangentin kulmakerroin kohdassa x = -1.
# :class: dropdown
# a) $f'(x) = Dx^5 = 5 x^4$       
# b) $f'(2) = 5*2^4 = 80$       
# c) $f'(-1) = 5*(-1)^4 = 5$
# ````

# ````{admonition} Derivoi a) $x^{2015}$, b) $\frac {1}{x}$ c) $\frac {1}{x^5}$
# :class: dropdown
# a) $Dx^{2015} = 2015 x^{2014}$   
# 
# b) $D\frac {1}{x} = -\frac {1}{x^{1+1}}=-\frac {1}{x^2} $   
# 
# c) $D\frac {1}{x^5} = -\frac {5}{x^{5+1}}=-\frac {5}{x^6} $
# ````

# ## Juurilausekkeiden derivointi

# ```{admonition} **Potenssin derivoimiskaavan sovellus murtopotensseihin**
# :class: tip
# 
# Juurilausekkeet voidaan esittää myös potenssimuodossa käyttäen murtopotensseja:      
# $\sqrt{x}=x^{\frac {1}{2}}$ , $\sqrt[3]{x} =x^\frac{1}{3}$, $\frac{1}{\sqrt{x}}=x^{-\frac{1}{2}}$     
# 
# Juurilausekkeiden derivaatat voidaan laskea potenssin derivoimissäännöllä. Esim.      
# 
# $D\sqrt{x}= Dx^{\frac {1}{2}}=\frac {1}{2}x^{-\frac {1}{2}}= \frac{1}{2\sqrt{x}}$    
# 
# $D\sqrt[3]{x}= Dx^{\frac {1}{3}}=\frac {1}{3}x^{-\frac {2}{3}}= \frac{1}{3\sqrt[3]{x^2}}$
# 

# ## Polynomin derivointi   

# Polynomien derivointiin tarvitaan potenssifunktion derivoimissäännön lisäksi kaksi muuta sääntöä, joiden mukaan derivointi on lineaarinen operaatio: ts. vakion voi siirtää derivaattaoperaattorin eteen ja summafunktion derivaatta on sen termien derivaattojen summa.     

# ```{admonition} **Derivointioperaation lineaarisuussäännöt**
# :class: tip    
# 
# 1)   $D(a f(x)) = a Df(x)$ 
# 
# 2)  $D(f(x)+g(x)) = Df(x) + Dg(x)$     
# 
# ```

# ```{admonition} Derivoi $-3x^3 + 5x^2 - 4x + 7$
# :class: dropdown
# $D(-3x^3 + 5x^2 - 4x + 7) =-3\cdot 3x^2+5\cdot 2x - 4\cdot 1+ 0 =-9 x^2+ 10 x -4 $      
# 
# ```

# ```{admonition} Derivoi $5x^2 + \frac {2}{x^2} - 5\sqrt{x} + 3$
# :class: dropdown
# $D(5x^2 + \frac {2}{x^2} - 5\sqrt{x} + 3) =10x - \frac {2\cdot 2}{x^3}-5\frac {1}{2\sqrt{x}}=10x-\frac {4}{x^3}-\frac {5}{2\sqrt{x}}$      
# 
# ```

# ## Erikoisfunktioiden derivoimiskaavoja

# ```{admonition} **Tavallisimpien erikoisfunktioiden derivoimiskaavoja**
# :class: tip    
# 
# 1)  $D\hspace{2mm} sin(x) = cos(x)$ 
# 
# 2)  $D\hspace{2mm} cos(x) = - sin(x)$
# 
# 3)  $D\hspace{2mm} tan(x) = \frac {1}{cos(x)^2}$
# 
# 4)  $D\hspace{2mm} e^x = e^x$
# 
# 5)  $D\hspace{2mm} ln(x) = \frac {1}{x}$
# ```

# ```{admonition} Derivoi $5 sin(x) - 2 cos(x) - 3 ln(x) + 4 e^x$
# :class: dropdown
# $D(5 sin(x) - 2 cos(x) - 3 ln(x) + 4 e^x)$ =      
# 
# $5 cos(x) + 2 sin(x) - \frac {3}{x} + 4 e^x$
# 
# ```

# ## Derivointi WolframAlpha laskimella

# esim. WoframAlpha-komento  $\color {red} {D(-3x^3 + 5x^2 - 4x + 7)}$    
# 
# antaa vastaukseksi $\color {blue} {-9x^2+10x-4}$      
# 

# ## Tulon ja osamäärän derivoimiskaavat

# Perusfunktioista voidaan lineaariyhdistelmien lisäksi muodostaa monimutkaisempia funktioita kerto- ja jakolaskun avulla. Näiden funktioiden derivoinnissa tarvitaan **tulon ja osamäärän derivoimiskaavoja**.  

# ```{admonition} **Tulon derivoimiskaava**
# :class: tip    
# 
# $D\hspace{2mm}(f(x)\cdot g(x)) = f'(x)\cdot g(x) + f(x)\cdot g'(x)$  
# 
# Tulon derivaatta on summalauseke, jossa on derivoitu yhtä tekijää kerrallaan muiden pysyessä ennallaan.    
# Periaate on sama kun tulossa on enemmän kuin kaksi funktiota.
# ```

# ```{admonition} Derivoi $x^2\cdot sin(x)$
# :class: dropdown
# Kaavan merkinnöillä $f(x)=x^2$ ja $g(x)=sin(x)$     
# ja niiden derivaatat $f'(x) = 2x$ ja $g'(x) = cos(x)$    
# 
# Sijoitus kaavaan $D\hspace{2mm}(f(x)\cdot g(x)) = f'(x)\cdot g(x) + f(x)\cdot g'(x)$ antaa    
# 
# 
# D $(x^2sin(x)) = 2x\cdot sin(x)+ x^2\cdot cos(x)$     
# 
# ```

# ```{admonition} Derivoi $(2x+1)\cdot ln(x)\cdot e^x$
# :class: dropdown
# Nyt tulossa on kolme tekijää $f(x)=2x+1$, $g(x)=ln(x)$ ja $h(x)=e^x$, joiden derivaatat ovat $f'(x) = 2$ , $g'(x) = \frac {1}{x}$ ja $h'(x) = e^x$    
# 
# Tulon derivoimissäännön periaatteen mukaan saadaan kolme termiä, joissa yksi tulon $f\cdot g\cdot h$ tekijä kerrallaan on derivoitu.     
# 
# 
# D $(2x+1)\cdot ln(x)\cdot e^x = 2\cdot ln(x)\cdot e^x + (2x+1)\cdot \frac {1}{x}\cdot e^x+(2x+1)\cdot ln(x)\cdot e^x$   
# 
# ```

# ```{admonition} **Osamäärän derivoimiskaava**
# :class: tip    
# 
# $\frac {f(x)}{g(x)} = \frac {f'(x)\cdot g(x) - f(x)\cdot g'(x)}{g(x)^2}$  
# 
#  
# ```

# ```{admonition} Derivoi $\frac {sin(x)}{x}$
# :class: dropdown
# Osoittajan $f(x)=sin(x)$, nimittäjän $g(x)=x$ lisäksi tarvitaan derivaatat $f'(x) = cos(x)$ ja $g'(x) = 1$    
# 
# Sijoittamalla nämä osamäärän derivoimiskaavaan, saadaan      
# 
# 
# D $\frac {sin(x)}{x} = \frac {cos(x)\cdot x-sin(x)\cdot 1}{x^2} = \frac {x\cdot cos(x)-sin(x)}{x^2}$   
# 
# ```

# ```{admonition} Derivoi $\frac {2x}{5x+1}$
# :class: dropdown
# Osoittajan $f(x)=2x$, nimittäjän $g(x)=5x+1$ lisäksi tarvitaan derivaatat $f'(x) = 2$ ja $g'(x) = 5$    
# 
# Sijoittamalla nämä osamäärän derivoimiskaavaan, saadaan      
# 
# 
# D $\frac {2x}{5x+1} = \frac {2\cdot (5x+1)-2x\cdot 5}{(5x+1)^2} = \frac {10x+2-10x}{(5x+1)^2}=\frac {2}{(5x+1)^2}$   
# 
# ```

# ## Yhdistetyn funktion derivaatta

# Perusfunktioista voidaan muodostaa monimutkaisempia funktiota myös asettamalla niitä sisäkkäin. Niistä käytetään nimitystä **yhdistetyt funktiot**.  
# 
# Esimerkiksi funktio y = cos(4x+1) on muodostettu kosinifunktiosta, jonka sisällä on polynomi 4x+1. 
# Funktiota y = cos(x) kutsutaan **ulkofunktioksi** ja funktiota y = 4x+1 **sisäfunktioksi**     
# 
# 
# Funktion $e^{-2x^2}$ ulkofunktio on y = $e^x$ ja sisäfunktio $-2x^2$      
# 
# Funktion $(3x+1)^4$ ulkofunktio on y = $x^4$  ja sisäfunktio y = 3 x + 1 
# 

# ```{admonition} **Yhdistetyn funktion derivaatta**
# :class: tip    
# 
# $D\hspace{2mm} g(f(x)) = g'(f(x))\cdot f'(x)$  
# 
# Kaavaa kutsutaan usein **ketjusäännöksi**, mikä viittaa siihen, että yhdistetyn funktion derivaatta on ulkofunktion derivaatan ja sisäfunktion derivaatan tulo.  Mikäli yhdistetty funktio koostuu useammasta kuin kahdesta sisäkkäisestä funktiosta, jokainen ketjussa oleva funktio derivoidaan.
# ```

# ```{admonition} Derivoi a) $cos(4x+1)$  b) $e^{-2x^2}$  c) $(3x+1)^4$
# :class: dropdown
# a) Ulkofunktio g(x)= cos(x) ja sisäfunktio f(x) = 4x+1.     
# Derivaatat g'(x)=-sin(x) ja f'(x) = 4 =>     
# D $cos(4x+1) = g'(f(x))\cdot f'(x) = -sin(4x+1)\cdot 4 = -4 sin(4x+1)$       
# 
# b) Ulkofunktio $g(x)= e^x$ ja sisäfunktio $f(x) = -2x^2$.      
# Derivaatat $g'(x)=e^x$ ja $f'(x) = -4x$ =>     
# D $e^{-2x^2} = g'(f(x))\cdot f'(x) = e^{-2x^2}\cdot (-4x) = -4x e^{-2x^2}$        
# 
# c) Ulkofunktio $g(x)= x^4$ ja sisäfunktio f(x) = 3x+1.       
# Derivaatat $g'(x)=4 x^3$ ja f'(x) = 3 =>     
# D $(3x+1)^4 = g'(f(x))\cdot f'(x) = 4(3x+1)^3\cdot 3 = 12 (3x+1)^3$ 
# 
# 
# ```

# Yhdistetyn funktion derivoimiskaavan käyttöä helpottaa, kun kaava puretaan useaksi kaavaksi tavallisille ulkofunktoille.

# ```{admonition} **Yhdistetyn funktion derivointikaavoja eri ulkofunktioille**
# :class: tip    
# 
# 1) $D\hspace{2mm} sin(f(x)) = cos(x)\cdot f'(x)$       
# 2) $D\hspace{2mm} cos(f(x)) =-sin(x)\cdot f'(x)$     
# 3) $D\hspace{2mm} e^{f(x)}  = e^{f(x)}\cdot f'(x)$       
# 4) $D\hspace{2mm} ln(f(x))  = \frac {f'(x)}{f(x)}$        
# 5) $D\hspace{2mm} {f(x)}^n  = n {f(x)}^{n-1}\cdot f'(x)$       
# 6) $D\hspace{2mm} \sqrt{f(x)} = \frac {f'(x)}{2\sqrt{f(x)}}$ 
# 
# ```

# Esimerkkejä:

# ```{admonition} Laske  D $sin(5x)$  
# :class: dropdown
# D $sin(5x)$ =$cos(5x)\cdot 5 = 5\hspace{1mm}cos(5x)$ 
# ```

# ```{admonition} Laske  D $(4x+7)^3$  
# :class: dropdown
# D $(4x+7)^3$=$3(4x+7)^2\cdot 4 = 12\hspace{1mm}(4x+7)^2$ 
# ```

# ```{admonition} Laske  D $cos(2x^2)$  
# :class: dropdown
# D $cos(2x^2)$ = $-sin(2x^2)\cdot 4x = -4x\hspace{1mm}sin(2x^2)$ 
# ```

# ```{admonition} Laske  D $ln(2x+3)$  
# :class: dropdown
# D $ln(2x+3)$ = $\frac {2}{2x+3} $ 
# ```

# ```{admonition} Laske  D$\sqrt{x^2+5}$  
# :class: dropdown
# D$\sqrt{x^2+5}$ =  $\frac {1}{2\sqrt{x^2+5}}\cdot 2x =\frac {x}{\sqrt{x^2+5}}$  
# ```
