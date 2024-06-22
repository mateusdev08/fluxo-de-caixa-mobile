from django.urls import path
from financeiro.views import f_lancamento
from financeiro.views import salvar_f_lancamento
from financeiro.views import consultar_lancamentos
from financeiro.views import editar_lancamento
from financeiro.views import alterar_f_lancamento
from financeiro.views import deletar_f_lancamento

urlpatterns = [
    path('flancamento/', f_lancamento, name='f_lancamento'),
    path('salvarflancamento/', salvar_f_lancamento, name='salvar_f_lancamento'),
    path('lancamentos/', consultar_lancamentos, name='consultar_lancamentos'),
    path('editarlancamento/<int:lancamento_id>/',
         editar_lancamento, name='editar_lancamento'),
    path('alterarflancamento/', alterar_f_lancamento,
         name='alterar_f_lancamento'),
    path('deletarflancamento/<int:id>/', deletar_f_lancamento,
         name='deletar_f_lancamento'),
]
