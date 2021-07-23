import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from theta_method import theta_method
from handy_resc_eg import handy_resc_eg
from tqdm import tqdm
import pickle 
from time import strftime
from datetime import datetime

def handy_resolu(xc0,y0,w0,delta):
    """
        Résoud le modèle HANDY dans le cas d'une société égalitaire
    """
    k = 0
    jacob = 0
    f0 = np.array([xc0,y0,w0])
    theta = 1/2
    temps,sol = theta_method(handy_resc_eg,jacob,delta,k,theta,0,100,f0,10000)
    communers= sol[ :, 0]
    nature = sol[:, 1]
    richesse = sol[:,2]
    return temps, communers, nature, richesse

def est_eq(x,y,w):
    """
        Détermine si (x,y,w) sont un point d'équilibre
    """
    ok = False 
    if (x_e -  1) <= x and x <= (x_e + 1):
        if (y_e -  1) <= y and y <= (y_e + 1):
            if (w_e -  1) <= w and w <= (w_e + 1):
                ok = True
    return ok 


i = 1
j = 0
delta = 0.25
X0, Y0, W0,C = [],[],[],[]
#Point d'équilibre 
x_e = 5/delta*(10 - 1/(3*delta))
y_e = 10/(3*delta)
w_e = 10/(3*delta)*(10 - 1/(3*delta))


x0_range = np.arange(50,400,30)
yc = 5 # si on veut calculer un plan (x,w)
y0_range = np.arange(5,100,10)
w0_range = np.arange(0,800, 30)
for x0 in tqdm(x0_range) :
    y0 = yc
    if y0 == yc:
    #for y0 in (y0_range):
        for w0 in (w0_range):
            temps, com,nat,rich = handy_resolu(x0,y0,w0,delta)
            X0.append(x0)
            Y0.append(y0)
            W0.append(w0)
            if est_eq(com[-1],nat[-1],rich[-1]):
                C.append("red")
            else:
                C.append("blue")

# Enregistrement des valeurs
time = datetime.now().strftime("%H:%M:%S")
pickle.dump(X0,open("x0_"+str(time)+"_.pkl","wb"))
pickle.dump(Y0,open("y0_"+time+"_.pkl","wb"))
pickle.dump(W0,open("w0_"+time+"_.pkl","wb"))
pickle.dump(C,open("c_"+time+"_.pkl","wb"))

# Affichage
plt.scatter(X0,W0,c=C)
plt.scatter(x_e,w_e,c="black")
plt.xlabel(r"$x_0$ - Population")
plt.ylabel(r"$w_0$ - Richesse")
plt.legend()   
plt.show()



