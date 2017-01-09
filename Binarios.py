class numero_binario:
    def calculo(self, num):
        self.lista_numeros=[]
        while num !=0:
            self.numero = num%2
            self.lista_numeros.append(self.numero)
            num = num/2

    def imprime(self):
        for i in reversed(self.lista_numeros):
            print i,
        print("\n")


