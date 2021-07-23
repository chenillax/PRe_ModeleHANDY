import numpy as np
import matplotlib.pyplot as plt
from theta_method import theta_method
from handy_art import betac,betae,xc0,chiM,lamba,y0,w0,rho,alpham,alphaM,gama,s
from handy_resc import handy_resc
from tqdm import tqdm, trange

"""
    Ce fichier a été servi pour faire l'analyse de sensibilité.
"""

def heavy(x):
    """
        La fonction d'Heaviside
    """
    if x>0 :
        return 1
    else :
        return 0

def plateau_rich(sol):
    """
        Détermine si on est sur le plateau pour la courbe de la richesse, lorsqu'on fait varier w_0
    """
    plat = []
    for ind, val in enumerate(sol):
        if val >= 249 and val <= 251:
            plat.append(ind)
    return (plat[-1] - plat[0])*20/10000

def plateau(sol):
    """
        Détermine si on est sur le plateau dans le cas où les variables sont normalisées.
    """
    plat = []
    for i in range(len(sol)):
        if sol[i] > 0.98 :
            plat.append(i)
    plat = np.array(plat)
    return (plat[-1] - plat[0])*20/10000

pas = 10000
def handy_resolu(xe0, k, delta,betac = betac, betae=betae,xc0 = xc0,w0 = 0):
    f0 = np.array([xc0,xe0,y0,w0])
    theta = 0.5
    def handy_resc_beta(X,t,delta,k):
        """
            Modèle HANDY remis à l'échelle avec paramètres apparents
        """
        xc,xe,y,w = X[0],X[1],X[2],X[3]
        xct = xc + (alphaM-alpham)/(betac-alpham)*(xc*w/(xe+xc)-xc)*heavy(xc+xe-w)
        xet = xe*(betae - alpham)/(betac - alpham) + (alphaM-alpham)/(betac-alpham)*(xe*k*w/(xe+xc)-xe)*heavy(xc+xe-k*w)
        yt = gama/(betac-alpham)*y*(100-y)-delta*y*xc
        wt = delta*y*xc-s/(rho*(betac-alpham))*(xc+xe)+s/(rho*(betac-alpham))*(xc+xe-w)*heavy(xe+xc-w)
        return np.array((xct,xet,yt,wt))
    
    temps,sol = theta_method(handy_resc_beta,delta,k,theta,0,20,f0,10000)
    communers= sol[ :, 0]
    elites = sol[ :, 1]
    nature = sol[:, 2]
    richesse = sol[:,3]
    communers_normalized = communers/max(communers)
    elites_normalized = elites/max(elites)
    nature_normalized = nature/max(nature)
    richesse_normalized = richesse/max(richesse)
    return temps, communers_normalized,  elites_normalized, nature_normalized, richesse_normalized, np.array([max(communers),max(elites),max(nature),max(richesse)])



xc0_resc = xc0*rho
k =10
sol = []
para =[]
maxi = []
plat = []
xerange = [1E-5,5E-5,1E-4,5E-4,1E-3,5E-3,1E-2,5E-2,1E-1,5E-1]
paraname = "w_0"
inter = " "
# Calcul Variation de paramètres
for i in trange(0,160,10):
    X = handy_resolu(5E-4,100,0.0667,betac =3E-2, betae =3E-2,xc0=xc0_resc,w0= i)
    para.append(i) #Mettre les transformations subis par i !
    maxi.append(X[-1])
    plat.append([plateau(X[1]),plateau(X[4])])
    sol.append(X)

print(len(maxi), len(para))
maxi = np.array(maxi[:])
plat = np.array(plat)
# Affichage de toutes les solutions sur le même graphique
for x in sol :
    plt.plot(x[0],x[1])
    plt.plot(x[0],x[2])
    plt.plot(x[0],x[3])
    plt.plot(x[0],x[4])
plt.show()

# Affichage de toutes les solutions sur des graphiques différents
i = 0 
j= 0
per, delt = [],[]
fig, ax = plt.subplots(4,4)
for x in (sol): 
    ax[j,i%4].plot(x[0],x[1])
    ax[j,i%4].plot(x[0],x[2])
    ax[j,i%4].plot(x[0],x[3])
    ax[j,i%4].plot(x[0],x[4])
    ax[j,i%4].set_xlabel("Temps")
    i +=1
    if i%4 == 0:
        j += 1
plt.suptitle("Solution pour " + paraname+"$\in" + inter+"$")
plt.show()

### Affichage des Maximums en fonction de la variation d'un paramètre
fig,ax = plt.subplots(2,2)
ax[0,0].scatter(para,maxi[:,0])
ax[0,0].set_title("Communers")
ax[0,1].scatter(para,maxi[:,1])
ax[0,1].set_title("Elites")
ax[1,0].scatter(para,maxi[:,2])
ax[1,0].set_title("Nature")
ax[1,1].scatter(para,maxi[:,3])
ax[1,1].set_title("Richesse")
plt.suptitle("Maximum en fonction de la variation de " + paraname)
plt.show()

# Affichage de la longueur du plateau des courbes des communers et de la richesse en fonction de la variation d'un paramètre.
fig,ax = plt.subplots(2)
ax[0].scatter(para,plat[:,0])
ax[0].set_title("Communers")
ax[1].scatter(para,plat[:,1])
ax[1].set_title("Richesse")
plt.suptitle("Longueur du plateau en fonciton  de la variation de " + paraname)
plt.show()