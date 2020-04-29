#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

with open("/Users/damym/data0.dat", "r") as file:
    contents_cero=file.read()
with open("/Users/damym/data-1.dat", "r") as file:
    contents_uno=file.read()
#specials with the mod every 100 values:
with open("/Users/damym/data-2.dat", "r") as file:
    contents_dos=file.read()
with open("/Users/damym/data-3.dat", "r") as file:
    contents_tres=file.read()
with open("/Users/damym/data-4.dat", "r") as file:
    contents_quatro=file.read()
with open("/Users/damym/data-5.dat", "r") as file:
    contents_five=file.read()
with open("/Users/damym/data-6.dat", "r") as file:
    contents_six=file.read()


# In[3]:


import os

dirpath =os.getcwd()
print(dirpath)


# In[46]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,9,100000)
anal= np.exp(-3*t)
x0 = np.loadtxt("/Users/damym/data0.dat", delimiter = ', ',unpack=True)
#x0= (1,-2,4,-8,16,-32,64,-128,256,-512)
t0 = np.linspace(0,9,len(x0))

x1 = np.loadtxt("/Users/damym/data-1.dat", unpack=True)
#x1= (1, 0.7, 0.49, 0.343, 0.2401, 0.16807, 0.117649, 0.0823543, 0.057648, 0.0403536, 0.0282475, 0.0197733, 0.0138413, 0.0096889, 0.00678223, 0.00474756, 0.00332329, 0.0023263, 0.00162841, 0.00113989, 0.000797922, 0.000558546, 0.000390982, 0.000273687, 0.000191581, 0.000134107, 9.38748e-05, 6.57123e-05, 4.59986e-05, 3.2199e-05, 2.25393e-05, 1.57775e-05, 1.10443e-05, 7.73099e-06, 5.41169e-06, 3.78818e-06, 2.65173e-06, 1.85621e-06, 1.29935e-06, 9.09543e-07, 6.3668e-07, 4.45676e-07, 3.11973e-07, 2.18381e-07, 1.52867e-07, 1.07007e-07, 7.49048e-08, 5.24333e-08, 3.67033e-08, 2.56923e-08, 1.79846e-08, 1.25892e-08, 8.81247e-09, 6.16873e-09, 4.31811e-09, 3.02268e-09, 2.11587e-09, 1.48111e-09, 1.03678e-09, 7.25745e-10, 5.08021e-10, 3.55615e-10, 2.48931e-10, 1.74251e-10, 1.21976e-10, 8.53832e-11, 5.97682e-11, 4.18378e-11, 2.92864e-11, 2.05005e-11, 1.43503e-11, 1.00452e-11, 7.03167e-12, 4.92217e-12, 3.44552e-12, 2.41186e-12, 1.6883e-12, 1.18181e-12, 8.27269e-13, 5.79088e-13, 4.05362e-13, 2.83753e-13, 1.98627e-13, 1.39039e-13, 9.73274e-14, 6.81292e-14, 4.76904e-14, 3.33833e-14, 2.33683e-14, 1.63578e-14)
t1 = np.linspace(0,9,len(x1))

x2 = np.loadtxt("/Users/damym/data-2.dat", delimiter = ', ',unpack=True)
#x2= (1, 0.0461261,0.00226125,0.000107529,5.11327e-06,2.4315e-07,1.15624e-08,5.49823e-10,2.61455e-11,1.24329e-12)
t2= np.linspace(0,9,len(x2))

x3 = np.loadtxt("/Users/damym/data-3.dat", delimiter = ', ',unpack=True)
#print(len(t2))
#x3= (1, 0.0494133,0.00245639,0.000121379,6.01578e-06,2.98154e-07,1.47771e-08,7.32385e-10,3.62985e-11,1.80444e-12)
t3= np.linspace(0,9,len(x3))

x4 = np.loadtxt("/Users/damym/data-4.dat", delimiter = ', ', unpack=True)
#x4=(1,0.0497697,0.00245639,0.000100968,6.10068e-06,1.95095e-07,1.52344e-08,7.61399e-10,3.80426e-11,1.90133e-12)
t4= np.linspace(0,9,len(x4))

x5 = np.loadtxt("/Users/damym/data-5.dat", delimiter = ', ',unpack=True)
#x5=(1,0.223543,0.0500254,0.0111956,0.00250539,0.000560684,0.000125476,2.80804e-05,6.28396e-06,1.40634e-06,3.14707e-07,7.04306e-08,1.57617e-08,3.52733e-09,7.89385e-10,1.76652e-10,3.95332e-11,8.20902e-12)
t5= np.linspace(0,9,len(x5))

x6 = np.loadtxt("/Users/damym/data-6.dat", delimiter = ', ',unpack=True)
#x6 = (1,0.47424,0.227355,0.0522567,0.0239274,0.0109563,0.00501668,0.00229687,0.0010518,.000481597,0.000100968,0.000100965,4.6233e-05,2.11686e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
t6 = np.linspace(0,9,len(x6))




plt.plot(t,anal,'r')
plt.ylim(0,1)
#dy's at .000001, .00001, .0001, .001, .01, .1,
plt.plot(t0,x0,'c')
plt.plot(t1,x1,'m')
plt.plot(t2,x2,'g')
plt.plot(t3,x3,'y') #% less than 100
plt.plot(t4,x4,'k')
plt.plot(t5,x5,'m^')
plt.plot(t6,x6,'w')
plt.xlim(0,5)
#plt.savefig()


# In[ ]:





# In[ ]:




