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

    def __str__(self):
        return f"| Codigo: {self.codigo} | Nome do produto: {self.produto} | Categoria: {self.categoria} | Quantidade: {self.qnt} | Preço: {self.preco} | Preço Total: {self.totalPreco} no estoque |"

def menu():
    print("\nDigite [1] Cadastrar Novo Produto")
    print("Digite [2] Consultar Estoque Completo")
    print("Digite [3] Cadastrar Entrada ou Saída no estoque")
    print("Digite [4] Consulta pelo Código")
    print("Digite [5] Cunsulta pelo Nome do Produto")
    print("Digite [6] Visualizar Histórico de Movimentação")
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
    
    #PRECISO MONTAR A FUNÇÃO DE HISTORICO DE MOVIMENTAÇÃO digito 6
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
    print(f"\nCodigo gerado: {novoCodigo}, Nome do Produto: {nomeProduto} foi adicionado com sucesso!!")
    return retornarMenuOuFinalizar()


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

def editarEstoque(): #Essa função o cliente vai digitar o codigo e a quantidade que ele vai adicionar ou tirar do estoque, e caso ele queira alterar o valor do preço do produto
    codigo = pesquisaCodigo()
    for verificar in estoqueCompleto:
        if verificar.codigo == codigo: #Aparecer um Menu com adicionar,Tirar ou alterar o valor
            print("Código encontrado")
        else:
            print("Código não encontrado")

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

menu()
#MONTAR UM INPUT COM VARIOS IF JÁ QUE PYTHON NÃO TEM SWICH

#Da pra fazer bonitinho |---------|