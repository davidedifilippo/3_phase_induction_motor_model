import numpy as np
import matplotlib.pyplot as plt

# Tensione, frequenza di alimentazione

f = 50
V_s_linea = 230

# Parametri della macchina (collegamento a stella)

p = 2
Rs = 0.295
Rr = 0.379
Xm = 22.243
Xls = Xlr = 0.676

# scorrimento a carico

f_sinc = f/2
n_sinc = (f_sinc * 60)

print("------------------")
print("All'avviamento s = 1 -> rotore fermo")

s = np.linspace(0.001, 1)

# impedenza rotorica

Zr = Rr/s + Xlr*1j


Zin = Rs + Xls*1j + (Zr * Xm*1j)/(Zr + Xm*1j)


Zin_x = np.real(Zin)
Zin_y = np.imag(Zin)

# Coordinate polari (M, phi)

Zin_M = abs(Zin)
Zin_phi = np.angle(Zin)
FP = np.cos(Zin_phi)


V_s = V_s_linea/np.sqrt(3)
I_s = V_s / Zin
I_s_eff = abs(I_s)
I_r = I_s * (Xm*1j)/(Zr+Xm*1j)
I_r_eff = abs(I_r)
Coppia_mecc = (1 / (2*np.pi*f_sinc)) * (I_r_eff * I_r_eff) * (Rr / s)

V_s_linea_1 = 100

V_s_1 = V_s_linea_1/np.sqrt(3)
I_s_1 = V_s_1 / Zin
I_s_eff_1 = abs(I_s_1)
I_r_1 = I_s_1 * (Xm*1j)/(Zr+Xm*1j)
I_r_eff_1 = abs(I_r_1)
Coppia_mecc_1 = (1 / (2*np.pi*f_sinc)) * (I_r_eff_1 * I_r_eff_1) * (Rr / s)

V_s_linea_2 = 170

V_s_2 = V_s_linea_2/np.sqrt(3)
I_s_2 = V_s_2 / Zin
I_s_eff_2 = abs(I_s_2)
I_r_2 = I_s_2 * (Xm*1j)/(Zr+Xm*1j)
I_r_eff_2 = abs(I_r_2)
Coppia_mecc_2 = (1 / (2*np.pi*f_sinc)) * (I_r_eff_2 * I_r_eff_2) * (Rr / s)


# disegno le risposte al variare delle velocità
plt.figure(1)
plt.plot(f_sinc * 60 - s * f_sinc * 60, Coppia_mecc,  label='Vs = 230')
plt.plot(f_sinc * 60 - s * f_sinc * 60, Coppia_mecc_1, label='Vs = 100')
plt.plot(f_sinc * 60 - s * f_sinc * 60, Coppia_mecc_2, label='Vs = 170')
plt.legend()
plt.ylabel('Coppia motrice')
plt.xlabel('rpm')
plt.title("Andamento della coppia motrice")
plt.grid()


plt.figure(2)

plt.plot(f_sinc * 60 - s * f_sinc * 60, I_s_eff, label='Vs = 230')
plt.plot(f_sinc * 60 - s * f_sinc * 60, I_s_eff_1, label='Vs = 100')
plt.plot(f_sinc * 60 - s * f_sinc * 60, I_s_eff_2, label='Vs = 170')
plt.legend()
plt.ylabel('Corrente assorbita')
plt.xlabel('rpm')
plt.title("Andamento della corrente")
plt.grid()
plt.show()




