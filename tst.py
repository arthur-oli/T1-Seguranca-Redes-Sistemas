from random import choice
def vernam_cipher(file_content):
    possible_key_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    binary_content = ""
    key_content = ""
    final_content = ""
    tmp_array = ""

    for letter in file_content:
        new_letter = letter
        random_letter = letter

        if letter.isalnum():
            new_letter = format(ord(letter), '07b')
            random_letter = format(ord(choice(possible_key_values)), '07b')
        
        binary_content += new_letter
        key_content += random_letter
    
    for bin_letter, key_letter in zip(binary_content, key_content):
        if bin_letter == "0" or bin_letter == "1": # Não precisa verificar ambos
            tmp_letter = str(int(bin_letter) ^ int(key_letter))
            tmp_array += tmp_letter
            if(len(tmp_array) == 7):
                final_letter = chr(int(tmp_array, 2))
                tmp_array = ""
                final_content+= final_letter

        else:
            final_content+=bin_letter

    return binary_content, key_content, final_content


file_name = input("Qual o nome do arquivo a ser aberto?")
option = input("Codificar (C) ou decodificar (D)?")

with open(file_name + ".txt", "r") as file: file_content = file.read()

if option == "C":
    binary_content, key_content, final_content = vernam_cipher(file_content)
    print("Binary:", binary_content)
    print("Key:", key_content)
    print("Final:", final_content)
    with open("chave.txt", "a") as f: f.write(key_content)