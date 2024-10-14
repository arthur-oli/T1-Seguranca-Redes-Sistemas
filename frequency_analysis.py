from collections import defaultdict
import operator
from caesar import caesar
total_letter_count = 0
letter_count = defaultdict(int)
letter_proportion = defaultdict(int)
letter_displacement_count = defaultdict(int)
dicionario_associacoes = {}
character_sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

normal_letter_proportion = {'A': 14.63,'B': 1.04,'C': 3.88,'D': 4.99,
'E': 12.57,'F': 1.02,'G': 1.30,'H': 1.28,'I': 6.18,
'J': 0.40,'K': 0.02,'L': 2.78,'M': 4.74,'N': 5.05,
'O': 10.73,'P': 2.52,'Q': 1.20,'R': 6.53,'S': 7.81,
'T': 4.34,'U': 4.63,'V': 1.67,'W': 0.01,'X': 0.21,'Y': 0.01, 'Z': 0.47}

# Dict atualizado para letras minúsculas
# normal_letter_proportion = {'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99,
#  'e': 12.57, 'f': 1.02, 'g': 1.30, 'h': 1.28, 'i': 6.18,
#  'j': 0.40, 'k': 0.02, 'l': 2.78, 'm': 4.74, 'n': 5.05,
#  'o': 10.73, 'p': 2.52, 'q': 1.20, 'r': 6.53, 's': 7.81,
#  't': 4.34, 'u': 4.63, 'v': 1.67, 'w': 0.01, 'x': 0.21, 'y': 0.01, 'z': 0.47}

file_name = input("Qual o nome do arquivo a ser aberto? ")
with open(file_name + ".txt", "r") as file: file_content = file.read()

for letter in file_content:
    if letter.isalnum():
        total_letter_count += 1
        letter_count[letter] += 1

letter_proportion = {letter:(count/total_letter_count)*100 for letter, count in letter_count.items()}
sorted_normal_letter_proportion = sorted(normal_letter_proportion.items(), key=operator.itemgetter(1), reverse=True)
sorted_letter_proportion = sorted(letter_proportion.items(), key=operator.itemgetter(1), reverse=True)

for i in range(min(len(sorted_letter_proportion), len(sorted_normal_letter_proportion))):
    chave = sorted_letter_proportion[i][0]
    valor = sorted_normal_letter_proportion[i][0]
    dicionario_associacoes[chave] = valor

for letter_coded, letter_original in dicionario_associacoes.items():
    letter_displacement_count[character_sequence.index(letter_coded) - character_sequence.index(letter_original)] += 1

max_key = max(letter_displacement_count, key=letter_displacement_count.get)
print("A cifra utilizada foi:", max_key)
print("Com essa cifra, a mensagem se torna:\n" + caesar(file_content, -max_key))