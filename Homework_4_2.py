flag = True
while flag:
    try:
        number_1 = float(input("Please type a number: "))
        number_2 = float(input("Please type another number: "))
        number_operator = input("Please choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n your answer?:")
        if number_operator == '1':
            result = number_1 + number_2
        elif number_operator == '2':
            result = number_1 - number_2
        elif number_operator == '3':
            result = number_1 * number_2
        elif number_operator == '4':
            result = number_1 / number_2
        else:
            result = "Not operator"
        print(result)
        next_or_stop = input("Choose:\n next \n stop \n your answer?:")
        if next_or_stop == "next":
            flag = True
        elif next_or_stop == "stop":
            flag = False
        else:
            print("Not operator to end or continue")
            flag = False
    except ValueError:
        print('Not number!')
    except ZeroDivisionError:
        print("Bad operator")
