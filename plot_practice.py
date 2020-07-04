"""
Plotting practice
This script is based on Markus Possel's "A beginner's guide to working with astronomical data" 
Section 8 : Basic plotting with Python and Matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,200)
y = np.sin(x)

#%% Plotting a function
plt.clf()
plt.plot(x,y)

#%% Making plots look better
plt.clf()
plt.xlabel('Time in seconds')
plt.ylabel('Pendulum angle [units]') #added axis labels
plt.xlim(0,2*np.pi)
plt.ylim(-1.1,1.1) #specified plot limits
plt.plot(x,y,'r',lw=3.0,linestyle='dotted') #specified red, dotted line with width 3

#%% Annotating plots
plt.clf()
plt.xlabel('Time in seconds')
plt.ylabel('Pendulum angle [units]')
plt.xlim(0,2*np.pi)
plt.ylim(-1.1,1.1)
plt.axhline(0.0,color='m')       #added horizontal line
plt.axvline(0.5*np.pi,color='g') #added vertical line
plt.annotate('intersection!',xy=(np.pi,0),xytext=(4,0.3),fontsize=12,arrowprops=dict(arrowstyle='->',facecolor='k')) #added annotation pointing to the intersection
plt.plot(x,y)

#%% Figure size
plt.clf()
plt.figure(figsize=(6,2)) #specified the image size (in inches)
plt.xlabel('Time in seconds')
plt.ylabel('Pendulum angle [a.u.]')
plt.xlim(0,2*np.pi)
plt.ylim(-1.1,1.1)
plt.plot(x,y)

#%% Scatter plots
nm = ['SDSS-II SN 21387','SDSS-II SN 13651','SDSS-II SN 03706','SDSS-II SN 10963','SDSS-II SN 03475']
dpc = [4200.,1700.,3720.,577.,1040.]
zv = [0.48,0.25,0.44,0.09,0.3]
sizes = [40,15,25,80,38] #list used to specify the size of each data point in the plot
plt.clf()
plt.xlabel('Redshift z')
plt.ylabel('Distance in Mpc')
plt.scatter(zv,dpc,marker='^',color='r',s=sizes)
#plt.plot(zv,dpc,'o') #plotting using plot instead of scatter

#%% Fitting data
#popt, pcov = np.polyfit(zv,dpc,1,cov=True) #returns estiamted coeficients in polynomial fit and the associated covariance matrix
#perr = np.sqrt(np.diag(pcov)) #estimate the errors using the square root of the diagonal terms
#line_x = [min(zv),max(zv)]
#line_y = [popt[0]*min(zv)+popt[1],popt[0]*max(zv)+popt[1]]

from scipy.optimize import curve_fit
def fitFunc(x,a):
    return x*a
popt, pcov = curve_fit(fitFunc,zv,dpc) #returns estimated parameters for the defined function fitFunc and the covariance matrix
perr = np.sqrt(np.diag(pcov))
line_x = np.array([min(zv),max(zv)])
line_y = fitFunc(line_x,popt[0])

plt.clf()
plt.xlabel('Redshift z')
plt.ylabel('Distance in Mpc')
plt.scatter(zv,dpc,marker='.')
plt.plot(line_x,line_y,color='r')

#%% Histograms
randArray = np.random.rand(10000) # + np.random.rand(10000)
#plt.clf()
#plt.hist(randArray,bins=30)

gaussDraw = np.random.randn(100000)
plt.clf()
plt.hist(gaussDraw,40)
#plt.savefig('pratice_plot.pdf',bbox_inches='tight',replace='true') #saves figure to pdf file