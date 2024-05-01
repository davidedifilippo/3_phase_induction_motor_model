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

s = 0.0333
f_sinc = f/2
n_sinc = (f_sinc * 60)

print("Numero di giri del campo magnetico rotante:", n_sinc, "giri al minuto")

n = n_sinc * (1-s)
print("Numero di giri del rotore:", n, "giri al minuto")

# impedenza rotorica

Zr = Rr/s + Xlr*1j
print("Impedenza resistiva rotore", Zr)

Zin = Rs + Xls*1j + (Zr * Xm*1j)/(Zr + Xm*1j)
print("Impedenza d'ingresso della macchina ", Zin)

Zin_x = np.real(Zin)
Zin_y = np.imag(Zin)

# Coordinate polari (M, phi)
Zin_M = abs(Zin)
Zin_phi = np.angle(Zin)

print("Impedenza d'ingresso della macchina modulo", Zin_M, "fase in rad",  Zin_phi )

FP = np.cos(Zin_phi)
print("Fattore di potenza:", FP)

V_s = V_s_linea/np.sqrt(3)
I_s = V_s / Zin
print("Corrente statorica:", I_s)

I_s_eff = abs(I_s)
print("Valore efficace corrente statorica:", I_s_eff)

I_r = I_s * (Xm*1j)/(Zr+Xm*1j)
print("Corrente rotorica:", I_r)

I_r_eff = abs(I_r)
print("Valore efficace corrente rotorica:", I_r_eff)

Coppia_mecc = (1 / (2*np.pi*f_sinc)) * (I_r_eff * I_r_eff) * (Rr / s)
print("Coppia_meccanica:", Coppia_mecc, "N*m")

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

# disegno le risposte al variare delle velocità

plt.plot(s, Coppia_mecc)
plt.title("Andamento della coppia motrice")
plt.grid()
plt.show()

plt.plot(s, I_s_eff)
plt.title("Andamento della corrente")
plt.grid()
plt.show()
