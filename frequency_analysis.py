from collections import defaultdict
import operator

normal_letter_proportion = {'A': 14.63,'B': 1.04,'C': 3.88,'D': 4.99,
'E': 12.57,'F': 1.02,'G': 1.30,'H': 1.28,'I': 6.18,
'J': 0.40,'K': 0.02,'L': 2.78,'M': 4.74,'N': 5.05,
'O': 10.73,'P': 2.52,'Q': 1.20,'R': 6.53,'S': 7.81,
'T': 4.34,'U': 4.63,'V': 1.67,'W': 0.01,'X': 0.21,'Y': 0.01, 'Z': 0.47,
}

file_name = input("Qual o nome do arquivo aberto?")
with open(file_name + ".txt", "r") as file: file_content = file.read()

total_letter_count = 0
letter_count = defaultdict(int)
letter_proportion = defaultdict(int)

for letter in file_content:
    if letter.isalnum and letter != "\n" and letter != '.' and letter != ',' and letter != ' ':
        total_letter_count += 1
        letter_count[letter] += 1

letter_proportion = {letter:(count/total_letter_count)*100 for letter, count in letter_count.items()}

initial_sorted_normal_letter_proportion = sorted(normal_letter_proportion.items(), key=operator.itemgetter(1))
sorted_letter_proportion = sorted(letter_proportion.items(), key=operator.itemgetter(1))
sorted_normal_letter_proportion = initial_sorted_normal_letter_proportion[7:]

print(sorted_letter_proportion)
print(sorted_normal_letter_proportion)

dicionario_associacoes = {}

for i in range(min(len(sorted_letter_proportion), len(sorted_normal_letter_proportion))):
    chave = sorted_letter_proportion[i][0]  # Obter a letra da primeira lista
    valor = sorted_normal_letter_proportion[i][0]  # Obter a letra da segunda lista
    dicionario_associacoes[chave] = valor

# Exibir o dicionário resultante
#print(dicionario_associacoes)


#association = {letter:normal_letter for (letter,x), (normal_letter,y) in (sorted_letter_proportion, sorted_normal_letter_proportion.items())}
#print(association)

#print(sorted_letter_proportion)


string_substituida = ''.join([dicionario_associacoes.get(letra, "*") for letra in file_content])
print(string_substituida)