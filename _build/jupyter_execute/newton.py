#!/usr/bin/env python
# coding: utf-8

# # Newtonin menetelmä   

# **Newtonin menetelmä**  on differentiaalilaskentaan perustuva tehokas algoritmi funktion nollakohtien likiarvojen etsimisessä.  
# 
# Nollakohdan etsiminen aloitetaan asettamalla nollakohdalle **alkuarvaus $x_0$** iteraation lähtökohdaksi.    
# 
# 1. Seuraavaksi muodostetaan funktion **tangentin yhtälö** pisteeseen $(x_0, f(x_0)$ käyttäen kulmakertoimena derivattaa $f'(x_0)$.       
# 
# 
# > Tangentin yhtälö on:    $y - f(x_0) = f'(x_0)\cdot (x-x_0)$   
# 
# 
# 3. Lasketaan tangentin ja x-akselin leikkauskohta $x_1$ sijoittamalla yhtälöön y = 0, jolloin saadaan  $x_1=x_0-\frac{f(x_0)}{f'(x_0)}$ 
# 
#             
# 4. Tämän jälkeen asetetaan $x_1$ uudeksi alkuarvaukseksi ja jatketaan samaan tapaan, kunnes lukujonon $x_0, x_1, x_2, ...$ arvot vakiintuvat tiettyyn arvoon. Lukujonon raja-arvo on yhtälön f(x) = 0 juuren likiarvo.

# Kuva näyttää, miten käyrän tangentti johtaa iteraatioaskeleessa lähemmäs juurta.
# ![iter](images/kuva26.PNG)

# ```{admonition} **Newtonin menetelmä yhtälön f(x) = 0 juuren likiarvon laskemiksi**
# :class: tip
# 1. Annetaan alkuarvaus $x_0$ iteraation lähtökohdaksi     
# 
# 2. Lasketaan kaavalla $x_{n+1} = x_n -\frac {f(x_n)}{f'(x_n)}$ lukujonon $x_0, x_1, ...$ arvoja.
# 
# Useimmiten 4 - 5 arvon jälkeen lukujonon viimeisimmät arvot eivät enää juurikaan poikkea toisistaan. Lukujono lähestyy yhtälön f(x) = 0  juuren arvoa. 
# 
# Jos yhtälöllä f(x) = 0 on useita juuria, eri alkuarvot $x_0$ johtavat eri juuriin. On siis tarpeen suorittaa iteraatio useilla alkuarvoilla. 
# 
# ```

# ```{admonition} Esim. Määritä yhtälön  $x^3 + 3 x - 1 = 0$ juuri 2 desimaalin tarkkuudella. 
# :class: dropdown       
# Asetetaan alkuarvaukseksi x = 1     
# Iteraatiokaava on esimerkin tapauksessa $x_{n+1} = x_n -\frac {{x_n}^3 + 3x_n -1}{3 {x_n}^2+3}$.  
# 
# Lasketaan kaavaa käyttäen jonon pisteitä. WolframAlphalla tämä käy nopeasti, koska samaan lausekkeen voi evaluoida uudella muuttujan arvolla vaihtamalla where sanan jälkeistä arvoa.   
# 
# $\begin{matrix}
# x_n&\text{WolframAlpha komento}&x_{n+1}\\
# 1.0 &\text{x - (x^3+3x-1)/(x^3+3) where x=1.0} & 0.5 \\
# 0.5 &\text{x - (x^3+3x-1)/(x^3+3) where x=0.5} & 0.333 \\
# 0.333&\text{x - (x^3+3x-1)/(x^3+3) where x=0.333} & 0.322 \\
# 0.322&\text{x - (x^3+3x-1)/(x^3+3) where x=0.322} & 0.322
# \end{matrix}$                  
# 
# Lukujonon arvota näyttävän nopeasti suppenevan kohti arvoa 0.322, joka on juuren likiarvo.  
# 
# Vastaus: Juuri on n. 0.32
# 
# ```

# ````{admonition} Esim. Määritä yhtälön  $e^x - x - 3 = 0$ juuret (2 juurta) 1 desimaalin tarkkuudella. 
# :class: dropdown
# Vastaus: -2.9 ja 1.5
# ```{admonition} Ratkaisu
# :class: dropdown
# Iteraatiokaava on nyt $x_{n+1} = x_n -\frac {e^{x_n} - x_n - 3}{e^{x_n}-1}$.  
# 
# Lasketaan kaavaa käyttäen jonon pisteitä.      
# 
# Iteraatio alkuarvauksella 2 johtaa juureen 1.51
# 
# $\begin{matrix}
# x_n&\text{WolframAlpha komento}&x_{n+1}\\
# 2 &\text{(x-e^x-x-3)/(e^x-1) where x=2}  & 1.61 \\
# 1.63 &\text{(x-e^x-x-3)/(e^x-1) where x=1.63}  & 1.51 \\
# 1.51 &\text{(x-e^x-x-3)/(e^x-1) where x=1.51}  & 1.51
# \end{matrix}$
# 
# 
# Iteraatio alkuarvauksella -2 johtaa juureen -2.95
# 
# $\begin{matrix}
# x_n&\text{WolframAlpha komento}&x_{n+1}\\
# -2 &\text{(x-e^x-x-3)/(e^x-1) where x=-2}  & -3 \\
# -3 &\text{(x-e^x-x-3)/(e^x-1) where x=-3}  & -2.95 \\
# -2.95 &\text{(x-e^x-x-3)/(e^x-1) where x=-2.95}  & -2.95
# \end{matrix}$
# ```
# ````
