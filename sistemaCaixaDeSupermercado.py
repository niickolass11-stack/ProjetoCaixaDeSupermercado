dictProdutosCadastrados: dict = {}
carrinhoDeCompras = {}

totalDaCompra: float = 0

def cadastrarProdutos():

    cadastroDeProduto = str(input("Informe o nome do produto que deseja cadastrar: ")).upper()
    valorProduto = float(input("Informe o valor do produto R$: "))

    dictProdutosCadastrados[cadastroDeProduto] = valorProduto
    print("Produto Cadastrado com sucesso.")

def verListaDeProdutos():
    
    print("Estoque de Produtos Disponiveis")
    for produtos in dictProdutosCadastrados:

        print(f"Produto: {produtos} - R$ {dictProdutosCadastrados[produtos]}")

def adicionarItenAoCarrinho():
    
    global totalDaCompra

    while True:
        
        totalDaCompra = 0
        
        escolherProduto = str(input("Informe o Produto que deseja ( --- DIGITE X PARA ENCERRAR A COMPRA --- ): ")).upper()

        if (escolherProduto) in dictProdutosCadastrados:

            preco = dictProdutosCadastrados[escolherProduto]
            
            carrinhoDeCompras[escolherProduto] = preco
            
            print("Produto adicionado ao carrinho de compras")

        elif escolherProduto == "X":
            
            for valor in carrinhoDeCompras.values():
            
                totalDaCompra = totalDaCompra + valor
            
            print(f"O valor Total da compra e R$ {totalDaCompra}\n")
            
                
            break
        
        else:

            print("Produto invalido")
        
def verCarrinho():

    print("Carrinho de Compras")
    
    for produto, valor in carrinhoDeCompras.items(): 
    
        print(f"Produto: {produto} - R$ {valor}")


def realizarPagamento():

    print(f"O valor total de sua compra e R$ {totalDaCompra}\n")
    
    formaDePagamento = str(input('''Selecione a forma de pagamento\n
                                    1 - Cartao de credito\n
                                    2 - Cartao de debito\n
                                    3 - Dinheiro\n
                                    4 - Pix\n
                                    --> ''')).upper()
    
    print("Compra Realizada com sucesso !!!")
    carrinhoDeCompras.clear()

def menuAdm():

    while True:
        
        opcao = str(input('''Selecione a opção\n
                        1 - Cadastrar Produtos\n
                        2 - Ver Produtos\n
                        0 - Sair\n
                        --> ''')).upper()

        match opcao:

            case "1":

                cadastrarProdutos()
            
            case "2":

                verListaDeProdutos()
            
            case "0":

                print("Encerrando...")
                break

            case _:
                print("Opção invalida")


def menuCliente():

    while True:

        opcao = str(input('''Selecione uma opçaõ\n
                            1 - Adicionar itens ao carrinho\n
                            2 - Ver Carrinho de compras\n
                            3 - Realizar Pagamento\n
                            X - Sair\n
                            --> ''')).upper()
        
        match opcao:

            case "1":
            
                adicionarItenAoCarrinho()

            case "2":

                verCarrinho()
            
            case "3":

                realizarPagamento()
                break
            
            case "X":

                print("Encerrando...")
                break
                
            case _:

                print("Opção Inválida...")
        
        
def login():


    while True:

        opcao = str(input('''Selecione uma opção\n
                            1 - ADM\n
                            2 - Cliente\n
                            X - Sair\n
                            --> ''')).upper()
        
        match opcao:

            case "1":

                menuAdm()
            
            case "2":

                menuCliente()
            
            case "X":

                print("Encerrando...")
                break
                
            case _:

                print("Opção Invalida")

login()
