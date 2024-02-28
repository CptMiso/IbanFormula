    #Enlever les caractères indésirables (espaces, tirets)
iban = "GB87 BARC 2065 8244 9716 55"
iban = iban.replace(" ", "")
#print(iban)

    #Déplacer les 4 premiers caractères à la fin du compte
first = iban[:4]
second = iban[4:]
#print(first)
#print(second)
iban = second + first
#print(iban)

    #Remplacer les lettres par des chiffres au moyen d'une table de conversion (A=10, B=11, C=12 etc.)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in alphabet:
    iban = iban.replace(i, str(alphabet.index(i)+10))
#print(iban)

    #Diviser le nombre ainsi obtenu par 97, Si le reste n'est pas égal à 1 l'IBAN est incorrect : Modulo de 97 égal à 1.
iban = int(iban)

if iban%97 != 1:
    print("L'iban est faux")
else:
    print("L'iban est correcte")

    
