import numpy as np
import matplotlib.pyplot as plt

"""
    Ce fichier permet de reproduire les graphiques de l'évolution du taux de mort des 2 types de populations et de leur taux de consomation, de l'article HANDY. (Figure 2)
"""
#CONSTANTES
alpham = 1E-2
alphaM = 7E-2 
betac = 3E-2
betae = 3E-2
gama = 1E-2
k = 10
lamba = 100
rho = 5E-3
s = 5E-4
xc = 100
xe = 10
wth = rho*xc + rho*xe*k


#FONCTIONS
def cc(w): 
    """
        Taux de consommation des commoners
    """
    return min(1, w)*s*xc

def ce(w):
    """
        Taux de consommation des élites
    """
    return min(1,w)*k*s*xe

def alphac(w):
    """
        Taux de mortalité des commoners
    """
    return alpham + max(0,1-min(1,w))*(alphaM-alpham)

def alphae(w):
    """
        Taux de mortalité des élites
    """
    return alpham + max(0,1-min(1,w)*k)*(alphaM-alpham)


w_range = np.arange(0,3,0.1)
w_range = w_range/wth
CC = np.array([cc(w) for w in w_range])
CE = np.array([ce(w) for w in w_range])
w_range_a = np.arange(0,2,0.1)
w_range_a = w_range_a/wth
AC = np.array([alphac(w) for w in w_range_a])
AE = np.array([alphae(w) for w in w_range_a])
CC = CC/(s*xc)
CE = CE/ (s*xe)

# AFFICHAGE DES FONCTIONS
plt.plot(w_range, CC, label=r"$\frac{C_c}{sx_c}$")
plt.plot(w_range, CE,label=r"$\frac{C_e}{sx_e}$")
plt.xlabel(r"$\frac{w}{w_{th}}$")
plt.ylabel(r"$\frac{C}{sx}$")
plt.title("Consommation de la population en fonction de la richesse")
plt.legend()
plt.show()
plt.plot(w_range_a, AC, label=r"$\alpha_c$")
plt.plot(w_range_a, AE,"--",label=r"$\alpha_e$",)
plt.xlabel(r"$\frac{w}{w_{th}}$")
plt.ylabel(r"$\alpha$")
plt.title("Taux de mortalité de la population en fonction de la richesse")
plt.legend()
plt.show()