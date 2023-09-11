vogais = 'aeiou'
palavra = input('Digite uma palavra: ').lower()
total_vogais = 0
for letra in palavra:
    if letra in vogais:
        total_vogais += 1
print(f'O número total de vogais na palavra é: {total_vogais}')
