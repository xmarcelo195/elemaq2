from math import pi, asin, ceil
import numpy as np
import webbrowser


Peq = float(input('Potência do Equipamento(HP): '))
w1 = float(input('Rotação motor(rpm): '))
w2 = float(input('Rotação movida(rpm): '))

webbrowser.open_new(r'file:///home/marcelo/PycharmProjects/Elemaq2/PDF/Ks.pdf')
Ks = float(input('Ks: '))


"passo 1"
Pd = Peq*Ks
print('Potência de Projeto = ', round(Pd, 2), "HP")

"passo 2"
mg = w1/w2
print('mg = ', round(mg, 2))


"passo 3"

Vel = float(input('Velocidade(Ft/min)(Padrão 4000): '))
D1 = (Vel*12)/(pi*w1)*25.4
print('D1 Sugerido: ', round((D1), 2), "mm")


'passo 4'

V8 = [320, 335, 340, 380, 400, 430, 440, 445, 460, 480, 540, 550,
      650, 710, 750, 800, 880, 910, 950, 960, 1120, 1200, 1345, 1535]

V5 = [160, 170, 180, 190, 200, 210, 220,
      230, 240, 250, 280, 300, 320,
      350, 380, 400, 420, 450, 480, 500]

V3 = [80, 85, 90, 95, 100, 105, 110,
      115, 120, 125, 130, 140, 150, 160,
      170, 180, 190, 200, 220, 230,
      250, 280, 300, 320, 350, 380, 400]

webbrowser.open_new(r'file:///home/marcelo/PycharmProjects/Elemaq2/PDF/3v5v8v.pdf')
Tipo = float(input('Tipo de Correia: '))

"selecionar a lista de diametros do fabricante"

while Tipo != 3 and Tipo != 5 and Tipo != 8:
    Tipo = float(input('Tipo de Correia: '))

if Tipo == 3:
    V = V3
elif Tipo == 5:
    V = V5
elif Tipo == 8:
    V = V8

"Numero mais próximo"


def closest(lista, valor):
    lista = np.asarray(V)
    idx = (np.abs(lista - valor)).argmin()
    return lista[idx]



matriz = [["D1", " D2t", "  D2", " mg", " W2(real)", "Erro", "Vel"],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],]


pos = int(V.index(closest(V, D1)))

if (pos + 2) >= int(len(V)):
    Dmin = int(len(V) - 9)
elif (pos - 2) <= int(0):
    Dmin = 0
else:
    Dmin = (pos - 4)

"Definir os valores D1(comercial)"
for l in range(1, 10):
    matriz[l][0] = (V[Dmin])
    Dmin = Dmin + 1

"Definir os valores D2(teo)"

for l in range(1, 10):
    matriz[l][1] = round(matriz[l][0] * mg, 2)

"Definir os valores de D2(comercial)"
for l in range(1, 10):
    matriz[l][2] = closest(V, (matriz[l][1]))

"Definir o mg"
for l in range(1, 10):
    matriz[l][3] = float(round(matriz[l][2] / matriz[l][0], 2))

"Definir W real"

for l in range(1, 10):
    matriz[l][4] = round(w1 / matriz[l][3], 2)

"erro"
for l in range(1, 10):
    matriz[l][5] = round(abs(matriz[l][3] - mg)*100 / mg, 2)

"velocidade"
for l in range(1, 10):
    matriz[l][6] = round((pi * (matriz[l][2] / 25.4) * matriz[l][4]) / 12, 2)

"mostrar a matrz"
for l in range(0, 10):
    for c in range(0, 7):
        print(matriz[l][c], " " * 5, end='')
    print()

D1f = float(input('D1(Final): '))
D2f = float(input('D2(Final): '))

"calculo da distancia entre centros"

Cmin = D2f
Cmax = 3 * (D1f + D2f)

print('Distancia entre centros deve ser', Cmin, "≤ C ≤", '{:.2f}'.format((Cmax)), "mm")
Cteo = float(input('Digite o valor de C: '))

'calculo L da correia'

L = 2 * Cteo + (pi / 2) * (D1f + D2f) + ((D2f - D1f) ** 2) / (4 * Cteo)
print('O Valor teórico de L é: ', '{:.2f}'.format(L))

'Calculo do C real'
webbrowser.open_new(r'file:///home/marcelo/PycharmProjects/Elemaq2/PDF/Lreal.pdf')
Lreal = float(input('Valor de L real: '))

Creal = Cteo - (L-Lreal)/2

print("Distancia entre Centros real: ", '{:.2f}'.format(Creal))

"Calculo Θ1"

O1 = 180 - 2*(asin((D2f-D1f)/(2*Creal))*(180/pi))
O2 = 360 - O1
print('Valor de Θ1 = ', '{:.2f}'.format(O1))
print('Valor de Θ2 = ', '{:.2f}'.format(O2))

"correção Θ1"
webbrowser.open_new(r'file:///home/marcelo/PycharmProjects/Elemaq2/PDF/C0.pdf')
C0 = float(input('Valor C0 = '))

"correção comprimento"
webbrowser.open_new(r'file:///home/marcelo/PycharmProjects/Elemaq2/PDF/CL.pdf')
print('O Valor de L em polegadas é: ', '{:.2f}'.format(Lreal/25.4))
Cl = float(input('Valor Cl = '))

"numero de correias"

if Tipo == 3:
    webbrowser.open_new(r'file:///home/marcelo/PycharmProjects/Elemaq2/PDF/Pc_3v.pdf')
    print('O Valor de D1 em polegadas é: ', '{:.2f}'.format(D1f / 25.4))
    Pc = float(input('Valor de Pc: '))

elif Tipo == 5:
    webbrowser.open_new(r'file:///home/marcelo/PycharmProjects/Elemaq2/PDF/Pc_5v.pdf')
    print('O Valor de D1 em polegadas é: ', '{:.2f}'.format(D1f / 25.4))
    Pc = float(input('Valor de Pc: '))

elif Tipo == 8:
    webbrowser.open_new(r'file:///home/marcelo/PycharmProjects/Elemaq2/PDF/Pc_8v.pdf')
    print('O Valor de D1 em polegadas é: ', '{:.2f}'.format(D1f / 25.4))
    Pc = float(input('Valor de Pc: '))

num = Pd/(C0*Cl*Pc)
print('Número de Correias necessárias: ', ceil(num))
