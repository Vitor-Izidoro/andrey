funcaoComposta = 0

print("=========================================")
print("f(x) = 2 * x")
print("g(x) = y + 5")
print("=========================================")

print("Qual das operações deseja realizar? ")
print("[1] - (g ° f)")
print("[2] - (g ° g)")
print("[3] - (f ° f)")
print("[4] - (f ° g)")
choice = int(input("operação: "))
print("=========================================")

if choice == 1:
    print("(g ° f)")

    x = int(input("Defina um valor para 'x' "))
    funcaoF = 2 * x
    y = funcaoF
    funcaoG = y + 5
    print(funcaoG)

elif choice == 2:
    print("(g ° g)")
    x = int(input("Defina um valor para 'x' "))
    funcaoG = x + 5
    y = funcaoG
    funcaoG = y + 5
    print(funcaoG)


elif choice == 3:
    print("(F   ° F)")
    x = int(input("Defina um valor para 'x' "))
    funcaoF = 2 * x
    y = funcaoF
    funcaoF = 2 * y
    print(funcaoF)

elif choice == 4:
    print("(f ° g)")
    x = int(input("Defina um valor para 'x' "))
    funcaoG = x + 5
    y = funcaoG
    funcaoF = 2 * y
    print(funcaoF)

else:
    print("ERROR!")