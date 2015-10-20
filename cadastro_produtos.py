import sqlite3
conexao = sqlite3.connect('../Arquivos/database/produtos.db')
cursor = conexao.cursor()


def tabela():
    cursor.execute ('''create table if not exists modafeminina(
ID INTEGER NOT NULL PRIMARY KEY,
roupa VARCHAR(50) NOT NULL,
tamanho VARCHAR(50) NOT NULL,
cor VARCHAR(50) NOT NULL,
marca VARCHAR(50) NOT NULL,
preco INTEGER,
quantidade INTEGER )''')
    cursor.execute ('''create table if not exists modamasculina(
ID INTEGER NOT NULL PRIMARY KEY,
roupa VARCHAR(50) NOT NULL,
tamanho VARCHAR(50) NOT NULL,
cor VARCHAR(50) NOT NULL,
marca VARCHAR(50) NOT NULL,
preco INTEGER,
quantidade INTEGER)''')
    cursor.execute ('''create table if not exists modafemininainfantil(
ID INTEGER NOT NULL PRIMARY KEY,
roupa VARCHAR(50) NOT NULL,
tamanho VARCHAR(50) NOT NULL,
cor VARCHAR(50) NOT NULL,
marca VARCHAR(50) NOT NULL,
preco INTEGER NOT NULL,
quantidade INTEGER NOT NULL)''')
    cursor.execute ('''create table if not exists modamasculinainfantil(
ID INTEGER NOT NULL PRIMARY KEY,
roupa VARCHAR(50) NOT NULL,
tamanho VARCHAR(50) NOT NULL,
cor VARCHAR(50) NOT NULL,
marca VARCHAR(50) NOT NULL,
preco INTEGER NOT NULL,
quantidade INTEGER NOT NULL)''')

tabela()


class Moda:
    def __init__ (self):
        self.feminina = ['Blusas','Calça Jeans','Calças','Camisas','Casacos e Jaquetas',
                         'Lingerie','Malhas e Sueters','Moda Praia','Saias',
                         'Shorts','Vestidos','Moletom','Macaquinhos e Macacões',
                         'Plus Size','Pijamas e Camisolas','Meias',]
        self.masculina = ['Bermudas','Calças Casuais','Calças Jeans','Calças Sociais',
                      'Camisas','Camisetas','Casacos e Jaquetas','Malhas e Sueters',
                      'Ternos','Moletons','Underwear','Pijamas e Kits',
                      'Meias','Moda Praia','Plus Size']
        self.masculinainfantil =['Blusas e Camisas','Casacos e Jaquetas','Malhas e Suetes',
                      'Calças','Bermudas e Shorts','Macacão e Macaquinho','Conjunto',
                      'fantasias','Pijamas','Moda Praia','Meias','Underwear']
        self.femininainfantil = ['Blusas e Camisas','Casacos e Jaquetas','Malhas e Suetes',
                      'Calças','Bermudas e Shorts','Macacão e Macaquinho','Conjunto',
                      'fantasias','Pijamas','Moda Praia','Meias','Underwear',
                      'Enxoval','Jardineira e Salopete','Vestidos e Saias']
        self.idades = ['Bebes','Crianças','Adolescentes','Adultos']


def menu_principal():
    print('')
    print('########Menu Principal########')
    print('')
    print('[1] para moda masculina')
    print('[2] para moda feminina')
    print('[3] para moda masculina infantil')
    print('[4] para moda feminmina infantil')

def escolheremoda():
    loop = True
    while loop:
        selecionar = (input('Digite um número:'))
        if selecionar.isdigit():
            selecionar = int(selecionar)
            if selecionar == 1:
                escolhermodamasculina()
                break
            elif selecionar <=0 or selecionar >4:
                print('vcocê escolheu um numero incorreto')

        elif selecionar.isalpha():
            print('Não digite letras')

def escolhermodamasculina():
    loop = True
    while loop:
        print('Listando roupas')
        moda = Moda()
        for item in range(14):
            item += 1
            print('Cod %s: %s'%(item,moda.masculina[item]))
        cod = int(input('Escolha um código:'))
        roupa = moda.masculina[cod]
        tamanho = input('Digite um tamanho para o item [%s]:'%roupa)
        tamanho = tamanho
        cor = input('Digite uma cor para o item [%s]:'%roupa)
        cor = cor
        marca = input('Digite uma marca para o item[%s]'%roupa)
        marca = marca
        preco = float(input('Digite um preço para o item[%s]'%roupa))
        preco = preco
        quantidade = int(input('Digite uma quantidade em estoque para o item[%s]'%roupa))
        quantidade = quantidade
        print('Roupa:%s \nCor:%s \nMarca:%s \nTamanho:%s \nPreço: R$%1.2f \nQuantidade:%i'%(roupa,cor,marca,tamanho,preco,quantidade))
        loop = True
        while loop == True:
            decisao = input('Quer cadastrar o item acima?[S/N]')
            if decisao.isalpha():
                if decisao in 'S' or decisao in 's':
                    cursor.execute(''' insert into modamasculina(roupa,tamanho,cor,marca,preco,quantidade) values(?,?,?,?,?,?)''',(moda.roupas[cod],tamanho,cor,marca,preco,quantidade))
                    conexao.commit()
                    print('CADASTRADO COM SUCESSO')
                    menu_principal()
                    escolhemoda()
                elif decisao in 'N' or decisao in 'n':
                    menu_principal()
                    escolheremoda()
                else:
                    print('Essa opção não existe')
            elif decisao.isdigit():
                print('Não pode conter digitos')


menu_principal()
escolheremoda()
escolhermodamasculina()
