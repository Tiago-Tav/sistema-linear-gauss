from sistemaLinear import sistemaLinear

print()
tamanho = int(input("Escreva o tamanho da matriz: "))
sistema = sistemaLinear(tamanho)
if sistema.inserirLinhas():
    if sistema.determinante() != 0:
        sistema.operarSistema()
        print("\nMATRIZ ESCALONADA\n")
        sistema.printar()
        print()
        x = sistema.acharX()
        print("\nVALORES DE X\n")
        for i in range(len(x) - 1):
            print("x" + str(i+1) + "= " + str("{:.3f}".format(x[i])))
    else:
        print("O sistema é impossivel ou não é determinado!")


