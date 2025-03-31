import numpy
class sistemaLinear:
    def __init__(self, tamanhoMatriz):
        self.matriz = [[0 for i in range(tamanhoMatriz + 1)] for j in range(tamanhoMatriz)]
    def inserirLinhas(self):
        if len(self.matriz) < 1:
            print("Você inseriu um numero invalido")
            return False
        print("Escreva as linhas assim como no exemplo -> Ex:1 3 2 5")
        i = 0
        while i < len(self.matriz):
            dados = input("Entre com os dados da " + str(i+ 1) + " linha: ").split(' ')
            j = 0
            parar = False
            while j < len(self.matriz) + 1:
                if len(dados) > len(self.matriz) + 1:
                    parar = True
                try:
                    self.matriz[i][j] = float(dados[j])
                except IndexError:
                    print("Você não colocou a quantidade de colunas correta, ela deve ser o tamanho da matriz + 1 (Variavel idependente)")
                    parar = True
                    break
                except ValueError:
                    parar = True
                    print("Você inseriu um dado inválido")
                    break
                j += 1
                if parar == True:
                    print("Você não colocou a quantidade de colunas correta, ela deve ser o tamanho da matriz + 1 (Variavel idependente)")
                    return False
            i += 1
        print("\nMATRIZ ORIGINAL\n")
        self.printar()
        return True
    def acharMultiplo(self, i, j):
        multiplo = float(self.matriz[i][j]) / float(self.matriz[j][j])
        return multiplo
    def operarLinha(self,operar, valor, operadora):
        i = 0
        operar = self.matriz[operar]
        operadora = self.matriz[operadora]
        while i < len(self.matriz[0]):
            operar[i] = round(operar[i] - valor * operadora[i], 4)
            i += 1
    def operarSistema(self):
        j = 0
        while j < len(self.matriz):
            i = 0
            while i <= len(self.matriz) - 1:
                if (self.matriz[i][j] != 0) and i > j:
                    self.operarLinha(i, self.acharMultiplo(i,j), j)
                i += 1
            j += 1
    def acharX(self):
        res = [0] * len(self.matriz) + [1]
        contadorRes = len(res) - 1
        linha = len(self.matriz) - 1
        while linha >= 0:
            soma = self.matriz[linha][-1]
            divisor = 0
            for j in range(len(self.matriz[linha]) - 1):
                if divisor == 0:
                    divisor = self.matriz[linha][j]
                else:
                    soma = soma - self.matriz[linha][j] * res[j]
            if divisor == 0:
                print("O sistema é impossivel ou não é determinado!")
                return None
            contadorRes -= 1
            res[contadorRes] = soma/divisor
            linha -= 1
        return res

    def determinante(self):
        analise = []
        for linha in self.matriz:
            analise.append(linha[:-1])
        return numpy.linalg.det(analise)

    def printar(self):
        for i in self.matriz:
            linha = ""
            for c in i:
                linha = linha + str(float("{:.3f}".format(c))) + ", "
            print(linha)

