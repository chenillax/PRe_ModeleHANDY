import numpy as np 
import matplotlib.pyplot as plt
from math import log,sqrt
from handy_resc import handy_resc,  delta_resc, xc0_resc
from euler import euler
from scipy import stats
from theta_method import theta_method


def erreur(delta,k,normes,f0):
    """
        Affiche l'erreur de convergence en fonction du pas.
        delta, k sont les arguments du modèle 
        normes est la normes utilisé 
        f0 la condition initiale
    """
    EXC,EXE,EY,EW,H = [],[],[],[],[]
    precision = 20
    theta = 0
    titre = {0:"Euler Explicite",1/2:"Theta Method 1/2", 1:"Euler Implicite"}
    normename ={0:"Norme infinie", 1:"Norme 2 "}
    temps_ref,sol_ref = theta_method(handy_resc,delta,k,theta,0,20,f0,1000000) # La solution de référence
    sol_ref_precise = [sol_ref[1000000//precision *i] for i in range(precision)]
    for k in range(2000,10000,1000):
        temps,sol = theta_method(handy_resc,delta,k,theta,0,20,f0,k)
        sol_precise = [sol[k//precision*i] for i in range(precision)]
        EXC.append(normes(np.array(sol_ref_precise)-np.array(sol_precise),0))
        EXE.append(normes(np.array(sol_ref_precise)-np.array(sol_precise),1))
        EY.append(normes(np.array(sol_ref_precise)-np.array(sol_precise),2))
        EW.append(normes(np.array(sol_ref_precise)-np.array(sol_precise),3))
        H.append(log(5/k,10))
    #Regression Linéaire
    slope, intercept, r_value, p_value, std_err = stats.linregress(H,EXC)
    print("Xc est de pente : ", slope, "et de coefficient de correlation ", r_value**2)
    #Affichage
    fig, ax = plt.subplots(2,2)
    ax[0,0].scatter(H,EXC,label="Erreur sur xc ")
    ax[0,0].legend()
    ax[0,1].scatter(H,EXE,label="Erreur sur xe")
    ax[0,1].legend()
    ax[1,0].scatter(H,EY,label="Erreur sur y")
    ax[1,0].legend()
    ax[1,1].scatter(H,EW, label= "Erreur sur w")
    ax[1,1].legend()
    fig.suptitle(titre[theta]+normename[1])
    plt.show()


def norme_inf(X,j):
    return np.max(abs(X[:,j]))

def norme(X,j):
    S = 0 
    for i in range(len(X)):
        S += X[i,j]**2
    return sqrt(S)

erreur(5.5*delta_resc,0,norme,[xc0_resc,0,100,0])