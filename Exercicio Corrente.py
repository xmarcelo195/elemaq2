from math import pi, asin, sin, sqrt
import webbrowser

Peq = float(10)
w1 = float(2500)
w2 = float(900)
Ks = float(1)

#webbrowser.open_new(r'PDF Corrente/fator de serviço.pdf')


"passo 1"
Pd = Peq*Ks
print('Potência de Projeto = ', round(Pd, 2), "HP")

"passo 2"
mg = w1/w2
print('mg = ', round(mg, 2))

N1 = int(input('digite n1 (padrão 17): '))
N2t = mg*N1

#webbrowser.open_new(r'PDF Corrente/CATALOGO_RODAS_DENTADAS (1).pdf')
print('o valor de N2 téorico é: ', round(N2t, 2), 'verificar no catálogo')
VerifN2 = input('tem o inteiro de n2 no catalogo? (s),(n): ')

'utilizar o n2 com menor erro'
if VerifN2 == "n":
    t1 = int(input('Nº mais proximo 1: '))
    t2 = int(input('Nº mais proximo 2: '))

    t1_err = (((1/(sin(pi/t1)))/(1/(sin(pi/N1)))-mg)/mg)*100
    t2_err = ((((1/sin(pi/t2))/(1/sin(pi/N1)))-mg)/mg)*100

    print('erro de', t1, 'dentes =', round(abs(t1_err), 2), '%')
    print('erro de', t2, 'dentes =', round(abs(t2_err), 2), '%')

    N2 = int(input('qual n2 usar?: '))
    print('novo w2 = ', N1*w1/N2)
else:
    N2 = round(N2t, 0)
    print('novo w2 = ', round((N1 * w1 / N2), 2))

print('')
print('potência por corrente:')
print('Para 1 corrente: ', round(Pd/1, 2))
print('Para 2 corrente: ', round(Pd/1.7, 2))
print('Para 3 corrente: ', round(Pd/2.5, 2))
print('Para 4 corrente: ', round(Pd/3.3, 2))
print('Para 5 corrente: ', round(Pd/3.9, 2))
print('Para 6 corrente: ', round(Pd/4.6, 2))

webbrowser.open_new(r'PDF Corrente/Tabelas_Potencia_Corrente_Rolos (1).pdf')
Qnt_c = int(input('quantidade de corrente: '))

passo = float(input('Passo(in): '))


print('Distancia entre centros deve ser', '30*p', "≤ C ≤", '50*p',)
Cteo = float(input('Digite o valor de C (*p): '))

'calculo dos diametros'
D1 = passo/(sin(pi/N1))
D2 = passo/(sin(pi/N2))

print('D1 = ', D1, 'pol')
print('D2 = ', D2, 'pol')

'calculo L da correia'

Lt = (2 * Cteo + (N2+N1)/2 + ((N2-N1)**2/(4*pi*Cteo)))

print('O Valor teórico de L é: ', '{:.2f}'.format(Lt), '*p')
print('O Valor teórico de L é: ', round(Lt*passo, 2), 'in')

L = int(input('valor ajustado de L para o numero par mais prox: '))

'Calculo do C real'

Creal = 1/4*((L - ((N2+N1)/2)) + sqrt((L-(N2+N1)/2)**2-(8*(N2-N1)**2/(4*pi**2))))*passo

print("Distancia entre Centros real: ", '{:.2f}'.format(Creal), 'in')
print("Distancia entre Centros real: ", '{:.2f}'.format(Creal/passo), '*p')
"Calculo Θ1"

O1 = 180 - 2*(asin((D2-D1)/(2*Creal))*(180/pi))
O2 = 360 - O1
print('Valor de Θ1 = ', '{:.2f}'.format(O1))
print('Valor de Θ2 = ', '{:.2f}'.format(O2))

"calcular dinheiro"
##RESTRIÇÃO VERTICAL DE ESPAÇO: 10 polegadas  |
##RESTRIÇÃO HORIZONTAL DE ESPAÇO: 25 polegadas ___
##BUDGET (ORÇAMENTO): R$ 375,00 (Trezentos e Setenta e Cinco Reais)

pes_n1 = float(input('digite peso em lb n1'))
pes_n2 = float(input('digite peso em lb n2'))

P_elo = float(input('preço por elo:'))


Pn1 = 40*(pes_n1/2.205)
Pn2 = 40*(pes_n2/2.205)
print('preço n1 = ', Pn1)
print('preço n2 = ', Pn2)

Pcorr = L*P_elo*Qnt_c
print('preço da corrente', Pcorr)

print('preço total = ', (Pn1+Pn2+Pcorr))