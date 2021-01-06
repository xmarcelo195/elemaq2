from math import pi, sin, cos

'''
moldado = 0.25 até 0.45 || 1030-2070 kpa
tecido = 0.25 até 0.45  || 345-690 kpa
metal sinterizado = 0.15 até 0.45  || 1030-2070 kpa
ferro fundido ou aço endurecido = 0.15 até 0.25  || 690-720 kpa

'''


# input
densidade_aco = 7860  # kg/m3
budget = 700  # dinheiros
kg = 500*0.5
vi = 4  # m/s
vf = 0
s_freio = 5  # s
rigidez = 10 ** 7  # N/m rigidez mola
d_tambor = 0.350  # m
r = d_tambor / 2
massa_tambor = 50  # kg
j = (massa_tambor * (d_tambor / 2) ** 2) / 2
print('j=', j)
aceleracao = vi / s_freio
print('aceleração= ', aceleracao)

aceleracao_angular = aceleracao / (d_tambor / 2)
gravidade = 9.81  # m/s^2
# calculo do Torque
T1 = j * aceleracao_angular
T2 = kg * (gravidade + aceleracao) * (d_tambor / 2)
T = (T1 + T2)/2
print(T1, T2)
print('aceleração angular =', aceleracao_angular)
print('Torque desejado =', T)

# chutes

w = 0.048  # m
o1grau = 30
o2grau = 120
o1 = (pi / 180) * o1grau  #ultimo termo angulo 1
o2 = (pi / 180) * o2grau #ultimo termo angulo 2

#omax = 90 graus
delta_o = abs(o1 - o2)
a = 0.25
b = 0.1
c = 0.1  # 2c = 300
u = 0.45
r = 0.09
pmax = 2070*(10**3)  # pascal #tabelado

# calculo dos momentos
Mfn = w * r * b * (pmax / (sin(pi / 2))) * (1 / 2 * abs(o2 - o1) - (1 / 4) * (sin(2 * o2) - sin(2 * o1)))
print('mfn =', Mfn)

Mff = w * r * u * (pmax / (sin(pi / 2))) * (-r * (cos(o2) - cos(o1)) - b / 2 * (sin(o2) ** 2 - sin(o1) ** 2))
print('mff =', Mff)

Torque = u*w*r**2*pmax*(cos(o1)-cos(o2))/2
print('Torque nosso =', Torque)

Fa1 = (Mfn + Mff)/a
Fa2 = (Mfn - Mff)/a
Fa_total = max(Fa1, Fa2)
print('Fa =', Fa_total)

# calculo de x
x = Fa_total/rigidez
print('x =', x*1000, 'mm')

#dinheiros
material = [['moldado', 4000], ['tecido', 2000], ['metal', 5000], ['ferro', 3500]]
l = abs(o1grau-o2grau)*pi*r/180
print('arco =', l)

area_sapata = 2*l*w
print('area sapata= ', area_sapata)
preco_material = 4000*area_sapata
print('preço material = ', preco_material)

volume_aco = pi*r**2*w
print(pi*r**2*w)
preco_aco = volume_aco*densidade_aco* (50)

print('massa freio,', volume_aco*densidade_aco)
print('preço aço =', preco_aco)
print('preço total =', (preco_aco + preco_material))


##teste
