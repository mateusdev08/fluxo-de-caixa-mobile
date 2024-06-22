import sqlite3 as con
import mysql.connector


def conectar_db():
    global conexao, cursor

    conexao = con.connect('db.sqlite3')
    cursor = conexao.cursor()


def desconectar_db():
    cursor.close()
    conexao.close()


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


def desconectar_mysql():
    cursor_mysql.close()
    conexao_mysql.close()
