# ============================================================
# Exercice 2 : Chiffrement de Vigenere
# ============================================================

def vigenere_chiffrer(texte, cle):
    resultat = ""
    indice_cle = 0
    for caractere in texte:
        if caractere.isalpha():
            decalage = ord(cle[indice_cle % len(cle)].upper()) - ord('A')
            resultat += chr(ord('A') + (ord(caractere.upper()) - ord('A') + decalage) % 26)
            indice_cle += 1
        else:
            resultat += caractere
    return resultat

def vigenere_dechiffrer(texte, cle):
    resultat = ""
    indice_cle = 0
    for caractere in texte:
        if caractere.isalpha():
            decalage = ord(cle[indice_cle % len(cle)].upper()) - ord('A')
            resultat += chr(ord('A') + (ord(caractere.upper()) - ord('A') - decalage + 26) % 26)
            indice_cle += 1
        else:
            resultat += caractere
    return resultat


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("EXERCICE 2 : Chiffrement de Vigenere")
    print("=" * 60)

    chiffre = "vvqimsykttzbx"
    cle = "test"

    print(f"\n  Chiffre : {chiffre}")
    print(f"  Cle     : {cle}")

    clair = vigenere_dechiffrer(chiffre, cle)
    print(f"\n  Clair retrouve : {clair}")

    # Verification
    reverification = vigenere_chiffrer(clair, cle)
    if reverification.lower() == chiffre:
        print(f"  Verification   : chiffrer('{clair}', '{cle}') = {reverification} [OK]")
    else:
        print(f"  Verification   : [ERREUR] obtenu {reverification}")

    # Detail position par position
    print(f"\n  Detail du dechiffrement :")
    print(f"  {'Pos':<5} {'Chiffre':<8} {'Cle':<6} {'Calcul':<22} {'Clair'}")
    print(f"  {'-'*5} {'-'*8} {'-'*6} {'-'*22} {'-'*5}")
    indice_cle = 0
    for position, caractere in enumerate(chiffre):
        if caractere.isalpha():
            valeur_chiffre = ord(caractere.upper()) - ord('A')
            valeur_cle     = ord(cle[indice_cle % len(cle)].upper()) - ord('A')
            valeur_clair   = (valeur_chiffre - valeur_cle + 26) % 26
            lettre_cle     = cle[indice_cle % len(cle)]
            calcul         = f"({valeur_chiffre}-{valeur_cle}+26)%26={valeur_clair}"
            print(f"  {position:<5} {caractere:<8} {lettre_cle:<6} {calcul:<22} {chr(ord('A') + valeur_clair)}")
            indice_cle += 1
