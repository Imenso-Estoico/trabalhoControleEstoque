import time

def menu():
    while True:
        print("Escolha uma opção: \n1)Adicionar produto. \n2)Consultar produto. \n3)Retirar produto. \n4)Consultar histórico de entrada e saída. \n5)Sair do programa.\n>>",end="")
        try:
            return int(input())
        except:
            print("Use um comando válido.")


print("Bem vindo ao sistema de controle de estoque.")

try:
    inventory = open("estoque.txt","r")
    print("O arquivo do estoque foi alcançado com sucesso.")
    inventory.close()
except:
    print("O arquivo de estoque não foi encontrado.")
    inventory = open("estoque.txt","x")
    print("O arquivo de estoque foi criado com sucesso.")
    inventory.close()

try:
    log = open("historico.txt","r")
    print("O arquivo do histórico foi alcançado com sucesso.")
    log.close()
except:
    print("O arquivo de histórico não foi encontrado.")
    log = open("historico.txt","x")
    print("O arquivo de histórico foi criado com sucesso.")
    log.close()

while True:
    choice = menu()

    if choice == 1:
        keepGoing = True
        while keepGoing:
            print("Escreva o nome do produto a ser adicionado ao estoque: ")
            productNameInput = input()
            print(productNameInput)

            while True:
                print("Escreva a quantidade do produto a ser adicionado ao estoque: ")
                productNumberInput = input()
                if productNumberInput.isdigit() and int(productNumberInput) > 0:
                    print(productNumberInput)
                    break
                else:
                    print("Entrada inválida. Use números.")

            inventory = open("estoque.txt","a")
            inventory.write(productNameInput + " " + productNumberInput + "\n")

            print("Escreva o nome do responsável: ")
            actor = input()
            log = open("historico.txt","a")
            log.write(productNameInput + "+" + productNumberInput + " " + actor + " " + time.ctime() + "\n")

            print("Gostaria de adicionar outro produto? s/n.")
            keyInput = input()
            if keyInput == "n":
                break
    elif choice == 2:
        inventory = open("estoque.txt", "r")
        print("\nAtualmente no estoque: \n" + inventory.read())
        inventory.close()

    elif choice == 3:
        inventory = open("estoque.txt","r")
        lines = inventory.readlines()
        i = 1
        for line in lines:
            print(f'{i}){line}', end="")
            i += 1
        indexChoice = int(input("Escolha o produto\n>>")) - 1

    elif choice == 4:
        log = open("historico.txt", "r")
        print("\nHistórico: \n" + log.read())
        log.close()
    elif choice == 5:
        break
    else:
        print("Use um comando válido.")