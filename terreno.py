#receber as medidas de largura e comprimento de um terreno retangular(uma casa decimal)
#receber o valor do metro quadrado (duas casas decimais)
#calcular
#mostrar o valor da area do terreno, o preço do terreno(duas casas decimais)

#codigo basico

# largura_terreno = float(input("Digite a largura do terreno: "))
# comprimento_terreno = float(input("Digite o comprimento do terreno: "))
# valor_mquadrado = float(input("Digite o valor do metro quadrado: "))

# area_terreno = largura_terreno * comprimento_terreno
# preco_terreno = area_terreno * valor_mquadrado

# print(f"Area do terreno: {area_terreno:.2f}")
# print(f"Preço do terreno: {preco_terreno:.2f}")

#CODIGO AVANÇADO

def entrada_positiva(mensagem): #função para garantir que o usuario digite um valor numerico positivo
    while True: #usando o loop, consigo tratar erros e ainda retornar para o menu e novamente processar o codigo
        try: 
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Valor incorreto! Tente novamente.")
        except ValueError:
            print("Digite um numero valido.")    
                    
largura_terreno = entrada_positiva("Digite a largura do terreno: ")
comprimento_terreno = entrada_positiva("Digite o comprimento do terreno: ")
valor_mquadrado = entrada_positiva("Digite o valor do metro quadrado do terreno: ")

area_terreno = largura_terreno * comprimento_terreno
preco_terreno = area_terreno * valor_mquadrado

print(f"Area do terreno: {area_terreno:.1f}")
print(f"Preço do terreno: {preco_terreno:.2f}")
