while True:
    try:
        num1 = int(input("cislo jedna: "))
        num2 = int(input("cislo dva: "))
    except ValueError:
        print("napis cislo normalne ty kokot")
        continue
    
    while True:
        znak = str(input("znak: "))
        if znak in ('+', '-', '*', '/'):
            break
        print("len tieto znaky pouzivaj: +; -; *; /")
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

            opakovanie = str(input('chces s vysledkom este pracovat (y/n)?'))
            if opakovanie in ('y', 'n'):
                break
            print("invalid input.")
    if opakovanie == 'y':
        try:
            num2 = int(input("cislo dva: "))
        except ValueError:
            print("napis cislo normalne ty kokot")
            continue
        while True:
                znak = str(input("znak: "))
        
    if znak in ('+', '-', '*', '/'):
        break
    print("len tieto znaky pouzivaj: +; -; *; /")
    
    # elif opakovanie == 'n':
    #    break
    

    while True:
            nove = str(input('chces novy priklad (y/n)? '))
            if nove in ('y', 'n'):
                break
            print("invalid input.")
    if nove == 'y':
        continue
    elif nove == 'n':
        break
        