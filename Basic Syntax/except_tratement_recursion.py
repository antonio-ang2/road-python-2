# tratativa de erro no backend (ou no código em geral).
# o usuário pode ficar sabendo se eu expor isso com um print, se eu der pass ele passa.

# RAISE -> isso aqui é um erro, trate como tal.
# EU TENHO DUAS FORMAS DE PENSAR AQUI -> DEIXAR O PYTHON DETECTAR O ERRO OU EU DETECTAR ANTES QUE OCORRA. prevenir ou reagir ao erro.
num = int(input('digite aqui por quanto quer dividir'))

# dicas: preciso usar recursão? 
# Aqui está o ponto-chave: o except NÃO é um loop. Ele é executado UMA VEZ quando o erro acontece. Então se você ficar dentro do except esperando se repetir magicamente... vai ficar esperando. Mas e se você colocar o try-except DENTRO de um loop?

# posso fazer por recursão, porém cada vez que eu chamo por recursão crio um novo nível na pilha de memória (call stack).

# mais eficiente: abrir múltiplas "cópias" da função na memória, ou reutilizar o mesmo bloco de código?

def Divisao(num):
    try:
        res = 100/num
        print('seu resultado é', res)
    except ZeroDivisionError:
        nume = int(input('zé, tá chapando seu numero deve ser outro'))
        Divisao(nume)


Divisao(num)