from personne import Personne
from etudiant import Etudiant
from employe import Employe
from livre import Livre
from emprunt import Emprunt
from bibliotheque import Bibliotheque
from datetime import datetime

# Dictionnaire pour les couleurs et styles ANSI
COULEURS = {
    'RESET': '\033[0m',
    'NOIR': '\033[30m',
    'ROUGE': '\033[31m',
    'VERT': '\033[32m',
    'JAUNE': '\033[33m',
    'BLEU': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'BLANC': '\033[37m',
    'GRAS': '\033[1m',
    'ITALIQUE': '\033[3m',
    'SOULIGNE': '\033[4m',
    'BACKGROUND_BLANC': '\033[47m',
    'BACKGROUND_BLEU': '\033[44m',
}

# Création d'une instance de la bibliothèque au début
ma_bibliotheque = Bibliotheque("Bibliothèque Centrale U", "123 Rue de l'Université")

# Ajout de données initiales pour le test
def initialiser_donnees():
    # Livres
    livre1 = Livre("978-2070360868", "Les Misérables", "Victor Hugo", 1862, 5, "Roman")
    livre2 = Livre("978-0321765723", "The Lord of the Rings", "J.R.R. Tolkien", 1954, 3, "Fantaisie")
    livre3 = Livre("978-2253018288", "Le Comte de Monte-Cristo", "Alexandre Dumas", 1844, 2, "Roman")
    ma_bibliotheque.ajouter_livre(livre1)
    ma_bibliotheque.ajouter_livre(livre2)
    ma_bibliotheque.ajouter_livre(livre3)

    # Utilisateurs
    etudiant1 = Etudiant("E001", "Dupont", "Jean", "2000-05-15", "10 Rue des Fleurs", "0612345678", "jean.dupont@univ.fr", "Informatique", "L3", "C-001")
    employe1 = Employe("A001", "Martin", "Sophie", "1985-08-20", "25 Avenue de la Paix", "0687654321", "s.martin@univ.fr", "Bibliothécaire", "M-001", "2010-01-10")
    ma_bibliotheque.ajouter_utilisateur(etudiant1)
    ma_bibliotheque.ajouter_utilisateur(employe1)
    print(COULEURS['VERT'] + "\n✅ Données initiales chargées pour le test." + COULEURS['RESET'])

def afficher_menu():
    print(COULEURS['BLEU'] + "\n" + "="*50 + COULEURS['RESET'])
    print(COULEURS['GRAS'] + COULEURS['BLEU'] + " " * 8 + "MENU PRINCIPAL DE LA BIBLIOTHEQUE" + COULEURS['RESET'])
    print(COULEURS['BLEU'] + "="*50 + COULEURS['RESET'])
    print(COULEURS['GRAS'] + "1. " + COULEURS['RESET'] + "Ajouter un livre")
    print(COULEURS['GRAS'] + "2. " + COULEURS['RESET'] + "Ajouter un utilisateur (étudiant/employé)")
    print(COULEURS['GRAS'] + "3. " + COULEURS['RESET'] + "Effectuer un emprunt")
    print(COULEURS['GRAS'] + "4. " + COULEURS['RESET'] + "Effectuer un retour de livre")
    print(COULEURS['GRAS'] + "5. " + COULEURS['RESET'] + "Rechercher un livre")
    print(COULEURS['GRAS'] + "6. " + COULEURS['RESET'] + "Afficher les détails d'un utilisateur")
    print(COULEURS['GRAS'] + "7. " + COULEURS['RESET'] + "Afficher le catalogue de livres")
    print(COULEURS['GRAS'] + "8. " + COULEURS['RESET'] + "Afficher les emprunts actifs")
    print(COULEURS['GRAS'] + "9. " + COULEURS['RESET'] + "Quitter")
    print(COULEURS['BLEU'] + "="*50 + COULEURS['RESET'])

def ajouter_livre_interactif():
    print(COULEURS['JAUNE'] + "\n--- Ajout d'un nouveau livre ---" + COULEURS['RESET'])
    isbn = input("ISBN: ")
    titre = input("Titre: ")
    auteur = input("Auteur: ")
    annee = int(input("Année de publication: "))
    exemplaires = int(input("Nombre d'exemplaires: "))
    categorie = input("Catégorie: ")
    nouveau_livre = Livre(isbn, titre, auteur, annee, exemplaires, categorie)
    ma_bibliotheque.ajouter_livre(nouveau_livre)

def ajouter_utilisateur_interactif():
    print(COULEURS['JAUNE'] + "\n--- Ajout d'un nouvel utilisateur ---" + COULEURS['RESET'])
    type_utilisateur = input("Type d'utilisateur (etudiant/employe): ").lower()
    if type_utilisateur not in ["etudiant", "employe"]:
        print(COULEURS['ROUGE'] + "❌ Type d'utilisateur invalide." + COULEURS['RESET'])
        return

    id_personne = input("ID de la personne: ")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    date_naissance = input("Date de naissance (AAAA-MM-JJ): ")
    adresse = input("Adresse: ")
    telephone = input("Téléphone: ")
    email = input("Email: ")
    
    if type_utilisateur == "etudiant":
        filiere = input("Filière: ")
        niveau = input("Niveau d'étude: ")
        carte = input("Numéro de carte étudiant: ")
        nouvel_utilisateur = Etudiant(id_personne, nom, prenom, date_naissance, adresse, telephone, email, filiere, niveau, carte)
    else: # type_utilisateur == "employe"
        poste = input("Poste: ")
        num_employe = input("Numéro d'employé: ")
        date_embauche = input("Date d'embauche (AAAA-MM-JJ): ")
        nouvel_utilisateur = Employe(id_personne, nom, prenom, date_naissance, adresse, telephone, email, poste, num_employe, date_embauche)

    ma_bibliotheque.ajouter_utilisateur(nouvel_utilisateur)
    
def effectuer_emprunt_interactif():
    print(COULEURS['JAUNE'] + "\n--- Emprunt d'un livre ---" + COULEURS['RESET'])
    id_utilisateur = input("ID de l'utilisateur: ")
    isbn_livre = input("ISBN du livre: ")
    duree = int(input("Durée de l'emprunt en jours: "))
    ma_bibliotheque.effectuer_emprunt(id_utilisateur, isbn_livre, duree)

def effectuer_retour_interactif():
    print(COULEURS['JAUNE'] + "\n--- Retour d'un livre ---" + COULEURS['RESET'])
    id_emprunt = input("ID de l'emprunt: ")
    ma_bibliotheque.effectuer_retour(id_emprunt)

def rechercher_livre_interactif():
    print(COULEURS['JAUNE'] + "\n--- Recherche de livre ---" + COULEURS['RESET'])
    critere = input("Entrez un titre, un auteur ou un ISBN: ")
    livres_trouves = ma_bibliotheque.rechercher_livre(critere)
    if livres_trouves:
        print(COULEURS['VERT'] + "✅ Livres trouvés:" + COULEURS['RESET'])
        for livre in livres_trouves:
            print("-" * 20)
            print(livre.get_details())
    else:
        print(COULEURS['ROUGE'] + "❌ Aucun livre ne correspond à votre recherche." + COULEURS['RESET'])

def afficher_catalogue_livres():
    print(COULEURS['JAUNE'] + "\n--- Catalogue de livres ---" + COULEURS['RESET'])
    if not ma_bibliotheque._catalogue_livres:
        print("Le catalogue est vide.")
        return
    for livre in ma_bibliotheque._catalogue_livres.values():
        print("-" * 20)
        print(livre.get_details())

def afficher_details_utilisateur():
    print(COULEURS['JAUNE'] + "\n--- Détails de l'utilisateur ---" + COULEURS['RESET'])
    id_utilisateur = input("ID de l'utilisateur: ")
    utilisateur = ma_bibliotheque.get_utilisateur(id_utilisateur)
    if utilisateur:
        print("-" * 20)
        print(utilisateur.get_details())
    else:
        print(COULEURS['ROUGE'] + "❌ Utilisateur non trouvé." + COULEURS['RESET'])

def afficher_emprunts_actifs():
    print(COULEURS['JAUNE'] + "\n--- Emprunts actifs ---" + COULEURS['RESET'])
    emprunts = ma_bibliotheque.get_emprunts_actifs()
    if not emprunts:
        print("Aucun emprunt actif.")
        return
    for emprunt in emprunts.values():
        print("-" * 20)
        print(emprunt.get_details())
    
def main_app():
    initialiser_donnees()
    
    while True:
        afficher_menu()
        choix = input(COULEURS['CYAN'] + "Entrez votre choix: " + COULEURS['RESET'])

        if choix == '1':
            ajouter_livre_interactif()
        elif choix == '2':
            ajouter_utilisateur_interactif()
        elif choix == '3':
            effectuer_emprunt_interactif()
        elif choix == '4':
            effectuer_retour_interactif()
        elif choix == '5':
            rechercher_livre_interactif()
        elif choix == '6':
            afficher_details_utilisateur()
        elif choix == '7':
            afficher_catalogue_livres()
        elif choix == '8':
            afficher_emprunts_actifs()
        elif choix == '9':
            print(COULEURS['VERT'] + "Merci d'avoir utilisé le Gestionnaire de Bibliothèque. Au revoir!" + COULEURS['RESET'])
            break
        else:
            print(COULEURS['ROUGE'] + "❌ Choix invalide. Veuillez réessayer." + COULEURS['RESET'])

if __name__ == "__main__":
    main_app()