# Ele é a única instância do tipo NoneType
# Representa a ausência de valor (tipo um “nada”, mas com significado definido)
#É um singleton (só existe um None em todo o programa)

# quando aparece: Funções que não retornam nada retornam None por padrão, Usado para inicializar variáveis sem valor ainda
# EXEMPLO:
#def foo():
#   pass
#print(foo())  # None

# formas de comparar objetos com python:
# x is None -> isso é literalmente o mesmo objeto None?

## x == None -> isso é considerado igual a None? -> CHAMA O MÉTODO __EQ__ POR ISSO DÁ ERRO.

# o próprio objeto decide o que é “igual”

# dunder_methods

class Troll:
    def __eq__(self, other):
        return True  # sempre diz que é igual

peso_usuario = Troll()
peso_setado = None

def calculoPeso(peso_usuario, peso_setado):
    if peso_usuario == peso_setado:
        print('deu certo') # deu certo mesmo setando para dar errado porque eu sobrescrevi a forma como o objeto define igualdade.
    else:
        print('deu tudo errado')

calculoPeso(peso_usuario, peso_setado)