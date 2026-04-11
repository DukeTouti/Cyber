# ============================================================
# Exercice 3 : Cryptanalyse de Vigenere - Retrouver la cle
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

def filtrer_lettres(texte):
    return [caractere.upper() for caractere in texte if caractere.isalpha()]

def retrouver_cle(clair, chiffre):
    lettres_clair   = filtrer_lettres(clair)
    lettres_chiffre = filtrer_lettres(chiffre)

    # Calculer le decalage a chaque position : (chiffre - clair + 26) % 26
    decalages = []
    for indice in range(len(lettres_clair)):
        valeur_chiffre = ord(lettres_chiffre[indice]) - ord('A')
        valeur_clair   = ord(lettres_clair[indice])   - ord('A')
        decalages.append((valeur_chiffre - valeur_clair + 26) % 26)

    # Detecter la periode : plus petite longueur p ou les decalages se repetent
    longueur = len(decalages)
    periode = longueur
    for p in range(1, longueur + 1):
        if all(decalages[indice] == decalages[indice % p] for indice in range(longueur)):
            periode = p
            break

    cle_trouvee = ""
    for indice in range(periode):
        cle_trouvee += chr(ord('A') + decalages[indice])
    return cle_trouvee, decalages


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("EXERCICE 3 : Cryptanalyse Vigenere - Retrouver la cle")
    print("=" * 60)

    clair   = "MASTER TELECOM"
    chiffre = "AKGDSBHOZOQYA"

    print(f"\n  Clair   : {clair}")
    print(f"  Chiffre : {chiffre}")

    cle, decalages = retrouver_cle(clair, chiffre)

    # Detail position par position
    lettres_clair   = filtrer_lettres(clair)
    lettres_chiffre = filtrer_lettres(chiffre)
    print(f"\n  Detail :")
    print(f"  {'Pos':<5} {'Clair':<8} {'Chiffre':<10} {'Decalage':<10} {'Cle'}")
    print(f"  {'-'*5} {'-'*8} {'-'*10} {'-'*10} {'-'*3}")
    for indice in range(len(lettres_clair)):
        print(f"  {indice:<5} {lettres_clair[indice]:<8} {lettres_chiffre[indice]:<10} {decalages[indice]:<10} {cle[indice % len(cle)]}")

    print(f"\n  Cle trouvee : {cle}")

    # Verification
    chiffre_obtenu = vigenere_chiffrer(clair, cle).replace(" ", "")
    if chiffre_obtenu == chiffre:
        print(f"  Verification : chiffrer('{clair}', '{cle}') = {chiffre_obtenu} [OK]")
    else:
        print(f"  Verification : [ERREUR] obtenu {chiffre_obtenu}")
