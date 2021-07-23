import numpy as np 
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from handy_resc_eg import handy_resc_eg
from handy_resc import handy_resc
from theta_method import theta_method 

# VARIABLES GLOBALES
f = handy_resc_eg
delta = 0.33
k = 0
theta = 0.5
t0 = 0
tf = 60
duree = tf-t0
y0 = np.array([0.5,100,0])
n = 10000
#Points d'équilibre
x_e = 5/delta*(10 - 1/(3*delta))
y_e = 10/(3*delta)
w_e = 10/(3*delta)*(10 - 1/(3*delta))

# FONCTIONS
def moins_prod(tmp,new):
    """
        Fonction qui permet de changer le taux de production delta à new à l'indice tmp.
    """
    Y,T = [y0],[t0]
    h = (tf-t0)/n
    y = y0
    t = t0
    delta = 0.29
    for k in range(n):
        y = fsolve(lambda x,delta : x-h*theta*(f(x,t,delta,k))-y-h*(1-theta)*f(y,t,delta,k),y,args=(delta))
        t = t+h
        if k == tmp:
            delta = new
        Y.append(y)
        T.append(t)
    return  np.array(T),np.array(Y)

def impulsion_temps(var,timp,zer,pour= False):
    """ 
        Si pour == False : rajoute la quantité zer à la variable var au temps timp
        Sinon : rajoute diminue la varibale var du pourcentage zer au temps timp
    """
    Y,T = [y0],[t0]
    h = (tf-t0)/n
    y = y0
    t = t0
    ind = timp
    q = -1
    if var == "x" :
        vari = 0
    elif var == "y":
        vari = 1
    else :
        vari = 2 
    for k in range(n):
        y = fsolve(lambda x,delta : x-h*theta*(f(x,t,delta,k))-y-h*(1-theta)*f(y,t,delta,k),y,args=(delta))
        t = t+h
        if k == ind:
            if pour :
                q = y[vari]*zer
                y[vari] -= q
            else :
                y[vari] += zer
        #Reinjecte dans la richesse la 9.9% de la quantité q 
        '''if k == (ind+ int(n*0.6/duree)):
            print(duree/n*k)
            print(q)
            print(0.099 * q)
            y[1] += 0.099 * q'''
        Y.append(y)
        T.append(t)
    return  np.array(T),np.array(Y)


def find_index(liste, val,prec):
    """
        Renvoie l'indice i quand liste[i] est dans l'intervalle [val-prec, val+prec]
        Renvoie -1 si il n'y a pas un tel indice. 
    """
    i = 0
    while  i <len(liste):
        if liste[i] > (val -prec) and liste[i] < (val +prec):
            return i
        i +=1 
    return -1

def handy_resolu(xc0,y0,w0,delta ):
    """
        Résout le schéma HANDY remis à l'échelle 
    """
    k = 0
    f0 = np.array([xc0,y0,w0])
    theta = 1/2
    temps,sol = theta_method(handy_resc_eg,delta,k,theta,0,60,f0,10000)
    communers= sol[ :, 0]
    nature = sol[:, 1]
    richesse = sol[:,2]
    return temps, communers, nature, richesse


def aff(var,val,zer):
    """
        Affiche l'effet d'un controle sur la variable var 
    """
    debut = 10
    f = handy_resc
    y0=[0.5,0.125,100,0] # Conditions initiales
    delta = 0.0833 
    temps1,sol1 = theta_method(f,delta,k,theta,t0,tf,y0,n) # Solution témoin
    fig, ax = plt.subplots(2)
    ind = find_index(sol1[:,1][int(n*debut/duree):],30,1) # ind = indice où on veut agir
    ax[0].plot(temps1,sol1[:,0], label = 'x - Population')
    ax[0].plot(temps1,sol1[:,1], label = 'y - Nature')
    ax[0].plot(temps1,sol1[:,2], label = 'w - Richesse')
    ax[0].set_xlabel("Temps")
    ind += int(n*debut/duree)
    temps, sol = impulsion_temps(var,ind,zer,True)
    #temps, sol = moins_prod(var,ind,0.22)
    ax[1].plot(temps,sol[:,0], label = 'x - Population')
    ax[1].plot(temps,sol[:,1], label = 'y - Nature')
    ax[1].plot(temps,sol[:,2], label = 'w - Richesse')
    ax[1].set_xlabel("Temps")
    #plt.suptitle("Effet sur " + var +": baisse de 86% lorsque la nature est à 19")
    #plt.suptitle(r"Effet sur la production : nouveau $\delta$ à 0.25 lorsque la nature atteint 70 % de sa capacité lors du deuxième cycle")
    plt.suptitle("Reinjection de 9.9% de la richesse dans la nature")
    plt.legend()
    plt.show()

aff("w",5,0.99)

