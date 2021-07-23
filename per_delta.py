from scipy.signal import argrelextrema
import numpy as np
import matplotlib.pyplot as plt
from theta_method import theta_method
from handy_resc import betac, betae,xc0,rho,alpham,y0,w0
from handy_resc_eg import handy_resc_eg
from tqdm import tqdm, trange
from scipy import stats
from complementarite import complementarite

"""
    Ce fichier calcule et affiche la période de la nature en fonction de delta
"""
duree = 60
pas = 100000

def handy_resolu(xe0, k, delta,betac = betac, betae=betae,xc0 = xc0):
    """
        Calcule de la solution du modèle HANDY avec ou sans la loi de complémentarité.
    """
    f0 = np.array([xc0,y0,w0])
    theta = 0.5
    # Calcul de la solution (avec ou non la loi de complémentarité)
    temps,sol = theta_method(handy_resc_eg,delta,k,theta,0,60,f0,100000)
    #temps,sol = complementarite(handy_resc_eg,delta,k,theta,0,duree,f0,pas)
    communers= sol[ :, 0]
    nature = sol[:, 1]
    richesse = sol[:,2]
    communers_normalized = communers/max(communers)
    #elites_normalized = elites/xen
    nature_normalized = nature/max(nature)
    richesse_normalized = richesse/max(richesse)  
    return temps, communers_normalized,  nature_normalized, richesse_normalized

delta_opt = 6.67E-6
delta_opt2 = 8.33E-6
delta_resc  = delta_opt/(rho*(betac-alpham))
xc0_resc = xc0*rho
sol = []


# Calcul de la solution pour différents delta
for i in (trange(11,19)):
    X = handy_resolu(0,0,i/10,xc0=xc0_resc)
    sol.append(X)

i = 0 
j= 0
per, delt = [],[]
fig, ax = plt.subplots(2,4)
for x in (sol): 
    (indice,) = argrelextrema(x[2], np.greater)
    if len(indice)>2 :
        print(np.array(indice)*duree/pas)
        if indice[2]-indice[1] > 500 :
            per.append((indice[1]-indice[0])*duree/pas)
            delt.append((i+11)/10)
        else : 
            per.append((indice[2]-indice[0])*duree/pas)
            delt.append((i+11)/10)
    elif len(indice)>1 :
        if indice[1]-indice[0] > 500 :
            per.append((indice[1]-indice[0])*duree/pas)
            delt.append((i+11)/10)
        else : 
            per.append((indice[2]-indice[0])*duree/pas)
            delt.append((i+11)/10)
    ax[j,i%4].plot(x[0],x[1])
    ax[j,i%4].plot(x[0],x[2])
    ax[j,i%4].plot(x[0],x[3])
    ax[j,i%4].set_xlabel("Temps")
    i +=1
    if i%4 == 0:
        j += 1
plt.suptitle("Solution pour $\delta \in [1.1,1.8]$")
plt.show()

# Régression linéaire
slope, intercept, r_value, p_value, std_err = stats.linregress(delt,per)
droite = np.array(delt)*slope + intercept
plt.scatter(delt, per)
plt.plot(delt, droite,label=f"Régression linéaire  \n Slope : {slope: .5f} \n Intercept : {intercept : .5f} \n r² : {r_value**2 :.5f} ")
plt.legend()
plt.xlabel(r"$\delta $")
plt.ylabel("Periode")
plt.title(r"Periode en fonction de $\delta$")
plt.show()

