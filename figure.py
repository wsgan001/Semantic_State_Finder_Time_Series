import matplotlib.pyplot as plt
import numpy as np
x1 = np.loadtxt("/home/hao/py-work/PythonHMM/data-rle.csv", delimiter = ",", usecols = (0,), dtype = int)
x2 = np.loadtxt("/home/hao/py-work/PythonHMM/data-rle.csv", delimiter = ",", usecols = (1,), dtype = int)
#y2 = np.loadtxt("/home/hao/datasets/REDD/test.dat", delimiter = " ", usecols = (1,), dtype = float)
y2 = np.loadtxt("/home/hao/py-work/PythonHMM/data-rle.csv", delimiter = ",", usecols = (2,), dtype = int)
y1 = y2.tolist()
y1.insert(0,0)
del y1[-1]
print y1
plt.plot([x1,x2], [y2,y2],'b-',[x1,x1],[y1,y2],'r--')
plt.xlabel('time')
plt.ylabel('symbol')
plt.axis([0,24000,-0.5,9])
plt.show()