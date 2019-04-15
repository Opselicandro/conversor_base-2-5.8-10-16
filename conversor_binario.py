import os
#encode utf-8

lista_opcoes= (2, 5, 8, 10,16, 'S','s', 'sair', 'Sair')
pentadecimal = (0, 1, 2, 3, 4)
hexadecimal = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A','B', 'C', 'D', 'E', 'F')
A = 'A'
B = 'B'
C = 'C'
D = 'D'
F = 'F'
E = 'E'
s = 's'
#base5 hexadecimal
def base5_hexa(j):
    s = base5_decimal(j)
    z = int_hex(s)
    return  z
#base5 para octal
def base5_octal(j):
    s = base5_decimal(j)
    z = int_octal(s)
    return  z
#base5 binario
def base5_binario(j):
    s = base5_decimal(j)
    z = funcao_base2(s)
    return z
#recebe a base5 e retorna um decimal
def base5_decimal(j):
    n = str(j)
    s = list(n)
    d = 0
    convertido = 0
    t = len(s)
    t -= 1
    while True:
        for i in s:
            c = int(i) * (pow(5, t))
            convertido += int(c)
            t -= 1
            d += 1
            if t < 0:
                break
        return convertido

#hexadecimal para binario
def hexa_octal(j):
    s = hexa_int(j)
    z = int_octal(s)
    return z
# hexadecimal para binario
def hexa_binario(j):
    s =hexa_int(j)
    z = funcao_base2(s)
    return z
#hexadecimal para decimal; /// ja tenho um funcao pronta mas por alguma razao, creio que  por "encode" nao roda..
def hexa_base5(j):
    s = funcao_base16(j)
    z = int_base5(s)
    return z
#binario para octal
def binario_octal(j):
    s = binario_decimal(j)
    z = int_octal(s)
    return s
#binario para base5
def binario_base5(j):
    s = binario_decimal(j)
    z = int_base5(s)
    return z

#recebe um binario retorna hexa
def binario_hexa(j):
   s = binario_decimal(j)
   d = int_hex(s)
   return  d
#recebe binario retorna decimal
def binario_decimal(j):
    s = int(str(j), 2)
    return s

# inicio da funcao de base 2. esta funca recebe um decimal e retorna um binario
def funcao_base2(j):
    binario = ""
    while True:
        s = (j % 2)
        str(s)
        binario = str(binario) + str(s)
        j = j // 2
        if j == 0:
            break
    binario = binario[::-1]
    binario = int(binario)
    return binario

#recebe inteiro e retorn base 5
def int_base5(j):
    n = str(j)
    s = list(n)
    d = 0
    convertido = 0
    t = len(s)
    t -= 1
    while True:
        for i in s:
            c = int(i) * (pow(5, t))
            convertido += int(c)
            t -= 1
            d += 1
            if t < 0:
                break
        return convertido

 #recebe inteiro e retorna um octal
def int_octal(j):
    binario = ""
    while True:
        s = (j % 8)
        str(s)
        binario = str(binario) + str(s)
        j = j // 8
        if j == 0:
            break
    binario = binario[::-1]
    binario = int(binario)
    return binario

# inicio da funcao de conversao octal. recebe um octal e retorna um decimal
def funcao_base8 (j):
    n = str(j)
    s = list(n)
    d = 0
    convertido = 0
    t = len(s)
    t -= 1
    while True:
        for i in s:
            c = int(i) * (pow(8, t))
            convertido += int(c)
            t -= 1
            d += 1
            if t < 0:
                break
        return convertido

#inicio da funcao hexadecimal. recebe um hexadecimal retorna um decimal
def funcao_base16(j):
    n = str(j)
    s = list(n)
    t = len(s)
    d = 0
    c = 0
    convertido = 0
    t -= 1
    while True:
        for l in s:
            if l == A:
                c = 10 * (pow(16, t))
            if l == B:
                c = 11 * (pow(16, t))
            if l == C:
                c = 12 * (pow(16, t))
            if l == D:
                c = 13 * (pow(16, t))
            if l == E:
                c = 14 * (pow(16, t))
            if l == F:
                c = 15 * (pow(16, t))
            if l == str(1) or l == str(2) or l == str(3) or l == str(4) or l == str(5) or l == str(6) or l == str(7) or l == str(8) or  l == str(9):
                #h = int(l)
                c = int(l) * pow(16, t)
            convertido += c
            t -= 1
            d += 1
        if t < 0:
            break
    return convertido

#recebe um inteiro e retorna um hexadecimal
def hexa_int(j): #decimal para hexa
    s = str(j)
    x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F']
    hexalista = list(s) #passa para lista
    resultado = 0
    for pos, digit in enumerate(hexalista[-1::-1]):
        posicao = x.index(digit)
        resultado = (int(posicao) * (16**pos)) + resultado
    return(resultado)

def int_hex(j):
    s = hex(j)
    return s

# comeca a chamada de funcoes de conversao
escolha = ""
while True:
    print("\n\n")
    print ("====================================")
    print ("=========Conversor Unidades=========")
    print ("=================BASE===============\n")
    print ("Introduz um numero Binario=============> 2")
    print ("Introduz um numero Pentadecimal========> 5")
    print ("Introduz um numero Octal===============> 8")
    print ("Introduz um numero Decimal=============> 10")
    print ("Introduz um numero Hexadecimal=========> 16")
    print ("SAIR===================================> S")
    while escolha not in lista_opcoes:
        print("Digite um dos Valores acima!!!\n")
        for i in lista_opcoes:
            escolha = (input("Escolha a base que vai converter: "))
            if escolha in lista_opcoes and escolha == s:
                os.system(exit())
            x = input("Valor a converter: ")  # type: str
            valor = x
            if escolha == 10:

                print(valor, " Conversao para a base 2:  ", funcao_base2(valor))
                print(valor, " Conversao para a base 5:  ", int_base5(valor))
                print(valor, " Conversao para a base 8:  ", int_octal(valor))
                print(valor, " Conversao para a base 18: ", int_hex(valor))
                os.system("pause")

            elif escolha == 8:

                c = funcao_base8(valor)
                print(valor, " Conversao para a base  2: ", funcao_base2(c))
                print(valor, " Conversao para a base  5: ", int_base5(c))
                print(valor, " Conversao para a base 10: ", c)
                print(valor, " Conversao para a base 16: ", int_hex(c))
                os.system("pause")

            elif escolha == 2:

                print(valor, " Conversao para a base  5: ", binario_base5(valor))
                print(valor, " Conversao para a base  8: ", binario_octal(valor))
                print(valor, " Conversao para a base  10: ",binario_decimal(valor))
                print(valor, " Conversao para a base  16: ", binario_hexa(valor))
                os.system("pause")


            elif escolha == 16:

                print(valor, " Conversao na base  2: ", hexa_binario(valor))
                print(valor, " Conversao na base  5: ", hexa_base5(valor))
                print(valor, " Conversao na base  8: ", hexa_octal(valor))
                print(valor, " Conversao na base 10: ", hexa_int(valor))
                os.system("pause")

            elif escolha == 5:

                print(valor, " Conversao para a base  2: ", base5_binario(valor))
                print(valor, " Conversao para a base  8: ", base5_octal(valor))
                print(valor, " Conversao para a base 10: ", base5_decimal(valor))
                print(valor, " Conversao para a base 16: ", base5_hexa(valor))
                os.system("pause")
