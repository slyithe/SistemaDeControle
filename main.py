#Sistema de gerenciamento de estoque

class Produto:
  def __init__(self, id, nome, categoria_id, quantidade, preco):
   self.id = id
   self.nome = nome
   self.categoria_id = categoria_id
   self.quantidade = quantidade
   self.preco = preco

class categoria:
  def __init__(self,id,nome):
    self.id = id
    self.nome = nome

class movimentacao:
  def __init__(self,id,produto_id,quantidade, tipo_movimentacao,data):
    self.id = id
    self. produto_id = produto_id
    self. quantidade = quantidade
    self.tipo_movimentacao = tipo_movimentacao
    self.data = data

def cadastrar_produto(produtos,contador_produtos):
  id = contador_produtos + 1
  nome = input("nome do produto:")
  categoria_id = int(input("ID da categoria;"))
  quantidade = int(input("insira a quantidade"))
  preco = float(input("insira o preço"))
  produtos.append(Produto(id,nome,categoria_id,quantidade,preco))
  print("produto cadastrado com sucesso!")
  return contador_produtos + 1

def consultar_produto_id(produtos, id):
  for produto in produtos:
    if produto.id == id:
      print(f'id{produto,id}, nome:{produto.nome},categoria:{produto.categoria_id},quantidade:{produto.quantidade},preço:{produto.preco}')                           
#teste cadastro
produtos = []
contador = 0
contador = cadastrar_produtos(produtos, cpntador)

ask = int(input("qual o id deseja consultar: "))
consultar_produto_id(produtos, ask)


