import matplotlib.pyplot as plt
import numpy as np

y=np.array([40,25,20,15])
datas=["fruits","groceries","chocolates","others"]
mexplode=[0,0,0,0]

plt.pie(y, labels=datas,explode=mexplode , shadow=True)
plt.show()
