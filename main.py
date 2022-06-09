while True:
    try:
        num1 = int(input("first number: "))
        num2 = int(input("second number: "))
    except ValueError:
        print("numbers only, try again")
        continue
    
    while True:
        znak = str(input("symbol: "))
        if znak in ('+', '-', '*', '/'):
            break
        print("only use the following symbols: +; -; *; /")
    else:
        continue


    while True:

            if (znak == "+"):
                vysledok = int(num1 + num2)
                print(num1, "+", num2, "sa rovna", vysledok)
            elif (znak == "-"):
                vysledok = int(num1 - num2)
                print(num1, "-", num2, "sa rovna", vysledok)
            elif (znak == "*"):
                vysledok = int(num1 * num2)
                print(num1, "*", num2, "sa rovna", vysledok)
            elif (znak == "/"):
                vysledok = int(num1 / num2)
                print(num1, "/", num2, "sa rovna", vysledok)

            opakovanie = str(input('do you wanna work with this result (y/n)?'))
            if opakovanie in ('y', 'n'):
                break
            print("invalid input.")
    if opakovanie == 'y':
        try:
            num2 = int(input("second number: "))
        except ValueError:
            print("numbers only, try again")
            continue
        while True:
                znak = str(input("symbol: "))
                if znak in ('+', '-', '*', '/'):
                    break
                print("only use the following symbols: +; -; *; /")
            
        if (znak == "+"):
            vysledok = int(vysledok + num2)
            print(num1, "+", num2, "sa rovna", vysledok)
        elif (znak == "-"):
            vysledok = int(vysledok - num2)
            print(num1, "-", num2, "sa rovna", vysledok)
        elif (znak == "*"):
            vysledok = int(vysledok * num2)
            print(num1, "*", num2, "sa rovna", vysledok)
        elif (znak == "/"):
            vysledok = int(vysledok / num2)
            print(num1, "/", num2, "sa rovna", vysledok)

    elif opakovanie == 'n':
       break
    

    while True:
            nove = str(input('chces novy priklad (y/n)? '))
            if nove in ('y', 'n'):
                break
            print("invalid input.")
    if nove == 'y':
        continue
    elif nove == 'n':
        break
        