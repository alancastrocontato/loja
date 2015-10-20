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


class Modafeminina:
    def __init__ (self):
        self.roupas = ['Blusas','Calça Jeans','Calças','Camisas','Casacos e Jaquetas',
                         'Lingerie','Malhas e Sueters','Moda Praia','Saias',
                         'Shorts','Vestidos','Moletom','Macaquinhos e Macacões',
                         'Plus Size','Pijamas e Camisolas','Meias',]

class Modamasculina:
    def __init__ (self):
        self.roupas = ['Bermudas','Calças Casuais','Calças Jeans','Calças Sociais',
                      'Camisas','Camisetas','Casacos e Jaquetas','Malhas e Sueters',
                      'Ternos','Moletons','Underwear','Pijamas e Kits',
                      'Meias','Moda Praia','Plus Size']


class Modamasculina_infantil:
    def __init__ (self):
        self.idades = ['Baby','Kids','Teens']
        self.roupas = ['Blusas e Camisas','Casacos e Jaquetas','Malhas e Suetes',
                      'Calças','Bermudas e Shorts','Macacão e Macaquinho','Conjunto',
                      'fantasias','Pijamas','Moda Praia','Meias','Underwear']


class Modafeminina_infantil:
     def __init__ (self):
         self.idade = ['Baby','Kids','Teens']
         self.roupas = ['Blusas e Camisas','Casacos e Jaquetas','Malhas e Suetes',
                      'Calças','Bermudas e Shorts','Macacão e Macaquinho','Conjunto',
                      'fantasias','Pijamas','Moda Praia','Meias','Underwear',
                      'Enxoval','Jardineira e Salopete','Vestidos e Saias']

def menu_principal():
    print('')
    print('########Menu Principal########')
    print('')
    print('[1] para moda masculina')
    print('[2] para moda feminina')
    print('[3] para moda masculina infantil')
    print('[4] para moda feminmina infantil')

def escolhemoda():
    loop = True
    while loop == True:
        escolhemoda = (input('Digite um número:'))
        if escolhemoda.isdigit():
            escolhemoda = int(escolhemoda)
            if escolhemoda == 1:
                escolhamodamasculina()
                break
            elif escolhemoda <=0 or escolhemoda >4:
                print('vc escolheu um numero incorreto')

        elif escolhemoda.isalpha():
            print('não digite letras')

def escolhamodamasculina():
    loop = True
    while loop == True:
        print('Listando roupas')
        moda = Modamasculina()
        for item in range(14):
            item += 1
            print('Cod %s: %s'%(item,moda.roupas[item]))
        cod = int(input('Escolha um código:'))
        roupa = moda.roupas[cod]
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
                    escolhemoda()
                else:
                    print('Essa opção não existe')
            elif decisao.isdigit():
                print('Não pode conter digitos')


menu_principal()
escolhemoda()
escolhamodamasculina()
