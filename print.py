import numpy as np
import matplotlib.pyplot as plt
from theta_method import theta_method
from handy_art import handy_art, betac,betae,xc0,chiM,lamba,y0,w0,rho,alpham
from handy_resc import handy_resc,chiM_resc


def print_handy(titre,xe0, k, delta,betac = betac, betae=betae,xc0 = xc0,y0 = y0, w0= w0):
    """ 
        Fonction qui affiche le modèle HANDY 
        titre : est le titre du graphique 
        xe0, xc0, y0,w0 = conditions initiales
        delta,k,betac,betae = constante du modèle HANDY 
    """
    f0 = np.array([xc0,xe0,y0,w0])
    theta = 0.5
    #Pour le modèle de l'article
    #temps,sol = theta_method(handy_art,delta,k,theta,0,10000,f0,100000)
    #Pour le modèle remis à l'échelle
    temps,sol = theta_method(handy_resc,delta,k,theta,0,20,f0,10000)
    communers= sol[ :, 0]
    elites = sol[ :, 1]
    nature = sol[:, 2]
    richesse = sol[:,3]
    communers_normalized = communers/max(communers)
    elites_normalized = elites/max(elites)
    nature_normalized = nature/max(nature)
    richesse_normalized = richesse/max(richesse)

    # Evolution des populations 
    plt.plot(temps,communers_normalized,label="communers")
    plt.plot(temps,elites_normalized,label="elites")
    plt.plot(temps,nature_normalized,label="nature")
    plt.plot(temps,richesse_normalized,label="richesse")
    plt.xlabel("Unité de temps")
    plt.legend()
    plt.title(titre)
    plt.show()
   
    return temps, communers_normalized, nature_normalized, richesse_normalized
    
delta_opt = 6.67E-6
delta_opt2 = 8.33E-6
delta_resc  = delta_opt/(rho*(betac-alpham))
delta_resc2 = delta_opt2/(rho*(betac-alpham))
xc0_resc = xc0*rho
xe0 = 0
k = 0
xe0_resc = 0


print_handy("Egalitarian - Soft Landing to Optimal Eq", xe0_resc,k,delta_resc,xc0=xc0_resc)


