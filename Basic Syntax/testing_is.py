#is verifica se duas variáveis representam o mesmo endereço na memória;
# None, 0, e strings/listas/dicionários vazios todos retornam False.
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
if b is a:
    print("ocupam o mesmo endereço de memória")
elif b == a:
    print('verificada que possuem o mesmo valor')