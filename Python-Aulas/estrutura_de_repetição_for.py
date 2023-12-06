texto = input("Infome um texto para verificar as vogais: ")
VOGAIS = "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end="")