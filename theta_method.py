import numpy as np 
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


def theta_method(f,delta,k,theta,t0,tf,y0,n):
    """
        Fonction du schéma de la théta-méthode qui résout la fonction f. 
        delta, k sont les arguments de la fonction f 
        theta est un paramètre du schéma 
        t0,tf et n permettent de définir le pas 
        y0 est la condition initiale de f
    """
    Y,T = [y0],[t0]
    h = (tf-t0)/n
    y = y0
    t = t0
    for k in range(n):
        y = fsolve(lambda x,delta : x-h*theta*(f(x,t,delta,k))-y-h*(1-theta)*f(y,t,delta,k),y,args=(delta))
        t = t+h
        Y.append(y)
        T.append(t)
    return  np.array(T),np.array(Y)
