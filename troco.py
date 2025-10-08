#usuario digita a quantidade comprada
#preco definido por produto
#usuario digita o valor em dinheiro para pagar(sendo a mais ou a menos)
#computador recebe
#computador calcula: quantidade, preço da unidade e dinheiro recebido
#computador calcula
#computador devolve se houver troco ou solicita a mais se estiver faltando

def entrada_positiva(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Numero invalido! Tente novamente.")
        except ValueError:
            print("Valor não reconhecido! Tente novamente.")
            
precos = {
    "Produto1": 10.0,
    "Produto2": 15.0,
    "Produto3": 35.0,
    "Produto4": 49.90
}

carrinho = [] #inicia a lista vazia antes de tudo, importante

while True:
    print("Passe no leitor, os produtos do cliente.")
    print("1 - Produto1")
    print("2 - Produto2")
    print("3 - Produto3")
    print("4 - Produto4")
    
    produto_lista = input("Digite o numero do produto:").strip()
    
    if produto_lista not in precos:
        print("Opção invalida! Tente novamente.")
        continue
    
    preco_produto = precos[produto_lista] #junta os dois, tipo concatenar
    print(f"Preço do produto selecionado: R$ {preco_produto:.2f}")
    
    quantidade = entrada_positiva("Digite a quantidade que deseja comprar do produto: ")
    print()
    total_carrinho = quantidade * preco_produto
    
    carrinho.append((produto_lista, quantidade, total_carrinho)) #juntando tupla e lista
    
    continuar = input("Gostaria de adicionar outro produto? (S/N):").strip().lower()
    if continuar == "s":
        continue
    else:
        print("Carrinho fechado! Realizando a soma dos itens.")
        valor_total = sum(item[2] for item in carrinho)
    print()
    print("Itens no carrinho: ")
    for item in carrinho: 
        codigo, qtd, subtotal = item
        print(f"Produto {codigo} | Quantidade: {qtd} | Subtotal: R${subtotal:.2f}")
    
    print()
    print(f"Valor total da compra: {valor_total:.2f}")
    print()
    
    while True:
        dinheiro_cliente = entrada_positiva("Dinheiro recebido do cliente:")
        troco_cliente = dinheiro_cliente - valor_total
        
        if troco_cliente >= 0:
            print(f"Troco a ser devolvido: R${troco_cliente:.2f}")
            break
        elif troco_cliente == 0:
            print("Não há troco!")
            break
        else:
            print(f"Faltam R${abs(troco_cliente):.2f} para completar a compra.")
    exit()

            
    

    
    
    
    
    
    

