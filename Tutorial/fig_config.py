import matplotlib.pyplot as plt

plt.subplot(121)
plt.xlim(-1.5,1.25)
plt.ylim(-1.5,1.6)
plt.xlabel(r'$\log([\rm NII]/H\alpha)$', fontsize=18)
plt.ylabel(r'$\log([\rm OIII]/H\beta)$', fontsize=18)
plt.title('BPT Diagram', fontsize=20)

plt.subplot(122)
plt.xlim(-1.5,1.25)
plt.ylim(-1.1,3.05)
plt.xlabel(r'$\log([\rm NII]/H\alpha)$', fontsize=18)
plt.ylabel(r'$\log(\rm W_{H\alpha})$', fontsize=18)
plt.title('WHAN Diagram', fontsize=20)
