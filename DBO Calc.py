print ("DBO Calculator")

def decimal_into_binary(decimal_1):
    decimal=int(decimal_1)


    print("chosen Decimal: ",decimal, "..into Binary is: ",bin(decimal))

def decimal_into_octal(decimal_1):
    decimal=int(decimal_1)


    print("chosen Decimal: ",decimal, "..into Octal is: ",oct(decimal))

def decimal_into_hexadecimal(decimal_1):
    decimal=int(decimal_1)


    print("chosen Decimal: ",decimal, "..into Hex is: ",hex(decimal))


decimal_1=int(input("Enter decimal num: "))
decimal_into_binary(decimal_1)
decimal_into_octal(decimal_1)
decimal_into_hexadecimal(decimal_1)