import random

class estoque:
    def __init__(self,nomeProduto,qnt, preco,categoria):
        novoCodigo = random.sample(range(999999), k=1)
        self.codigo = novoCodigo
        self.produto = nomeProduto
        self.categoria = categoria
        self.qnt = qnt
        self.preco = preco
        self.totalPreco = qnt * preco
        self.movimentacao = True #usar o bollean para intentificar a movimentação?

    def __str__(self):
        return f"| Codigo: {self.codigo} | Nome do produto: {self.produto} | Categoria: {self.categoria} | Quantidade: {self.qnt} | Preço: {self.preco} | Preço Total: {self.totalPreco} |"

print("Digite [1] Cadastrar")
print("Digite [2] Exibir todos os Produtos")
print("Digite [3] Alterar a Quantidade de Produto pelo Código") #Preciso pensar como fazer essa função
print("Digite [4] Consultar pelo Código")
print("Digite [5] Cunsultar pelo Nome do Produto")
print("Digite [6] ")
menu = int(input(""))

estoqueCompleto = []

movimentacaoEstoque = [] #No final adicionar esse Array em uma Tupla

def cadastrar_produto():
    nomeProduto = input("Qual nome do produto? ")
    qnt = int(input("Quantidade : "))
    preco = float(input("Preço: "))
    categoria = input("Categoria do Produto: ")
    novoProduto = estoque(nomeProduto,qnt, preco,categoria)
    estoqueCompleto.append(novoProduto)
    print(f"O produto {nomeProduto} foi adicionado ao estoque")


def exibirProdutos():
    for produto in estoqueCompleto:
        print(produto)


#MONTAR UM INPUT COM VARIOS IF JÁ QUE PYTHON NÃO TEM SWICH

#Da pra fazer bonitinho |---------|