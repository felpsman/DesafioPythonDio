#Menu aprensentado pro usuario para ele saber quais sao as opcoes dele
print("Menu\n"
"Digite [D] para realizar deposito\n" #D de deposito
"Digite [S] para realizar saque\n" #S de saque
"Digite [E] para ver o extrato da conta\n" #E de extrato
"Digite [Q] caso queira sair do sistema") #Q de Quit, sair
acao=input("O que voce ira fazer: ").upper().strip()
#Valores inciais para auxiliarem na contagem do programa
numero_de_saques = 0 
extrato=0
contadorSaque=0
contadorDeposito=0
#Loop para realizar o armazenamento correto de cada acao do usuario
while(acao!='Q'):
    #Se for deposito, o numero sera armazenado a variavel extrato e a variavel contadoDeoposito ira somar 1 a ela mesma
    if(acao=='D'):
        deposito=float(input("Digite o valor em R$ que voce ira depositar:"))
        extrato+=deposito
        contadorDeposito=contadorDeposito+1
    #Se for saque, o valor de extrato sera o valor do deposito anterio menos o valor do saque realizado e a varaivevel contadorSaques ira somar 1  a ela mesma
    elif(acao=='S'):
        saque=float(input("Quanto voce gostaria de sacar: "))
        if(saque>500):
            print("Voce nao pode realizar Saques maiores que R$500,00")
        extrato=extrato-saque
        contadorSaque=contadorSaque+1
    #Se o contador de saque chegar a 3, quer dizer que voce ja relizou o maximo de saque do dia
        if(contadorSaque==3):
            print("Voce ja realizou o maximo de saques por hoje, espere ate amanha para conseguir sacar mais ")
        if(saque>extrato or extrato==0):
            print("Voce nao pode sacar uma quantia que voce nao tem!")
    #Se for extrato, mostrara o extrato da sua conta e quantas vezes ouve depositos e saques da sua conta
    elif(acao=='E'):
        if(contadorDeposito==0):
            print("Nao foram realizadas movimentacoes na sua conta")
        else:
            print(f"O saldo da sua conta eh de R$: {extrato}")
            print(f"Voce realizou {contadorDeposito} depositos")
            print(f"Voce realizou {contadorSaque} saques")
    else:
        print("Opcao invalida, digite alguma opcao de acao valida, por favor!")
    acao=input("O que voce ira fazer: ").upper().strip()
    #Se for Saida, voce ira encerrar o programa e o programa ira ser encerrado
if(acao=="Q"):
    print("Voce escolheu encerrar o sistema!")

