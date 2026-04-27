#  Flag sucesso: Começa como False. Quando a divisão funciona, vira True e o loop para
#  while not sucesso: Continua enquanto o código não funcionou
#  Sem recursão: Reutiliza o mesmo bloco de código, não cria novos níveis de memória
# num é reatribuído: Na linha do input, você atualiza num diretamente para a próxima iteração

# Stack Overflow é justamente isso! Quando você usa recursão, cada chamada da função ocupa um espaço na pilha de execução (call stack). Se você digitar 0 dez mil vezes

# Com while, isso não acontece porque você está reutilizando o mesmo espaço de memória. O loop simplesmente se repete dentro da mesma função, sem criar novos "níveis" na pilha.

num = int(input('digite aqui por quanto quer dividir'))

def Divisao(num):
    sucesso = False
    
    while not sucesso:
        try:
            res = 100/num
            print('seu resultado é', res)
            sucesso = True
        except ZeroDivisionError:
            num = int(input('zé, tá chapando seu numero deve ser outro: '))


Divisao(num)