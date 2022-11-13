import vv;c='';mas_reklama=['https://ege.com','https://www.aviasales.ru/?etext=&params=','https://www.avito.ru/'];mas_otv=['Молодец!','Правильно!','Отлично!'];mas_n_otv=['Не получилось','Почти','Неправильно'];print('As\nWe\nCan\n');a=0
def poisk(b='>>>'):
    vvod=str(input('На что вам нужна ссылка?\n'+b));mas_vuvod=vv.preob.poisk(vvod)
    for k in range(len(mas_vuvod)):print(mas_vuvod.pop())
    menu()
def chard():
    b=str(input('Введите текст который превратится в символы:\n'));print(*vv.preob.to_chards(b))
    menu()
def frases():
    b=str(input('Введите текст который превратится в буквы:\n'));print(*vv.preob.to_frases(b))
    menu()
def m_test(b='>>>'):
    c=input('Введите уровень сложности (1 - 4)\n'+b)
    if vv.str(c)or c=='':an_idiot();menu()
    c=int(c);
    if c<1or c>4:an_idiot();menu()
    else:
        d=vv.math_test(c);f=d[0]+'\n'+b;e=str(input(f))
        if e==d[1]:print(vv.random.randchose(mas_otv))
        else:print(vv.random.randchose(mas_n_otv))
    menu()
def an_idiot():
    с=str(input('Ты идиот?\n>>>'))
    if c=='Да'or с=='да':print('Я знал.')
    else:print('А похоже.')
def rand(b='>>>'):
    d=input('Какой битности вам нужно число (больше 0 и меньше 500)?\n'+b)
    if vv.str(d)or d=='':an_idiot();menu()
    d=int(d)
    if d>500or d<0:an_idiot();menu()
    else:print(vv.random.rand(d))
    menu()
def menu():
    global a;a+=1
    if a==5:print('Рекламная пауза:\n'+vv.randchose(mas_reklama))
    b=input('Выберете действие:\n1 - вывод ссылки.\n2 - конвертирование текста в символы.\n3 - конвертирование текста в слова.\n4 - тест на знание математики.\n5 - рандомное число.\n>>>')
    if b==''or vv.protect.str(b,'all'):an_idiot();menu()
    elif b<1or b>5:an_idiot();menu()
    elif b==1:poisk()
    elif b==2:chard()
    elif b==3:frases()
    elif b==4:m_test()
    elif b==5:rand()
menu()