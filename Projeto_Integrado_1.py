import random

class Estoque:
    def __init__(self,codigo,nomeProduto,qnt, preco,categoria):
        self.codigo = codigo
        self.produto = nomeProduto
        self.categoria = categoria
        self.qnt = qnt
        self.preco = preco
        self.totalPreco = qnt * preco
        self.movimentacao = True #usar o bollean para intentificar a movimentação?

    def entradaQnt(self, qnt):
        self.qnt = self.qnt + qnt
    
    def saidaQnt(self,qnt):
        if qnt > self.qnt:
            print("*Quantidade de Retirada Invalida!*")
            print(f"Total em Estoque: {self.qnt}")
            print("\nDigite novamente o codigo do Produto")
            return editarEstoque()
        else:    
            self.qnt = self.qnt - qnt
            

    def modificarPreco(self, preco):
        self.preco = preco
    
    def __str__(self):
        return f"| Codigo: {self.codigo} | Nome do produto: {self.produto} | Categoria: {self.categoria} | Quantidade: {self.qnt} | Preço: {self.preco} | Preço Total: {self.totalPreco} no estoque |"

def editarEstoque(): #Essa função o cliente vai digitar o codigo e a quantidade que ele vai adicionar ou tirar do estoque, e caso ele queira alterar o valor do preço do produto
    codigo = pesquisaCodigo()
    for verificar in estoqueCompleto:
        if verificar.codigo == codigo: #Aparecer um Menu com adicionar,Tirar ou alterar o valor
           print(f"\nCódigo {codigo} encontrado")
           print(f"Nome do Produto: {verificar.produto}--Quantidade Atual: {verificar.qnt}---Preço atual: {verificar.preco}\n")
           print("Digite [1] Para cadastrar *Entrada* no Estoque")
           print("Digite [2] Para Cadastrar *Saida* no Estoque")
           print("Digite [0] Retornar para o *Menu*")
           decisao = int(input("Digite:"))
           if decisao == 1:
                entradaEstoque = int(input("Digite o Valor de entrada: "))

                valorAntigo = verificar.qnt #Da para usar essa variavel para historico? Testar

                verificar.entradaQnt(entradaEstoque)
                print(verificar) #Testar se essa logica funcionou e alterou na classe
           if decisao == 2:
                saidaEstoque = int(input("Digite o Valor de Saída: "))
                verificar.saidaQnt(saidaEstoque)
                print(verificar)
           if decisao == 0:
                return menu()
        else:
            print("Código não encontrado")

def menu():
    print("\nDigite [1] Cadastrar Novo Produto")
    print("Digite [2] Consultar Estoque Completo")
    print("Digite [3] Cadastrar Entrada ou Saída no estoque")
    print("Digite [4] Consulta pelo Código")
    print("Digite [5] Cunsulta pelo Nome do Produto")
    print("Digite [6] Visualizar Histórico de Movimentação")
    print("Digite [7] Editar Preço do Produto")# Precisa montar a Função dentro da class e fora
    print("Digite [8] Deletar Produto do Sistema")
    print("Digite [0] Para Finalizar o Programa\n")
    
    numero = int(input("Digite: "))
    if numero == 1:
       return cadastrar_produto()
    if numero == 2:
        return exibirTodosProdutos()
    if numero == 3:
       return editarEstoque()
    if numero == 4:
        return consultarProdutoCodigo()
    if numero == 5:
        return consultarProdutoNome()
    if numero == 6:
        return historicoMovimentacao()
    if numero == 7:
        return alterarPreco()
    if numero == 0:
        return print("Programa Finalizado")

estoqueCompleto = []

movimentacaoEstoque = [] #No final adicionar esse Array em uma Tupla

def cadastrar_produto(): 
    nomeProduto = input("Qual nome do produto? ")
    qnt = int(input("Quantidade : "))
    preco = float(input("Preço: "))
    categoria = input("Categoria do Produto: ")
    novoCodigo = random.sample(range(999999), k=1)[0] #Gerando código no momento de cadastrar um novo produto
    novoProduto = Estoque(novoCodigo,nomeProduto,qnt, preco,categoria)
    estoqueCompleto.append(novoProduto)
    print(f"\nCodigo gerado: {novoCodigo}, Nome do Produto: {nomeProduto} foi adicionado com sucesso!!\n")
    print("Digite [1] Adicionar outro Produto")
    print("Digite [0] Retornar ao Menu")
    cliente = int(input("Digite: "))
    if cliente == 1:
        return cadastrar_produto()
    if cliente == 0:
        return menu()

def retornarMenuOuFinalizar():
    print("\nDigite [0] Finalizar Programa")
    print("Digite [1] Retornar Menu")
    digito = int(input("Digite: "))
    if digito == 1:
        return menu()
    if digito == 0:
        return print("Programa finalizado")
    else:
        while digito != 0 or digito != 1:
            print("\n[ERRO] DIGITE NOVAMENTE [0] OU [1]\n")
            print("Digite [0] Finalizar Programa")
            print("Digite [1] Retornar Menu\n")
            digito = int(input("Digite: "))
            if digito == 1:
                return menu()
            if digito == 0:
                return print("Programa finalizado")
          
def exibirTodosProdutos():
    for produto in estoqueCompleto:
        print(produto)
    return retornarMenuOuFinalizar()
    
def pesquisaCodigo(): #Reutilizando metodo
    codigoDoProduto = int(input("Digite o Código: "))
    return codigoDoProduto

def consultarProdutoCodigo():
    codigo =  pesquisaCodigo()
    for produto in estoqueCompleto:
        if produto.codigo == codigo:
            print(produto,"\n")
            return retornarMenuOuFinalizar()
    else:
        print(f"\nO Produto com Código {codigo} não foi encontrado")
        return retornarMenuOuFinalizar()

def consultarProdutoNome():
    nomeProduto = input("Nome do Produto: ")
    for produto in estoqueCompleto:
        if produto.nome == nomeProduto:
            print(produto)
            return retornarMenuOuFinalizar()
    else:
        print(f"Não encontramos o Produto {produto}")
        return retornarMenuOuFinalizar()
       
def deletarProdutoEstoque():
    codigo = pesquisaCodigo()
    for produto in estoqueCompleto:
        if produto.codigo == codigo:
            print(f"\n{produto.nome} foi removido com Sucesso!")
            estoqueCompleto.remove(produto)
            return retornarMenuOuFinalizar()
    else:
       return print(f"O Produto com Código {codigo} não foi encontrado")

def historicoMovimentacao():
    print("PRECISA MONTAR A LOGICA") # Essa função vai pegar as movimentações no estoque. gerando um extrato de todo o processo de entrada e saida de produto, vou deixar uma forma igual extrato bancario mostrando positivo ou negativo no estoque, 
    #Dependendo implementarImport DATE e entender os principais metodos, mas precisa add esses metodos na funções de controle de estoque

def alterarPreco():
    codigo = pesquisaCodigo()
    for produto in estoqueCompleto:
        if codigo == produto.codigo:
            precoNovo = float(input("Digite o Novo Preço: "))
            precoAntigo = produto.preco
            produto.modificarPreco(precoNovo)
            print(f"Preço alterado! De {precoAntigo} Para {produto.preco}")
            return menu()
    else:
        print("Código não encontrado!")
        return menu()

menu()