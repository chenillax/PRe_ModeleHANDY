import numpy as np

def heavy(x):
    """
        Fonction d'Heaviside
    """
    if x>0 :
        return 1
    else :
        return 0

def handy_resc_eg(X,t,delta,k):
    """
        Modèle HANDY remis à l'échelle dans le cas d'une société égalitaire (n'a qu'un seul type de population)
    """
    xc,y,w = X
    xct = xc + 3*(xc*w/(xc)-xc)*heavy(xc-w)
    yt = 0.5*y*(100-y)-delta*y*xc
    wt = delta*y*xc-5*(xc)+5*(xc-w)*heavy(xc-w)
    return np.array((xct,yt,wt))


def jacob (X,delta):        
    x,y,w = X
    if ((x-w)>0):
        return np.array(([-2,0,3],[-delta*y,50-y-delta*x,0],[delta*y,delta*x,-5]))
    else:
        return np.array(([1,0,0],[-delta*y,0,50-y-delta*x,0],[delta*y-5,delta*x,0]))

# CONSTANTES 
betac = 3E-2
betae = 3E-2
gama = 1E-2
lamba = 100
k = 1
s = 5E-4
rho = 5E-3
alpham = 1E-2
alphaM = 7E-2 
xc0 = 100
xe0 = 25
y0 = lamba
w0 = 0
eta = (alphaM-betac)/(alphaM-alpham)
chiM = gama/(eta*s)*lamba**2/4
delta_opt = 6.67E-6
delta_opt2 = 8.33E-6



delta_resc  = delta_opt/(rho*(betac-alpham))
delta_resc_2  = delta_opt2/(rho*(betac-alpham))
xc0_resc = xc0*rho
xe0_resc = xe0*rho*k
chiM_resc = gama/2*lamba/delta_resc

