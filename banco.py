class ContaBancaria:
    def __init__(self, saldo_bancario):
        self.__saldo_bancario = saldo_bancario 
    def depositar(self,valor_deposito): 
        self.__saldo_bancario += valor_deposito
    def sacar(self,valor_sacar):
        self.__saldo_bancario -= valor_sacar

    def mostrar_saldo(self): #metodo fora da classe, sendo publico
        return f"Saldo atual: {self.__saldo_bancario}"
    
ContaBancaria1 = ContaBancaria(1500) 

opcao = input("Selecione uma das opções: \n1 - Mostrar saldo  \n2 - Sacar  \n3 - Depositar\n")

if opcao == "1":
    print(ContaBancaria1.mostrar_saldo())

elif opcao == "2":
    i = int(input("Quanto voce quer sacar:"))
    ContaBancaria1.sacar(i)
    print (f"Voce sacou R${i}")
    print (ContaBancaria1.mostrar_saldo())

elif opcao == "3":
    i = int(input("Quanto voce quer depositar:"))
    ContaBancaria1.depositar(i)
    print (f"Voce depositou R${i}")
    print (ContaBancaria1.mostrar_saldo())
    
else:
    print("Opcao invalida")
    
