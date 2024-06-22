import sqlite3 as con
from datetime import datetime, date


def conectar_db():
    global conexao, cursor

    conexao = con.connect('db.sqlite3')
    cursor = conexao.cursor()


def desconectar_db():
    cursor.close()
    conexao.close()


def classe():
    conectar_db()
    tb_classe = cursor.execute(
        "select cod_classe || '-' || classe as classe from plano_de_contas;").fetchall()
    desconectar_db()

    campos_classe = {'': ''}

    for item in tb_classe:
        campos_classe[item[0]] = item[0]

    return campos_classe


def grupo():
    conectar_db()
    tb_grupo = cursor.execute(
        "select cod_grupo || '-' || grupo as grupo from plano_de_contas;").fetchall()
    desconectar_db()

    campos_grupo = {'': ''}

    for item in tb_grupo:
        campos_grupo[item[0]] = item[0]

    return campos_grupo


def natureza():
    conectar_db()
    tb_natureza = cursor.execute(
        f"select cod_natureza || '-' || natureza as natureza from plano_de_contas;").fetchall()
    desconectar_db()

    campos_natureza = {'': ''}

    for item in tb_natureza:
        campos_natureza[item[0]] = item[0]

    return campos_natureza


def centro_de_custo():
    conectar_db()
    tb_centro_de_custo = cursor.execute(
        "select centro_de_custo from centro_de_custo;").fetchall()
    desconectar_db()

    campos_centro_de_custo = {'': ''}

    for item in tb_centro_de_custo:
        campos_centro_de_custo[item[0]] = item[0]

    return campos_centro_de_custo


def movimentacao():
    conectar_db()
    tb_movimentacao = cursor.execute(
        "select movimentacao from movimentacao;").fetchall()
    desconectar_db()

    campos_movimentacao = {'': ''}

    for item in tb_movimentacao:
        campos_movimentacao[item[0]] = item[0]

    return campos_movimentacao


def conta():
    conectar_db()
    tb_conta = cursor.execute(
        "select conta from conta;").fetchall()
    desconectar_db()

    campos_conta = {'': ''}

    for item in tb_conta:
        campos_conta[item[0]] = item[0]

    return campos_conta


def cartao():
    conectar_db()
    tb_cartao = cursor.execute(
        "select cartao from cartao;").fetchall()
    desconectar_db()

    campos_cartao = {'': ''}

    for item in tb_cartao:
        campos_cartao[item[0]] = item[0]

    return campos_cartao


def status_movimento():
    conectar_db()
    tb_status_movimento = cursor.execute(
        "select status_movimento from status_movimento;").fetchall()
    desconectar_db()

    campos_status_movimento = {'': ''}

    for item in tb_status_movimento:
        campos_status_movimento[item[0]] = item[0]

    return campos_status_movimento


def forma_pagamento():
    conectar_db()
    tb_forma_pagamento = cursor.execute(
        "select forma_pagamento from forma_pagamento;").fetchall()
    desconectar_db()

    campos_forma_pagamento = {'': ''}

    for item in tb_forma_pagamento:
        campos_forma_pagamento[item[0]] = item[0]

    return campos_forma_pagamento


def insert_f_lancamento(classe, grupo, natureza, dt_movimento, dt_vencimento, centro_de_custo, movimentacao, conta, cartao, status_movimento, forma_pagamento, qtde_parcela, valor, descricao):
    conectar_db()

    valor_parcela = float(valor) / int(qtde_parcela)

    data = datetime.strptime(dt_vencimento, "%Y-%m-%d")
    vencimento = date(data.year, data.month, data.day)
    dia = vencimento.day
    mes = vencimento.month
    ano = vencimento.year

    if int(qtde_parcela) > 1 and forma_pagamento == "Parcelado":
        parcela = 1
        while parcela <= int(qtde_parcela):
            campos_insert = '''INSERT INTO financeiro_flancamento(classe, grupo, natureza, dt_movimento, dt_vencimento, centro_de_custo, movimentacao, conta, cartao, status_movimento, forma_pagamento, qtde_parcela, parcela, valor, valor_parcela, descricao) values('''
            valores_insert = f"'{classe}', '{grupo}', '{natureza}', '{dt_movimento}', '{vencimento}', '{centro_de_custo}', '{movimentacao}', '{conta}', '{cartao}', '{status_movimento}', '{forma_pagamento}', {qtde_parcela}, {parcela}, {valor}, {valor_parcela}, '{descricao}');"
            query_insert = campos_insert + valores_insert

            cursor.execute(query_insert)
            conexao.commit()

            parcela += 1

            if mes == 12:
                mes = 1
                ano += 1
                vencimento = date(ano, mes, dia)

            else:
                mes += 1
                vencimento = date(ano, mes, dia)

    elif int(qtde_parcela) > 1 and forma_pagamento == "Recorrente":
        parcela = 1
        while parcela <= int(qtde_parcela):
            campos_insert = '''INSERT INTO financeiro_flancamento(classe, grupo, natureza, dt_movimento, dt_vencimento, centro_de_custo, movimentacao, conta, cartao, status_movimento, forma_pagamento, qtde_parcela, parcela, valor, valor_parcela, descricao) values('''
            valores_insert = f"'{classe}', '{grupo}', '{natureza}', '{dt_movimento}', '{vencimento}', '{centro_de_custo}', '{movimentacao}', '{conta}', '{cartao}', '{status_movimento}', '{forma_pagamento}', {qtde_parcela}, {parcela}, {valor}, {valor}, '{descricao}');"
            query_insert = campos_insert + valores_insert

            cursor.execute(query_insert)
            conexao.commit()

            parcela += 1

            if mes == 12:
                mes = 1
                ano += 1
                vencimento = date(ano, mes, dia)

            else:
                mes += 1
                vencimento = date(ano, mes, dia)

    elif forma_pagamento == "Repetir":
        parcela = 1
        while parcela <= int(qtde_parcela):
            campos_insert = '''INSERT INTO financeiro_flancamento(classe, grupo, natureza, dt_movimento, dt_vencimento, centro_de_custo, movimentacao, conta, cartao, status_movimento, forma_pagamento, qtde_parcela, parcela, valor, valor_parcela, descricao) values('''
            valores_insert = f"'{classe}', '{grupo}', '{natureza}', '{dt_movimento}', '{dt_vencimento}', '{centro_de_custo}', '{movimentacao}', '{conta}', '{cartao}', '{status_movimento}', 'À Vista', {1}, {1}, {valor}, {valor}, '{descricao}');"
            query_insert = campos_insert + valores_insert

            cursor.execute(query_insert)
            conexao.commit()

            parcela += 1

    else:
        campos_insert = '''INSERT INTO financeiro_flancamento(classe, grupo, natureza, dt_movimento, dt_vencimento, centro_de_custo, movimentacao, conta, cartao, status_movimento, forma_pagamento, qtde_parcela, parcela, valor, valor_parcela, descricao) values('''
        valores_insert = f"'{classe}', '{grupo}', '{natureza}', '{dt_movimento}', '{dt_vencimento}', '{centro_de_custo}', '{movimentacao}', '{conta}', '{cartao}', '{status_movimento}', '{forma_pagamento}', {qtde_parcela}, {qtde_parcela}, {valor}, {valor}, '{descricao}');"
        query_insert = campos_insert + valores_insert

        cursor.execute(query_insert)
        conexao.commit()

    desconectar_db()


def filtro_conta():
    conectar_db()
    col_conta = cursor.execute(
        "select distinct conta from financeiro_flancamento order by conta asc;").fetchall()
    desconectar_db()

    campos_conta = {'': ''}

    for item in col_conta:
        campos_conta[item[0]] = item[0]

    return campos_conta


def filtro_cartao():
    conectar_db()
    col_cartao = cursor.execute(
        "select distinct cartao from financeiro_flancamento order by cartao asc;").fetchall()
    desconectar_db()

    campos_cartao = {'': ''}

    for item in col_cartao:
        campos_cartao[item[0]] = item[0]

    return campos_cartao


def filtro_natureza():
    conectar_db()
    col_natureza = cursor.execute(
        "select distinct natureza from financeiro_flancamento order by natureza asc;").fetchall()
    desconectar_db()

    campos_natureza = {'': ''}

    for item in col_natureza:
        campos_natureza[item[0]] = item[0]

    return campos_natureza
