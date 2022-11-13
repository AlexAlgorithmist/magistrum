import turtle as t
from random import randint as r, choice as c



t.hideturtle()
t.tracer(0)



mas_cords = []
inp = int(input(">>>"))
col = 0



for n in range(inp):
    mas_cords_p = []
    mas_cords_p.append(n)
    mas_cords_p.append(r(-600, 600))
    mas_cords_p.append(r(-300, 300))
    mas_cords.append(mas_cords_p)
    del(mas_cords_p)


s_p = r(0, inp - 1)
t.penup()
m = mas_cords[s_p]
t.goto(m[1], m[2])
t.pendown()
del(m)

while True:
    for k in range(1000):
        mas_cords_p = []
        for m in mas_cords:
            mas_cords_p.append(m)
        del(mas_cords_p[s_p])
        col += 1
        col = col % 1000000
        col_s = "#"
        col_s += "0" * (6 - len(str(col)))
        col_s += str(col)
        t.pencolor(col_s)
        mas_cord_pp = c(mas_cords_p)
        t.goto(mas_cord_pp[1], mas_cord_pp[2])
        for n in range(inp):
            mas_cords_p_s = mas_cords[n]
            mas_cords_p_s[1] = mas_cords_p_s[1] + r(-5, 5) / 10
            mas_cords_p_s[2] = mas_cords_p_s[2] + r(-5, 5) / 10
            mas_cords[n] = mas_cords_p_s
        s_p = mas_cord_pp[0]
    t.update()