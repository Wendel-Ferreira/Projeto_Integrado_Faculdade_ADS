import random

class estoque:
    def __init__(self,nomeProduto,categoria):
        novoCodigo = random.sample(range(999999), k=1)
        self.codigo = novoCodigo
        self.produto = nomeProduto
        self.categoria = categoria

    def __str__(self):
        return f"Codigo {self.codigo}|Nome do produto: {self.produto} | Categoria: {self.categoria}"

estoqueCompleto = []

movimentaçãoEstoque = [] #No final adicionar esse Array em uma Tupla

def cadastrar_produto():
    nomeProduto = input("Qual nome do produto?")
    categoria = input("Qual categoria do produto?")
    novoProduto = estoque(nomeProduto,categoria)
    estoqueCompleto.append(novoProduto)
    print(f"O produto {nomeProduto} foi adicionado")

cadastrar_produto()

def exibirProdutos():
    for produto in estoqueCompleto:
        print(produto)

exibirProdutos()

#MONTAR UM INPUT COM VARIOS IF JÁ QUE PYTHON NÃO TEM SWICH

#Da pra fazer bonitinho |---------|