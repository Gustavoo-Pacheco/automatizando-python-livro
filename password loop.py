i = 0
while 10 > i:
    print("qual seu nome")
    name = input()
    if name != "Gustavo":
        continue
    print("Oi gustavo, Qual é a senha (uma raça de cachorro.)")
    passsword = input()
    if passsword == "golden":
        break
print("asseco liberado")