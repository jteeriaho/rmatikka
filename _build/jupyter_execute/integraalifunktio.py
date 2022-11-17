#!/usr/bin/env python
# coding: utf-8

# # Integraalifunktio    

# **Integrointi** on derivoinnin käänteisoperaatio. Funktion f(x) integraalifunktio on mikä tahansa funktio F(x), jonka derivaatta on f(x). Integraalifunktio ei ole yksikäsitteinen, sillä jos F(x) on funktion f(x) integraalifunktio, niin myös F(x) + C, missä C on mielivaltainen vakio,  on f(x):n integraalifunktio,

# ```{admonition} **Integraalifunktion määritelmä**
# :class: tip
# Jos $F'(x) = f(x)$ eli f(x) on funktion F(x) derivaatta, niin funktiota F(x) sanotaan funktion f(x) **integraalifunktioksi**.      
# 
# Tällöin kaikki f(x):n integraalifunktiot ovat muotoa F(x) + C, missä C on mielivaltainen vakioa, jota sanotaan *integroimisvakioksi*.  Funktion f(x) integraalifunktion määrittämistä sanotaan integroinniksi.    
# 
# Merkintä:
# 
# $ \int f(x)dx=F(x) + C$
# 
# 
# *(lukuohje: "integraali f(x) dee ex = F(x) + C")*   
# 
# ```

# ```{admonition} Esim. Laske $ \int 2x dx$
# :class: dropdown
# $ \int 2x dx = x^2 + C$  
# 
# Perustelu: $D (x^2+ C) = 2x$
# ```

# ```{admonition} Esim. Laske $ \int cos(x) dx$
# :class: dropdown
# $ \int cos(x) dx = sin(x) + C$  
# 
# Perustelu: $D (sin(x)+ C) = cos(x)$
# ```

# ## Integroimiskaavat   

# Derivoimiskaavoista voidaan johtaa integroimiskaavoja.

# ```{admonition} Perusfunktioiden integroimiskaavoja
# :class: tip
# $ \int a dx = a x + C \hspace{40mm}\text{   vakiofunktion y = a integraali}$   
# 
# $ \int x^n dx = \frac {1}{n+1} x^{n+1} + C\hspace{27mm}\text{potenssifunktion }y = x^n\text{ integraali}$      
# 
# $ \int \frac {1}{x} dx = ln(x) + C $   
# 
# $ \int e^x dx = e^x + C $ 
# 
# $ \int cos(x) dx = sin(x) + C $  
# 
# $ \int sin(x) dx = cos(x) + C $ 
# ```

# Integrointi on derivoinnin tapaan **lineaarinen operaatio**, mikä tarkoittaa, että mm. polynomi integroidaan termi kerrallaan siten, että potenssien kertoimet voi siirtää integraalimerkin eteen.

# ```{admonition} Integrointi on lineaarinen operaatio
# :class: tip
# $ \int (a f(x) + b f(x)) dx = a \int f(x) dx +  b \int g(x) dx$   
# ```

# ```{admonition} Esim. Laske $ \int (2 x^2 - 5x + 7)dx$
# :class: dropdown
# Ratkaisu:  Integroidaan x:n potenssi käyttäen potenssin integroimissääntöä       
# 
# $ \int (2 \color{red}{x^2}\color{black}{ - 5}\color{red}{x}\color{black}{ + 7)dx = 2\color{red}{\frac {1}{3}x^3}\color{black}{ - 5}\color{red}{\frac {1}{2}x^2}\color{black}{ + 7}\color{red}{x}\color{black}{ + C}}$       
# $=\frac {2}{3}x^3 - \frac {5}{2}x^2 + 7x + C $
# 
# ```

# Potenssin integroimissääntöä voidaan soveltaa myös integroitaessa $\frac {1}{x^n} $ - tyypin funktioita, sekä juurilausekkeita, jotka voidaan esittää murtopotensseina

# ```{admonition} Esim. Laske $ \int \frac {1}{x^4} dx$
# :class: dropdown
# Ratkaisu:  Käytetään muunnosta $\frac {1}{x^n} = x^{-n}$      
# 
# $ \int \frac {1}{x^4}dx = \int x^{-4}dx = \frac {1}{-3} x^{-3} = -\frac {1}{3 x^3} + C $
# 
# ```

# ```{admonition} Esim. Laske $ \int \sqrt{x} dx$
# :class: dropdown
# Ratkaisu:  Esitetään juuri murtopotenssimuodossa $ x^{\frac {1}{2}}$      
# 
# $ \int \sqrt{x} dx  = \int x^{\frac {1}{2}}dx = \frac {1}{\frac {3}{2}} x^{\frac {3}{2}} = \frac {2}{3} x^{\frac {3}{2}} + C $
# 
# ```

# ```{admonition} Esim. Laske $ \int (2cos(x)-4 sin(x)+5e^x -3)dx$
# :class: dropdown
# Ratkaisu:  
# 
# $ \int (2cos(x)-4 sin(x)+5e^x -3)dx$     
# = $2 sin(x) + 4 cos(x) + 5e^x - 3x + C$
# 
# ```

# ## Yhdistettyjen funktioiden integrointi

# Yksinkertaisia yhdistettyjä funktioita ovat esimerkiksi tyyppiä g(ax+b) olevat funktiot, missä g(x) on jokin perusfunktio ja a x + b on lineaarinen sisäfunktio.     
# 
# Yhdistetyn funktion derivoimissäännöstä $D g(f(x)) = g'(f(x)) f'(x)$  voidaan käänteisesti johtaa integroimissääntöjä tavanomaisille integraaleille.  Seuraavassa muutamia kaavoja.  
# 

# ```{admonition} Perusfunktioiden integroimiskaavoja
# :class: tip
# $ \int cos(a x) dx = \frac {1}{a} sin(a x) + C $   
# 
# $ \int sin(a x) dx = -\frac {1}{a} cos(a x) + C $      
# 
# $ \int \frac {1}{a x + b} dx = \frac {1}{a} ln(a x+ b) + C $   
# 
# $ \int e^{ax} dx = \frac {1}{a}e^{ax} + C $ 
# 
# $ \int (a x + b)^n dx = \frac {1}{a} \frac {(a x + b)^{n+1}}{{n+1}} + C $  
# 
# ```

# ```{admonition} Esim. Laske $ \int 3 e^{-4x}dx$
# :class: dropdown
# Ratkaisu:  
# 
# $ \int 3 e^{-4x}dx = 3 \frac{1}{-4}e^{-4x} =-\frac{3}{4}e^{-4x} + C $  
# 
# ```

# ```{admonition} Esim. Laske $ \int 4 (2x+1)^5 dx$
# :class: dropdown
# Ratkaisu:  
# 
# $ \int 4 (2x+1)^5 dx = 4\cdot \frac{1}{2}\frac{1}{6}(2x+1)^6 =\frac{1}{3}(2x+1)^6 + C $  
# 
# ```

# ```{admonition} Esim. Laske $ \int 5 sin(3x) dx $
# :class: dropdown
# Ratkaisu:  
# 
# $ \int 5 sin(3x) dx = 5\cdot \frac{1}{-3}cos(3x)=-\frac{5}{3}cos(3x) + C $  
# 
# ```

# ## Integrointi laskimella

# Algebralaskimissa on integrointitoiminto.        
# 
# **WolframAlpha- laskimella** edellinen esimerkki voidaan laskea komennolla       
# 
# $\color{red}{\text{integrate 5 sin(3x)}} $  , joka antaa vastauksen muodossa $\color{blue}{-\frac {5}{3}cos(x)\text{ + costant}} $  
# 
