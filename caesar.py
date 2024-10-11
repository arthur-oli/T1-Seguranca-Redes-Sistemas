def remove_acento(char):
    if char in ["á", "ã", "à", "â"]:
        return "a"
    elif char in ["é", "ê"]:
        return "e"
    elif char in ["í"]:
        return "i"
    elif char in ["ó", "õ", "ò", "ô"]:
        return "o"
    elif char in ["ú", "ü"]:
        return "u"
    elif char == "ç":
        return "c"
    else:
        return char

def caesar_cipher(content, k):
    result = []
    
    for char in content:
        char = remove_acento(char)
        new_char = chr(ord(char) + k)
        upper = lower = ' '

        if new_char > 'Z' and new_char < 'a':
            upper = 'a'
            lower = 'Z'

        elif new_char > '9' and new_char < 'A':
            upper = 'A'
            lower = '9'

        elif new_char > 'z':
            upper = '0'
            lower = 'z'

        else:
            upper = '!'
        result.append(chr(ord(upper) + (ord(new_char) - ord(lower) - 1)))

    return ''.join(result)

file_to_cypher = input("Qual o nome do arquivo aberto?")
cypher_value = int(input("Quanto será o deslocamento da cifra?"))

with open(file_to_cypher + ".txt", "r") as file:
    file_content = file.read()

result = caesar_cipher(file_content, cypher_value)
print(result)