produtos = {1:'arroz', 2:'batata'}
def add_produtos(c,n):
    produtos.update({c : n})

resp = 0

while resp != '4':
    print('[1] Adicionar ')
    print('[2] Consultar')
    print('[3] Deletar')
    print('[4] Sair')

    resp = input('Opção: ')

    if resp == '1':
        codigo = int(input('Qual o codigo do produto: '))
        nome = input('Nome do produto: ')
        add_produtos(codigo,nome)

    elif resp == '2':
        print(produtos)
    elif resp == '3':
        prod = input('Codigo do produto: ')
        del(produtos[int(prod)])
    elif resp == '4':
        print('Programa Finalizado!')