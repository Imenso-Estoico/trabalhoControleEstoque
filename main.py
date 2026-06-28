import time #Função necessária para acessar o relógio do PC

def menu(): #Dá print na pergunta do menu
    while True:
        print("Escolha uma opção: \n1)Adicionar produto. \n2)Consultar produto. \n3)Retirar produto. \n4)Consultar histórico de entrada e saída. \n5)Sair do programa.\n>>",end="")
        try:
            return int(input())
        except:
            print("Use um comando válido.") #Tenta impedir comandos inválidos.


print("Bem vindo ao sistema de controle de estoque.")

#Estas próximas linhas buscam por pelos arquivos de texto. Caso não encontrem, elas criam por sí mesmas
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

#While infinito a menos que se escolhar sair.
while True:
    choice = menu()

    #Escolha de adicionar item.
    if choice == 1:
        keepGoing = True
        while keepGoing:
            print("Escreva o nome do produto a ser adicionado ao estoque: ")
            productNameInput = input()
            print(productNameInput)

            #Só para se receber dado adequado
            while True:
                print("Escreva a quantidade do produto a ser adicionado ao estoque: ")
                productNumberInput = input()
                if productNumberInput.isdigit() and int(productNumberInput) > 0:
                    print(productNumberInput)
                    break
                else:
                    print("Entrada inválida. Use números.")

            #Salva o progresso no txt estoque
            inventory = open("estoque.txt","a")
            inventory.write(productNameInput + " " + productNumberInput + "\n")

            #Salva as ações no txt histórico
            print("Escreva o nome do responsável: ")
            actor = input()
            log = open("historico.txt","a")
            log.write(productNameInput + " +" + productNumberInput + " " + actor + " " + time.ctime() + "\n")

            print("Gostaria de adicionar outro produto? s/n.")
            keyInput = input()
            if keyInput == "n":
                break

    #Simplesmente lê o txt estoque
    elif choice == 2:
        inventory = open("estoque.txt", "r")
        print("\nAtualmente no estoque: \n" + inventory.read())
        inventory.close()

    #A mais trabalhosa
    elif choice == 3:
        inventory = open("estoque.txt","r")
        lines = inventory.readlines()
        i = 1

        #Lista as opções com um número indicados antes
        for line in lines:
            print(f'{i}){line}', end="")
            i += 1

        indexChoice = int(input("\nEscolha o produto\n>>")) - 1

        #Se válido, escolhe a linha e a decompõe
        if 0 < indexChoice +1 <= len(lines):
            productData = lines[indexChoice].strip().split()
            nameProduct = productData[0]
            currentQuantity = productData[1]

            numberRemove = int(input("Informe a quantidade de unidades a ser removida.\n>>"))

            #Escolhe como lidar com a remoção baseado na diferença do que há no estoque e no que foi pedido
            if numberRemove < int(currentQuantity):
                lines[indexChoice] = f'{nameProduct} {int(currentQuantity) - numberRemove}\n'
                print(lines[indexChoice])
                print("Escreva o nome do responsável: ")
                actor = input()
                log = open("historico.txt", "a")
                log.write(f'{nameProduct} -{numberRemove} {actor} {time.ctime()}\n')
            elif numberRemove == int(currentQuantity):
                lines.pop(indexChoice)
                print("Escreva o nome do responsável: ")
                actor = input()
                log = open("historico.txt", "a")
                log.write(f'{nameProduct} -{numberRemove} {actor} {time.ctime()}\n')
            else:
                print("Quantidade inválida")

            #Salva o progresso
            inventory = open("estoque.txt", "w")
            inventory.writelines(lines)
        else:
            print("Escolha inválida")


    #Simplesmente lê o txt historico
    elif choice == 4:
        log = open("historico.txt", "r")
        print("\nHistórico: \n" + log.read())
        log.close()

    #Acaba o loop e o código
    elif choice == 5:
        break

    #Tenta evitar entrada inválida
    else:
        print("Use um comando válido.")