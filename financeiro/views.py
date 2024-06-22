from django.shortcuts import render, redirect, get_object_or_404
from financeiro.models import FLancamento
import financeiro.data_base as db
from django.contrib.auth.decorators import login_required
from financeiro.etl_sqlite_mysql_f_lancamentos import etl_dw

# Create your views here.


@login_required
def f_lancamento(request):
    classe = db.classe()
    grupo = db.grupo()
    natureza = db.natureza()
    centro_de_custo = db.centro_de_custo()
    movimentacao = db.movimentacao()
    conta = db.conta()
    cartao = db.cartao()
    status_movimento = db.status_movimento()
    forma_pagamento = db.forma_pagamento()

    return render(request, 'financeiro/f_lancamento_insert.html', {'classe': classe, 'grupo': grupo, 'natureza': natureza, 'centro_de_custo': centro_de_custo, 'movimentacao': movimentacao, 'conta': conta, 'cartao': cartao, 'status_movimento': status_movimento, 'forma_pagamento': forma_pagamento})


@login_required
def salvar_f_lancamento(request):
    classe = request.POST.get('classe')
    grupo = request.POST.get('grupo')
    natureza = request.POST.get('natureza')
    dt_movimento = request.POST.get('dt_movimento')
    dt_vencimento = request.POST.get('dt_vencimento')
    centro_de_custo = request.POST.get('centro_de_custo')
    movimentacao = request.POST.get('movimentacao')
    conta = request.POST.get('conta')
    cartao = request.POST.get('cartao')
    status_movimento = request.POST.get('status_movimento')
    forma_pagamento = request.POST.get('forma_pagamento')
    qtde_parcela = request.POST.get('qtde_parcela')
    valor = request.POST.get('valor')
    descricao = request.POST.get('descricao')

    db.insert_f_lancamento(classe, grupo, natureza, dt_movimento, dt_vencimento, centro_de_custo,
                           movimentacao, conta, cartao, status_movimento, forma_pagamento, qtde_parcela, valor, descricao)

    # etl_dw()

    return redirect('consultar_lancamentos')


@login_required
def consultar_lancamentos(request):
    # pesquisa = request.GET.get('pesquisa', None)
    conta = db.filtro_conta()
    cartao = db.filtro_cartao()
    natureza = db.filtro_natureza()
    busca_conta = request.GET.get('conta', None)
    busca_cartao = request.GET.get('cartao', None)
    busca_natureza = request.GET.get('natureza', None)

    # if pesquisa:
    #     lancamentos = FLancamento.objects.all()
    #     lancamentos = lancamentos.filter(cartao=pesquisa)
    if busca_conta or busca_cartao or busca_natureza:
        # lancamentos = FLancamento.objects.filter(
        #     dt_vencimento=busca_vencimento, conta=busca_conta, cartao=busca_cartao)
        lancamentos = FLancamento.objects.filter(
            conta=busca_conta) | FLancamento.objects.filter(
            cartao=busca_cartao) | FLancamento.objects.filter(
            natureza=busca_natureza)

    else:
        lancamentos = FLancamento.objects.all()

    return render(request, 'financeiro/f_lancamento_select.html', {'lancamentos': lancamentos, 'natureza': natureza, 'conta': conta, 'cartao': cartao})


@login_required
def editar_lancamento(request, lancamento_id):
    lancamento = get_object_or_404(FLancamento, pk=lancamento_id)

    context = {
        'classe': db.classe(),
        'grupo': db.grupo(),
        'natureza': db.natureza(),
        'centro_de_custo': db.centro_de_custo(),
        'movimentacao': db.movimentacao(),
        'conta': db.conta(),
        'cartao': db.cartao(),
        'status_movimento': db.status_movimento(),
        'forma_pagamento': db.forma_pagamento(),
        'lancamento': lancamento,
    }

    return render(request, 'financeiro/f_lancamento_update.html', context)


@login_required
def alterar_f_lancamento(request):
    classe = request.POST.get('classe')
    grupo = request.POST.get('grupo')
    natureza = request.POST.get('natureza')
    dt_movimento = request.POST.get('dt_movimento')
    dt_vencimento = request.POST.get('dt_vencimento')
    centro_de_custo = request.POST.get('centro_de_custo')
    movimentacao = request.POST.get('movimentacao')
    conta = request.POST.get('conta')
    cartao = request.POST.get('cartao')
    status_movimento = request.POST.get('status_movimento')
    forma_pagamento = request.POST.get('forma_pagamento')
    qtde_parcela = request.POST.get('qtde_parcela')
    parcela = request.POST.get('parcela')
    valor = request.POST.get('valor')
    valor_parcela = request.POST.get('valor_parcela')
    descricao = request.POST.get('descricao')

    # Obtendo o objeto FLancamento existente
    lancamento = get_object_or_404(
        FLancamento, pk=request.POST.get('lancamento_id'))

    # Atualizando os campos do objeto existente
    lancamento.classe = classe
    lancamento.grupo = grupo
    lancamento.natureza = natureza
    lancamento.dt_movimento = dt_movimento
    lancamento.dt_vencimento = dt_vencimento
    lancamento.centro_de_custo = centro_de_custo
    lancamento.movimentacao = movimentacao
    lancamento.conta = conta
    lancamento.cartao = cartao
    lancamento.status_movimento = status_movimento
    lancamento.forma_pagamento = forma_pagamento
    lancamento.qtde_parcela = qtde_parcela
    lancamento.parcela = parcela
    lancamento.valor = valor
    lancamento.valor_parcela = valor_parcela
    lancamento.descricao = descricao

    # Salvando as alterações no banco de dados
    lancamento.save()
    etl_dw()

    return redirect('consultar_lancamentos')


@login_required
def deletar_f_lancamento(request, id):
    lancamento = get_object_or_404(FLancamento, pk=id)

    if request.method == 'POST':
        lancamento.delete()
        etl_dw()
        return redirect('consultar_lancamentos')

    return render(request, 'financeiro/f_lancamento_delete.html', {'deletar': lancamento})
