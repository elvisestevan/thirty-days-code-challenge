# Enter your code here. Read input from STDIN. Print output to STDOUT

n_palavras = int(input())
palavras = []

for i in range(n_palavras):
    palavras.append(input())
    
for palavra in palavras:
    tamanho_palavra = len(palavra)
    i = 0
    palavra_par = ""
    palavra_impar = ""
    while i < tamanho_palavra:        
        if (i % 2 > 0):
            palavra_impar = palavra_impar + palavra[i]
        else:
            palavra_par = palavra_par + palavra[i]
        i += 1
    print(palavra_par + " " + palavra_impar)


