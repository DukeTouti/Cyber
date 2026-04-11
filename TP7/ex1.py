# ============================================================
# Exercice 1 : Substitution et Analyse Frequentielle
# ============================================================

# Table de substitution monoalphabetique (donnee dans le TP)
# Clair   : A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# Chiffre : N  L  E  H  X  Y  J  T  G  K  Z  D  A  R  W  M  C  Q  S  B  O  F  V  I  P  U
TABLE_CHIFFREMENT = ['N','L','E','H','X','Y','J','T','G','K','Z','D','A',
                     'R','W','M','C','Q','S','B','O','F','V','I','P','U']


# ----- Q1 : Chiffrement de Cesar -----

def cesar_chiffrer(texte, cle):
    resultat = ""
    for caractere in texte:
        if caractere.isalpha():
            resultat += chr(ord('A') + (ord(caractere.upper()) - ord('A') + cle) % 26)
        else:
            resultat += caractere
    return resultat

def cesar_dechiffrer(texte, cle):
    return cesar_chiffrer(texte, -cle)


# ----- Q2 : Substitution monoalphabetique -----

def mono_chiffrer(texte):
    resultat = ""
    for caractere in texte:
        if caractere.isalpha():
            indice = ord(caractere.upper()) - ord('A')
            resultat += TABLE_CHIFFREMENT[indice]
        else:
            resultat += caractere
    return resultat

def mono_dechiffrer(texte):
    resultat = ""
    for caractere in texte:
        if caractere.isalpha():
            indice = TABLE_CHIFFREMENT.index(caractere.upper())
            resultat += chr(ord('A') + indice)
        else:
            resultat += caractere
    return resultat


# ----- Q4 : Dechiffrement avec phrase-cle -----

def construire_table_phrasekey(phrase):
    table = []
    for caractere in phrase.upper():
        if caractere.isalpha() and caractere not in table:
            table.append(caractere)
    for caractere in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if caractere not in table:
            table.append(caractere)
    return table

def phrasekey_dechiffrer(texte, phrase):
    table = construire_table_phrasekey(phrase)
    resultat = ""
    for caractere in texte:
        if caractere.isalpha():
            indice = table.index(caractere.upper())
            resultat += chr(ord('A') + indice)
        else:
            resultat += caractere
    return resultat


# ----- Q5 : Analyse frequentielle -----

def compter_frequences(texte):
    frequences = {}
    for caractere in texte.upper():
        if caractere.isalpha():
            frequences[caractere] = frequences.get(caractere, 0) + 1
    return frequences

def frequence_attaque(texte):
    # Frequences standard francais (ordre decroissant)
    freq_francais = "EASINTRULODCMPGBVHFQYZXKWJ"
    frequences = compter_frequences(texte)
    lettres_triees = sorted(frequences, key=lambda c: frequences[c], reverse=True)
    correspondance = {}
    for indice, lettre in enumerate(lettres_triees):
        if indice < len(freq_francais):
            correspondance[lettre] = freq_francais[indice]
    resultat = ""
    for caractere in texte.upper():
        if caractere.isalpha():
            resultat += correspondance.get(caractere, '?')
        else:
            resultat += caractere
    return resultat, correspondance, frequences

def appliquer_correspondance(texte, correspondance):
    resultat = ""
    for caractere in texte.upper():
        if caractere.isalpha():
            resultat += correspondance.get(caractere, '?')
        else:
            resultat += caractere
    return resultat


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("EXERCICE 1 : Substitution et Analyse Frequentielle")
    print("=" * 60)

    # Q1
    print("\n[Q1] Chiffrement de 'securite' par Cesar (cle=3)")
    chiffre = cesar_chiffrer("securite", 3)
    print(f"  Clair   : securite")
    print(f"  Chiffre : {chiffre}")
    print(f"  Verif   : {cesar_dechiffrer(chiffre, 3)}")

    # Q2
    print("\n[Q2] Chiffrement de 'securite' par substitution monoalphabetique")
    chiffre = mono_chiffrer("securite")
    print(f"  Clair   : securite")
    print(f"  Chiffre : {chiffre}")
    print(f"  Verif   : {mono_dechiffrer(chiffre)}")

    # Q3
    print("\n[Q3] Deux attaques contre la substitution monoalphabetique")
    print("  1. Analyse frequentielle")
    print("  2. Attaque a texte clair connu (Known Plaintext Attack)")

    # Q4
    print("\n[Q4] Dechiffrement de 'HAWAEZXXIGHAD' (phrase-cle : Il etait une fois)")
    phrase = "Il etait une fois"
    table = construire_table_phrasekey(phrase)
    print(f"  Table : {''.join(table)}")
    print(f"  Clair : {phrasekey_dechiffrer('HAWAEZXXIGHAD', phrase)}")

    # Q5
    print("\n[Q5] Analyse frequentielle : LHLZ HFQ BC HFFPZ WH YOUPFH MUPZH")
    texte = "LHLZ HFQ BC HFFPZ WH YOUPFH MUPZH"

    # Etape 1 : compter les frequences
    frequences = compter_frequences(texte)
    total = sum(frequences.values())
    print("  Frequences :")
    for lettre, nb in sorted(frequences.items(), key=lambda x: x[1], reverse=True):
        print(f"    {lettre} : {nb} ({nb/total*100:.1f}%)")

    # Etape 2 : estimation automatique par frequences francaises
    estimation, _, _ = frequence_attaque(texte)
    print(f"\n  Estimation initiale : {estimation}")

    # Etape 3 : affinage manuel mot par mot
    # H=E (le plus frequent)
    # HFQ=EST   -> F=S, Q=T
    # BC=UN     -> B=U, C=N
    # WH=DE     -> W=D
    # YOUPFH=PHRASE -> Y=P, O=H, U=R, P=A
    # LHLZ=CECI -> L=C, Z=I
    # MUPZH=VRAIE -> M=V
    correspondance_finale = {
        'H':'E', 'F':'S', 'Q':'T',
        'B':'U', 'C':'N', 'W':'D',
        'Y':'P', 'O':'H', 'U':'R', 'P':'A',
        'L':'C', 'Z':'I', 'M':'V'
    }
    print("\n  Correspondance finale :")
    for chiffre_lettre, clair_lettre in sorted(correspondance_finale.items()):
        print(f"    {chiffre_lettre} -> {clair_lettre}")
    print(f"\n  Texte dechiffre : {appliquer_correspondance(texte, correspondance_finale)}")
