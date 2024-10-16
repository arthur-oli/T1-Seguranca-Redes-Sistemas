from random import choice

def vernam_decipher(cypher_content, key_content):
    if len(cypher_content) != len(key_content):
        print("Tamanho do arquivo não corresponde ao tamanho da chave.")
        return False
    
    binary_cypher_content = ""
    binary_key_content = ""
    final_content = ""
    tmp_array = ""

    for letter_cypher, letter_key in zip(cypher_content, key_content):
        new_cypher_letter = letter_cypher
        new_key_letter = letter_key

        if letter_key.isalnum():
            new_cypher_letter = format(ord(letter_cypher), '07b')
            new_key_letter = format(ord(letter_key), '07b')

        binary_cypher_content += new_cypher_letter
        binary_key_content += new_key_letter
    
    for number_cypher, number_key in zip(binary_cypher_content, binary_key_content):
        if number_key == "0" or number_key == "1" and number_cypher == "0" or number_cypher == "1":
            if number_cypher == number_key:
                tmp_array += "0"
            
            else:
                tmp_array += "1"
            
            if len(tmp_array) == 7:
                final_content += chr(int(tmp_array, 2))
                tmp_array = ""
        
        else:
            final_content += number_key

    return final_content

def vernam_cipher(file_content):
    possible_key_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    binary_content = ""
    key_content = ""
    key_binary_content = ""
    final_content = ""
    tmp_array = ""

    for letter in file_content:
        new_letter = letter
        random_letter = letter
        random_binary_letter = letter

        if letter.isalnum():
            new_letter = format(ord(letter), '07b')
            random_binary_letter = format(ord(choice(possible_key_values)), '07b')
            random_letter = chr(int(random_binary_letter, 2))
        
        binary_content += new_letter
        key_binary_content += random_binary_letter
        key_content += random_letter
    
    for bin_letter, key_letter in zip(binary_content, key_binary_content):
        if bin_letter == "0" or bin_letter == "1": # Não precisa verificar ambos
            tmp_letter = str(int(bin_letter) ^ int(key_letter))
            tmp_array += tmp_letter
            if(len(tmp_array) == 7):
                final_content+= chr(int(tmp_array, 2))
                tmp_array = ""


        else:
            final_content+=bin_letter

    return key_content, final_content

def main():
    file_name = input("Qual o nome do arquivo a ser aberto? Digite 0 para 'texto_normal.txt' e 1 para 'texto_cifrado.txt', ou o nome do arquivo sem .txt. ")
    if file_name == "0": 
        file_name = "texto_normal"
        option = "C"

    elif file_name == "1":
        file_name = "texto_cifrado"
        option = "D"
    
    else:
        option = input("Codificar (C) ou decodificar (D)?")

    with open(file_name + ".txt", "r") as file: file_content = file.read()

    if option == "C":
        key_content, final_content = vernam_cipher(file_content)
        print(f"Texto original, obtido do arquivo '{file_name}.txt':", file_content)
        print("Chave gerada, salva no arquivo 'chave.txt':", key_content)
        print("Texto cifrado final, salvo no arquivo 'texto_cifrado.txt':", final_content)
        with open("chave.txt", "w") as c: c.write(key_content)
        with open("texto_cifrado.txt", "w") as f: f.write(final_content)

    elif option == "D":
        key_file_name = input("Qual o nome do arquivo de chave? Digite 0 para chave.txt, ou o nome do arquivo sem .txt")
        if key_file_name == "0": key_file_name = "chave"
        with open(key_file_name + ".txt", "r") as file: key_file_content = file.read()
        final_content = vernam_decipher(file_content, key_file_content)
        print(f"Texto cifrado original, obtido do arquivo '{file_name}.txt':", file_content)
        print(f"Chave, obtida do arquivo '{key_file_name}.txt':", file_content)
        print("Texto decifrado final, salvo no arquivo 'texto_decifrado.txt':", final_content)
        with open("texto_decifrado.txt", "w") as f: f.write(final_content)

if __name__ == "__main__":
    main()