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

def validar_strings(nome,tipo):
    loop = True
    while loop:
        nome = input('Defina um ou uma {} para {}:'.format(nome,tipo))
        if nome.isalpha():
            nome = nome
            break
        elif nome.isdigit():
            print('Não digite  números')
        else:
            print('Só digite letras')

def validar_numeros(nome,tipo):
    loop = True
    while loop:
        nome = input('Defina um ou uma {} para {}:'.format(nome,tipo))
        if nome.isdigit():
            nome = nome
            break
        elif nome.isalpha():
            print('Não digite  letras')
        else:
            print('Só digite números')

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
        validar_numeros('tamanho',roupa)
        validar_strings('cor',roupa)
        validar_strings('marca',roupa)
        validar_numeros('preço',roupa)
        validar_numeros('quantidade',roupa)

        print('Roupa:{}\nCor:{}\nMarca:{}\nTamanho:{}\nPreço:R%:{}\nQuantidade:{}'.format(roupa,cor,marca,tamanho,preco,quantidade))
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
