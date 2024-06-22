import sqlite3 as con
import mysql.connector


def conectar_db():
    global conexao, cursor

    conexao = con.connect(r'C:\Users\Winchester-PC\Desktop\fluxo-de-caixa-django\db.sqlite3')
    cursor = conexao.cursor()
    print('Con sqlite')


def desconectar_db():
    cursor.close()
    conexao.close()
    print('Desc sqlite')


def conectar_mysql():
    global conexao_mysql, cursor_mysql
    dados_mysql = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'So28954371@',
        'database': 'fluxo_de_caixa'
    }

    conexao_mysql = mysql.connector.connect(**dados_mysql)
    cursor_mysql = conexao_mysql.cursor()
    print('Con MySQQL')


def desconectar_mysql():
    cursor_mysql.close()
    conexao_mysql.close()
    print('Desc MySQL')


# conectar_db()
# desconectar_db()
# conectar_mysql()
# desconectar_mysql()
