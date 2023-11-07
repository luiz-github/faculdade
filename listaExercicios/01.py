dados = [1500, 3500, 3000, 500, 150, 150]  # lista dos votos em ordem
nomes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']


# função funcionando
def pct(x):  # faz a porcentagem rapidamente
    try:
        total = sum(dados)
        pct = (x*100)/total
        return pct
    except:
        return


def resultado(args):
    print('-------------------------------------------')
    print(f'{('Sistema Operacional'):<14}   {('Votos'):>9}   {('%'):>9}')
    print(f'{('-------------------'):<14}   {('------'):>10}   {('---'):>8}')
    for i in range(len(dados)):
        print(f'{nomes[i]:<14}   {dados[i]:>13}   {round(pct(dados[i])):>9}%')
    print('-------------------------------------------')
    print(f'{('Total'):<14}   {sum(dados):>13}')



def voto(dados, x):  # computar voto
    if x == 1:
        dados[0] = dados[0] + 1
    elif x == 2:
        dados[1] = dados[1] + 1
    elif x == 3:
        dados[2] = dados[2] + 1
    elif x == 4:
        dados[3] = dados[3] + 1
    elif x == 5:
        dados[4] = dados[4] + 1
    elif x == 6:
        dados[5] = dados[5] + 1
    elif x == 0:
        resultado(x)
        exit()
    else:
        return "Valor {} inválido".format(x)


# inicio do programa
while True:
    x = int(input("Qual o melhor Sistema Operacional para uso em servidores? digite:\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n0- Encerrar processo"))
    voto(dados, x)
