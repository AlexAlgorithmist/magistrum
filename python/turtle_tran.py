import turtle as t

t.speed(100)
t.penup()
t.back(750)
t.pendown()

def prob():
    t.penup()
    t.forward(30)
    t.pendown()

def a():
    t.left(70)
    t.forward(50)
    t.right(140)
    t.forward(25)
    t.right(110)
    t.forward(18)
    t.back(18)
    t.left(110)
    t.forward(25)
    t.right(120)
    t.penup()
    t.right(170)
    t.forward(10)
    t.pendown()

def b():
    t.left(90)
    t.forward(40)
    t.right(120)
    t.forward(23)
    t.right(130)
    t.forward(23)
    t.left(130)
    t.forward(23)
    t.right(130)
    t.forward(23)
    t.penup()
    t.left(159.9)
    t.forward(30)
    t.pendown()

tran = {'a' : 'a', 'b' : 'b', ' ' : 'prob'}
mas = []
mas1 = [a, b, prob]
name = ''

inp = str(input())
for ch in inp:
    if ch in tran:
        mas.append(tran[ch])
    else:
        pass
fun_now = {f.__name__ : f for f in mas1}
for k in range(len(mas)):
    ch1 = mas.pop(0)
    fun_now[ch1]()
t.mainloop()