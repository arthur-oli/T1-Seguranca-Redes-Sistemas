def caesar(s, k): a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"; return "".join((a[(a.index(c) + k) % len(a)] if c in a else c) for c in __import__("unicodedata").normalize("NFD", s) if __import__("unicodedata").category(c) != "Mn")
file_to_cypher, cypher_value = input("Qual o nome do arquivo aberto?"), int(input("Quanto será o deslocamento da cifra? (Positivo ou negativo)"))
with open(file_to_cypher + ".txt", "r") as file: file_content = file.read()
print(caesar(file_content, cypher_value))