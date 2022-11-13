from math import log, e

def In(a):
    return log(a, e)

# Порядок (счёт в кг): [начальная масса, конечная масса, кол-во двигателей, УИ, ускорение свободного падения]

mas = [[500, 300, 5, 160, 9.780327], [290, 20, 1, 400, 9.480327], [19, 2, 1, 1600, 8.380327]]
mas_2 = []
Dvo = 0

for mas_1 in mas:
    nm, km, k, UI, S = mas_1
    Dv = UI / k * In((nm / km))
    mas_2.append(Dv)
    Dvo += Dv

print(f"Общее DV = {Dvo}; по ступеням: {1*mas_2}.")