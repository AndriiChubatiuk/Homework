# 1. Дано рядок.
#      a. виведіть третій символ цього рядка.
value = "qwerty"
print(value[2])
#      b. виведіть передостанній символ цього рядка.
value = "qwerty"
print(value[-2])
#      c. виведіть перші п'ять символів цього рядка.
value = "qwerty"
print(value[0:5])
#      d. виведіть весь рядок, крім двох останніх символів.
value = "qwerty123"
print(value[0:-2])
#      e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи)
#      з першого).
value = "qwerty123"
print(value[::2])
#      f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
value = "qwerty123"
print(value[1::2])
#      g. виведіть усі символи у зворотному порядку.
value = "qwerty123"
print(value[::-1])
#      h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
value = "qwerty123"
print(value[::-2])
#      i. виведіть довжину цього рядка.
value = "qwerty1231"
print(len(value))
#
# 2. Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів. Використовуйте для вирішення
# завдання функцію `count`
value = "Hello Hello Hello"
c = value.count("Hello")
print(c)

# 3. Користувач вводить окремо рядок `s` та один символ `ch`. Необхідно здійснити пошук у рядку `s` всіх символів `ch`.
# Для вирішення можна використовувати тільки функцію `find` (rfind), оператори `if` та `for` (while).
s = input("Input 1: ")
ch = input("Input 2: ")
count = 0
flag = True
while flag:
    x = s.find(ch, count)
    if x == -1:
        flag = False
    else:
        print(x)
        count = x + 1
#
# 11. Дано рядок. Замініть у цьому рядку всі появи літери `h` на літеру `H`, крім першого та останнього входження.
value = "ah12345ha"
x = value[1:-1]
x1 = value[0]
x2 =  value[-1]
value2 = x.replace("h", "H")
print(x1+value2+x2)


