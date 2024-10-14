# T1 - Segurança de Redes e Sistemas

## Descrição
Este repositório contém o **Trabalho 1** da disciplina de Segurança de Redes e Sistemas, que consiste na implementação de diferentes técnicas de criptografia, incluindo um Cifrador de César, análise de frequência, cifrador de Vernam e o algoritmo RC4.

## Conteúdo

### 1. Cifrador de César
- **caesar_bad.py**: Implementação anterior, que utiliza a tabela ASCII.
- **caesar.py**: Implementação atualizada, que utiliza um conjunto de caracteres "hard-coded".

### 2. Analisador de Frequência
- **frequency_analysis.py**: Analisa a frequência de letras no arquivo "cifrado.txt" comparando as proporções das letras com a frequência da língua portuguesa.
    - **Instruções**: 
        - Rode o arquivo com o input = cifrado.
        - Para garantir o funcionamento correto, descomente as linhas 18-22 e comente as linhas 11-15, que se referem ao conjunto de caracteres minúsculos.
    - Use este script para decodificar a mensagem criptografada fornecida.

### 3. Cifrador de Vernam
- **Código**: Utilize este cifrador para criptografar o texto aberto encontrado na análise de frequência.

### 4. Algoritmo RC4
- **Código**: Use o algoritmo RC4 para criptografar o texto aberto decodificado na análise de frequência, a fim de entender seu funcionamento.