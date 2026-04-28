# if + raise -> define o que é inválido
# try + except -> define o que fazer quando o estado é inválido 

class PrecoInvalido(Exception):
    pass

def PlotaAtivos(ativo):
    print('ativo: ', ativo)


def calculandoPrecoAtivo(preco):
    quantidade = 10
    if preco < 0:
        raise PrecoInvalido('O preço não pode ser negativo') # esse estado é inválido segundo minha regra - fluxo forçado a parar
    return preco * quantidade
        # devidir o que fazer depois que um erro acontece, mostrar mensagem, pedir um novo input, retornar erro da API.

try:
    preco = int(input('coloque aqui o valor do preço que deseja'))
    ativo = calculandoPrecoAtivo(preco)
    PlotaAtivos(ativo)

except PrecoInvalido as e: # ok, deu erro — o que eu faço agora?
    print(e)

except ValueError:
    print('Digite um número válido')