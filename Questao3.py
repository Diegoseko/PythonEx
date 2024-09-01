print('Bem vindo a FOTOXEROX do Diego OSEKO')
pdig = 1.10
pico = 1.00
pipb = 0.40
pfot = 0.20
def escolha_servico():
    global servico
    while True:
        print('DIG - DIGITALIZACAO')
        print('ICO - IMPRESSAO COLORIDA')
        print('IPB - IMPRESSAO PRETO E BRANCO')
        print('FOT - FOTOCOPIA')
        servico = input('Escolha o serviço desejado: ')
    
        if (servico != 'dig' and servico != 'ico' and servico != 'ipb' and servico != 'fot'):
            print('Opcao inválida, tente novamente.')
            continue
        return servico
    
def num_pagina():
    global num
    global preco
    while True:
        try:
            num = float(input('Qual o numero de paginas?: '))
        except ValueError:
            print("Digite apenas numeros")
            continue
        if(servico == 'dig'):
            if(num >= 20000):
                print("Nao fazemos pedidos nesta quantidade")
                continue
            elif(num >= 20 and num < 200):
                preco = pdig*num
                preco = preco - (preco*0.15)
                return preco 
            elif(num >= 200 and num < 2000):
                preco = pdig*num
                preco = preco - (preco*0.20)
                return preco 
            elif(num >= 2000 and num < 20000):
                preco = pdig*num
                preco = preco - (preco*0.25)
                return preco 
            else:
                preco = pdig*num
                return preco
        elif(servico == 'ico'):
            if(num >= 20000):
                    print("Nao fazemos pedidos nesta quantidade")
                    continue
            elif(num >= 20 and num < 200):
                preco = pico*num
                preco = preco - (preco*0.15)
                return preco 
            elif(num >= 200 and num < 2000):
                preco = pico*num
                preco = preco - (preco*0.20)
                return preco 
            elif(num >= 2000 and num < 20000):
                preco = pico*num
                preco = preco - (preco*0.25)
                return preco 
            else:
                preco = pico*num
                return preco
        elif(servico == 'ipb'):
            if(num >= 20000):
                print("Nao fazemos pedidos nesta quantidade")
                continue
            elif(num >= 20 and num < 200):
                preco = pipb*num
                preco = preco - (preco*0.15)
                return preco 
            elif(num >= 200 and num < 2000):
                preco = pipb*num
                preco = preco - (preco*0.20)
                return preco 
            elif(num >= 2000 and num < 20000):
                preco = pipb*num
                preco = preco - (preco*0.25)
                return preco 
            else:
                preco = pipb*num
                return preco
        elif(servico == 'fot'):
            if(num >= 20000):
                    print("Nao fazemos pedidos nesta quantidade")
                    continue
            elif(num >= 20 and num < 200):
                preco = pfot*num
                preco = preco - (preco*0.15)
                return preco 
            elif(num >= 200 and num < 2000):
                preco = pfot*num
                preco = preco - (preco*0.20)
                return preco 
            elif(num >= 2000 and num < 20000):
                preco = pfot*num
                preco = preco - (preco*0.25)
                return preco 
            else:
                preco = pfot*num
                return preco

def servico_extra():
    global extra
    while True:
        print("Deseja adicionar mais algum serviço?")
        print('Encadernação Simples - 1')
        print('Encadernação Capa Dura - 2')
        print('Nao desejo mais nada - 0')
        optc = int(input(" "))
        if (optc == 1):
            extra = 15
            return extra
        elif(optc == 2):
            extra = 40
            return extra
        elif(optc == 0):
            extra = 0
            return extra
        else:
            print("Selecione uma opcao valida")
            continue

escolha_servico()
num_pagina()
servico_extra()
print(f'Total a Pagar: {preco + extra}')



