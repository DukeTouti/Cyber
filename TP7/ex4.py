# ============================================================
# Exercice 4 : Chiffrement par Transposition en Colonnes
# ============================================================

def normaliser(texte):
    # Supprimer espaces et accents, tout en majuscules
    accents = {
        'é':'E','è':'E','ê':'E','ë':'E',
        'à':'A','â':'A','ä':'A',
        'î':'I','ï':'I',
        'ô':'O','ö':'O',
        'ù':'U','û':'U','ü':'U',
        'ç':'C'
    }
    resultat = ""
    for caractere in texte.lower():
        if caractere in accents:
            resultat += accents[caractere]
        elif caractere.isalpha():
            resultat += caractere.upper()
    return resultat

def construire_ordre(cle):
    # Retourne les indices des colonnes tries par ordre alphabetique de la cle
    # ex: DESERT -> D(0) E(1) S(2) E(3) R(4) T(5)
    # ordre alpha : D E E R S T -> [0, 1, 3, 4, 2, 5]
    return sorted(range(len(cle)), key=lambda indice: cle[indice])

def transpose_chiffrer(texte, cle):
    texte_norm = normaliser(texte)
    cle_norm   = normaliser(cle)
    nb_cols    = len(cle_norm)
    nb_lignes  = (len(texte_norm) + nb_cols - 1) // nb_cols
    ordre      = construire_ordre(cle_norm)

    # Afficher la grille
    rangs = [0] * nb_cols
    for rang, colonne in enumerate(ordre):
        rangs[colonne] = rang + 1
    print(f"  Cle    : {' '.join(cle_norm)}")
    print(f"  Ordre  : {' '.join(str(rang) for rang in rangs)}")
    print(f"  Grille ({nb_lignes} lignes x {nb_cols} colonnes) :")
    for ligne in range(nb_lignes):
        contenu = ""
        for colonne in range(nb_cols):
            position = ligne * nb_cols + colonne
            contenu += (texte_norm[position] if position < len(texte_norm) else '*') + " "
        print(f"    {contenu}")

    # Lire colonne par colonne dans l'ordre alphabetique de la cle
    chiffre = ""
    for colonne in ordre:
        for ligne in range(nb_lignes):
            position = ligne * nb_cols + colonne
            if position < len(texte_norm):
                chiffre += texte_norm[position]
    return chiffre

def transpose_dechiffrer(chiffre, cle):
    chiffre_norm = normaliser(chiffre)
    cle_norm     = normaliser(cle)
    nb_cols      = len(cle_norm)
    nb_lignes    = (len(chiffre_norm) + nb_cols - 1) // nb_cols
    reste        = len(chiffre_norm) % nb_cols
    ordre        = construire_ordre(cle_norm)

    # Calculer la hauteur de chaque colonne
    hauteurs = []
    for colonne in range(nb_cols):
        rang_alpha = ordre.index(colonne)
        if reste == 0 or rang_alpha < reste:
            hauteurs.append(nb_lignes)
        else:
            hauteurs.append(nb_lignes - 1)

    # Remplir la grille colonne par colonne dans l'ordre alphabetique
    grille = [[''] * nb_cols for _ in range(nb_lignes)]
    position = 0
    for colonne in ordre:
        for ligne in range(hauteurs[colonne]):
            grille[ligne][colonne] = chiffre_norm[position]
            position += 1

    # Lire ligne par ligne
    clair = ""
    for ligne in range(nb_lignes):
        for colonne in range(nb_cols):
            if grille[ligne][colonne] != '':
                clair += grille[ligne][colonne]
    return clair


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("EXERCICE 4 : Transposition en Colonnes")
    print("=" * 60)

    cle = "desert"

    # Q1 : Chiffrement
    print("\n[Q1] Chiffrement avec la cle 'desert'")
    message = "seul celui qui voyage verra le long chemin qui mene a son pays"
    print(f"  Clair : {message}\n")
    chiffre = transpose_chiffrer(message, cle)
    print(f"\n  Chiffre : {chiffre}")
    print(f"  Verif   : {transpose_dechiffrer(chiffre, cle)}")

    # Q2 : Dechiffrement
    print("\n[Q2] Dechiffrement de 'AGMBHNDJEKCIFL' avec la cle 'desert'")
    chiffre2 = "AGMBHNDJEKCIFL"
    print(f"  Chiffre : {chiffre2}")
    print(f"  Clair   : {transpose_dechiffrer(chiffre2, cle)}")
