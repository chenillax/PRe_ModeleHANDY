import numpy as np 
from scipy.optimize import fsolve


def complementarite(f,delta,k,theta,t0,tf,y0,n):
    """
        Schéma avec la loi de complémentarité
    """
    Y,T = [y0],[t0]
    h = (tf-t0)/n
    y = y0
    t = t0
    for k in range(n):
        y = fsolve(lambda x,delta : x-h*theta*(f(x,t,delta,k))-y-h*(1-theta)*f(y,t,delta,k),y,args=(delta))
        if y[1] <0 :
            y[1] = 0
        t = t+h
        Y.append(y)
        T.append(t)
    return  np.array(T),np.array(Y)
