from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pickle
from theta_method import theta_method
from handy_resc_eg import handy_resc_eg

def handy_resolu(xc0,y0,w0,delta ):
    k = 0
    jacob = 0
    f0 = np.array([xc0,y0,w0])
    theta = 1/2
    temps,sol = theta_method(handy_resc_eg,delta,k,theta,0,100,f0,10000)
    communers= sol[ :, 0]
    nature = sol[:, 1]
    richesse = sol[:,2]
    return temps, communers, nature, richesse

def limite(x,y,w,c):
    xl,wl,yl= [],[],[]
    for i in range(1,len(c)):
        if  x[i]==x[i-1] and y[i] == y[i-1] and c[i-1]!=c[i] :
            xl.append(x[i-1])
            wl.append(w[i-1])
            yl.append(y[i-1])
        if y[i] == 5 : 
            x5.append(x[i])
            y5.append(y[i])
            w5.append(w[i])
            c5.append(c[i])
    return xl,yl,wl


def cercle_limite(x0,y0,w0,delta):
    X = handy_resolu(x0,y0,w0,delta)
    return X[1][9000:],X[2][90000:],X[3][9000:]

pref = "./bista/"
#pref = ''
heures_50= ['11:16:55','11:42:25','11:45:13','11:48:31','14:07:27','14:33:14','14:41:05','14:51:55','14:53:12','14:55:09','14:57:06','15:38:55']
heures_1 = ['09:42:45','09:54:20','10:12:06','10:27:51','10:49:31','11:05:57','11:10:51','11:16:48','11:18:16']
heures_99 = ['14:16:32','14:43:29','14:41:25']
heures_25 = ['15:46:22']
heures_12 = ['16:16:30']
heures_7 = ['17:18:13']
heures_3 = ['09:41:31']
heures_5 = ['18:37:20','19:27:31']
heures_77 = ['11:55:36']
heures_66 = ['13:07:20']
heures_88 =['14:05:43']
heures_33 = ['15:12:12','15:13:27']
heures_44=['16:02:12','16:11:20']
heures_55 = ['17:07:35']
heures_100 = ['21:00:16']
heures_19 = ['15:20:22']
delta_25 = ['07:18:19']
delta_31 = ['031','11:36:42']
x0,w0,y0,xl,wl,yl,c,cp = [],[],[],[],[],[],[],[]
x5,y5,w5,c5 = [],[],[],[]
couleurs = ["blue","purple"]
i = 0
for heures in [heures_5,heures_7,heures_12,heures_25,heures_33,heures_44,heures_55,heures_66,heures_77,heures_88,heures_99]:
#for heures in [delta_31,delta_25]:
#for heures in [heures_12]:
    for heure in heures :
        lc = pickle.load(open(pref+'x0_'+heure+'_.pkl', 'rb'))
        x0 += lc
        y0 +=pickle.load(open(pref+'y0_'+heure+'_.pkl','rb'))
        w0 +=pickle.load(open(pref+'w0_'+heure+'_.pkl', 'rb'))
        c  +=pickle.load(open(pref+'c_'+heure+'_.pkl', 'rb'))
        x,y,w = limite(x0,y0,w0,c)
        xl += x
        yl += y
        wl += w
    i += 1

axe =plt.axes(projection='3d')
axe.scatter(x0,y0,w0)

#xcl,ycl,wcl = cercle_limite(0.5,100,0,0.29)
#axe.plot(xcl,ycl,wcl)
plt.show()
ax =plt.axes(projection='3d')
ax.scatter(xl,yl,wl)
X =handy_resolu(0.5,100,0,0.29)
ax.plot(X[1],X[2],X[3],c="black")
ax.set_xlabel(r'$x_0$ - Population')
ax.set_ylabel(r'$y_0$ - Nature')
ax.set_zlabel(r'$w_0$ - Richesse ')
plt.show()
plt.plot(X[1],X[3])
plt.scatter(xl,wl)
plt.show()
