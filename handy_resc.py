import numpy as np

def heavy(x):
    """
        Fonction d'Heaviside
    """
    if x>0 :
        return 1
    else :
        return 0

def handy_resc(X,t,delta,k):
    """
        Modèle HANDY remis à l'échelle
    """
    xc,xe,y,w = X[0],X[1],X[2],X[3]
    xct = xc + 3*(xc*w/(xe+xc)-xc)*heavy(xc+xe-w)
    xet = xe + 3*(xe*k*w/(xe+xc)-xe)*heavy(xc+xe-k*w)
    yt = 0.5*y*(100-y)-delta*y*xc
    wt = delta*y*xc-5*(xc+xe)+5*(xc+xe-w)*heavy(xe+xc-w)
    return np.array((xct,xet,yt,wt))


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
