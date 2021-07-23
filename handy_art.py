import numpy as np

#CONSTANTE DE L'ARTICLE
alpham = 1E-2
alphaM = 7E-2 
betac = 3E-2
betae = 3E-2
s = 5E-4
rho = 5E-3
gama = 1E-2
lamba = 100
k = 10
xc0 = 100
y0 = lamba
w0 = 0
eta = (alphaM-betac)/(alphaM-alpham)
chiM = gama/(eta*s)*lamba**2/4

def handy_art(X,t,delta,k):
    """
        Modèle HANDY de l'article
    """
    xc,xe,y,w = X[0],X[1],X[2],X[3]
    wth = rho*xc + k*rho*xe
    cc = min(1, w/wth)*s*xc
    ce = min(1,w/wth)*k*s*xe
    alphac = alpham + max(0,1-cc/(s*xc))*(alphaM-alpham)
    alphae = alpham + max(0,1-min(1,w/wth)*k)*(alphaM-alpham)
    xct = betac*xc - alphac*xc
    xet = betae*xe - alphae*xe
    yt = gama*y*(lamba-y) - delta*xc*y
    wt = delta*xc*y - cc -ce 
    return np.array((xct,xet,yt,wt))