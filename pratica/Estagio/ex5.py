string = input("Informe uma string: ")

invertida = ''
for caractere in range(len(string) - 1, -1, -1):
    invertida += string[caractere]

print("String invertida:", invertida)
