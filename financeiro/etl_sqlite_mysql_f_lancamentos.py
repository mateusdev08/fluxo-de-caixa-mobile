import financeiro.data_base_etl as db
from time import time
from datetime import datetime


def etl_dw():
    tempo_inicio = time()

    db.conectar_db()
    tabela_oltp = db.cursor.execute(
        'select * from financeiro_flancamento;').fetchall()

    db.conectar_mysql()
    tabela_olap = '''
    create table if not exists f_lancamentos(
        id int not null,
        classe text not null,
        grupo text not null,
        natureza text not null,
        dt_movimento date not null,
        dt_vencimento date not null,
        centro_de_custo text not null,
        movimentacao text not null,
        conta text not null,
        cartao text not null,
        status_movimento text not null,
        forma_pagamento text not null,
        qtde_parcela int not null,
        parcela int null,
        valor decimal(9,2) not null,
        valor_parcela decimal(9,2) null,
        descricao text not null
    );'''

    db.cursor_mysql.execute(tabela_olap)
    db.cursor_mysql.execute('truncate table f_lancamentos;')

    print('=' * 50)
    print('ETL iniciado, aguarde...')
    print('=' * 50)

    registros = 0
    for item in tabela_oltp:
        id = item[0]
        classe_tratada = item[1]
        classe_i = classe_tratada.find('-')
        classe = classe_tratada[classe_i + 1:]
        grupo_tratado = item[2]
        grupo_i = grupo_tratado.find('-')
        grupo = grupo_tratado[grupo_i + 1:]
        natureza_tratada = item[3]
        natureza_i = natureza_tratada.find('-')
        natureza = natureza_tratada[natureza_i + 1:]
        dt_movimento = item[4]
        dt_vencimento = item[5]
        centro_de_custo = item[6]
        movimentacao = item[7]
        conta = item[8]
        cartao = item[9]
        status_movimento = item[10]
        forma_pagamento = item[11]
        qtde_parcela = item[12]
        parcela = item[13]
        valor = item[14]
        valor_parcela = item[15]
        descricao = item[16]

        q_campos = '''insert into f_lancamentos(id, classe, grupo, natureza, dt_movimento, dt_vencimento, centro_de_custo, movimentacao, conta, cartao, status_movimento, forma_pagamento, qtde_parcela, parcela, valor, valor_parcela, descricao) values('''
        q_valores = f"{id}, '{classe}', '{grupo}', '{natureza}', '{dt_movimento}', '{dt_vencimento}', '{centro_de_custo}', '{movimentacao}', '{conta}', '{cartao}', '{status_movimento}', '{forma_pagamento}', {qtde_parcela}, {parcela}, {valor}, {valor_parcela}, '{descricao}');"
        q_insert = q_campos + q_valores

        db.cursor_mysql.execute(q_insert)
        db.conexao_mysql.commit()

        registros += 1

    db.desconectar_mysql()
    db.desconectar_db()

    tempo_final = time()
    tempo_total = tempo_final - tempo_inicio

    print(f"ETL finalizado com sucesso! Tempo em segundos: {tempo_total:.2f}")
    print(f"Quantidade de registro(s) carregado(s): {registros}")
    print('=' * 50)

    with open(r'.\log\log_flancamentos.log', 'a', encoding='UTF-8') as log_file:
        log_file.write(
            f"Data: {datetime.today()},ETL finalizado com sucesso! Tempo em segundos: {tempo_total:.2f},Quantidade de registro(s) carregado(s): {registros}\n")
