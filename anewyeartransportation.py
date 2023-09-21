cellsnumber = int(input("Digite o numero de celulas: "))
findNumber = int(input("Digite o numero a ser encontrado: "))
ai = input("Digite os valores da celula: ").split()

aiNumbers = [int(x) for x in ai]

cells = [x for x in range(1, cellsnumber + 1)] 

for index, item in enumerate(cells):
    portal = aiNumbers[index] + item 
    if portal == findNumber:
        print("A soma de ", aiNumbers[index], " e ", item, " eh ", findNumber)
        break
    elif portal > findNumber:
        print("nao existe")
        break
    
