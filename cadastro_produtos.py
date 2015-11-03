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



def escolher_moda():
    print('\n')
    print('*****************Menu Principal*****************')
    print('**                                            **')
    print('**         [1] Moda Masculina                 **')
    print('**         [2] Moda Feminina                  **')
    print('**         [3] Moda Masculina Infantil        **')
    print('**         [4] Moda Feminmina Infantil        **')
    print('**                                            **')
    print('************************************************')
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
    while True:
        entrada = input('Defina um ou uma {} para {}:'.format(nome,tipo))
        if entrada.isalpha():
            return entrada
        elif entrada.isdigit():
            print('Não digite  números')
        else:
            print('Só digite letras')

def validar_numeros(nome,tipo):
    while True:
        entrada = input('Defina um ou uma {} para {}:'.format(nome,tipo))
        if entrada.isdigit():
            return entrada
        elif entrada.isalpha():
            print('Não digite  letras')
        else:
            print('Só digite números')

def escolhermodamasculina():
    while True:
        print('Listando roupas')
        moda = Moda()
        for item in range(0,14,1):
            print('Cod {}: {}'.format(item,moda.masculina[item]))
        while True:
            cod = input('Escolha um código:')
            if cod.isdigit():
                cod = int(cod)
                if cod >= 0 and cod <=13:
                    cod = cod
                    roupa = moda.masculina[cod]
                    tamanho = validar_numeros('tamanho',roupa)
                    cor = validar_strings('cor',roupa)
                    marca = validar_strings('marca',roupa)
                    preco = validar_numeros('preço',roupa)
                    quantidade = validar_numeros('quantidade',roupa)
                    print('Roupa:{}\nCor:{}\nMarca:{}\nTamanho:{}\nPreço:R${}\nQuantidade:{}'.format(roupa,cor,marca,tamanho,preco,quantidade))
                    while True:
                        decisao = input('Quer cadastrar o item acima?[S/N]')
                        if decisao.isalpha():
                            if decisao in 'S' or decisao in 's':
                                cursor.execute(''' insert into modamasculina(roupa,tamanho,cor,marca,preco,quantidade) values(?,?,?,?,?,?)''',(roupa,tamanho,cor,marca,preco,quantidade))
                                conexao.commit()
                                print('CADASTRADO COM SUCESSO')
                                return escolher_moda()
                            elif decisao in 'N' or decisao in 'n':
                                return escolher_moda()
                            else:
                                print('Essa opção não existe')
                        elif decisao.isdigit():
                            print('Não pode conter digitos')
                elif cod <0 or cod >13:
                    print('Código inexistente')
            elif cod.isalpha:
                print('Não use letras')
            else:
                print('Só use dígitos')



escolher_moda()
