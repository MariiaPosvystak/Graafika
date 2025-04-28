import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=x**2-5*x+6
plt.figure(facecolor='lightblue')
plt.title("Joonise pealkiri")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)
plt.plot(x,y,color='blue',linestyle='-', marker='D',markersize=8, label='Jooniseis')

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [16, 9, 4, 1, 0]

plt.plot(x, y1, linestyle='-', marker='o', color='blue',
         markersize=8, markerfacecolor='lightblue', label="Tõusev joon")
plt.plot(x, y2, linestyle='--', marker='x', color='green',
         markersize=8, label="Laskuv joon")

plt.title("Kahe joone näide")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.legend()
plt.grid(True)
plt.show()

plt.title("Graafiku pealkiri", fontsize=14, fontweight='bold')
plt.xlabel("x telg", fontsize=12)
plt.ylabel("y telg", fontsize=12)
plt.text(2, 10, "Tipp-punkt", fontsize=10, color='red')

plt.scatter(x,y1, color='blue', tabel="Tõusev joon")