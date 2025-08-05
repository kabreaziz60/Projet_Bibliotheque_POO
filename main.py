from personne import Personne
from etudiant import Etudiant
from employe import Employe
from livre import Livre
from emprunt import Emprunt
from bibliotheque import Bibliotheque
from datetime import datetime, timedelta

def main():
    # 1. Création de la bibliothèque
    ma_bibliotheque = Bibliotheque("Bibliothèque Centrale U", "123 Rue de l'Université")
    print(f"Bienvenue à la {ma_bibliotheque._nom}.\n")

    # 2. Ajout de livres
    livre1 = Livre("978-2070360868", "Les Misérables", "Victor Hugo", 1862, 5, "Roman")
    livre2 = Livre("978-0321765723", "The Lord of the Rings", "J.R.R. Tolkien", 1954, 3, "Fantaisie")
    livre3 = Livre("978-2253018288", "Le Comte de Monte-Cristo", "Alexandre Dumas", 1844, 2, "Roman")

    ma_bibliotheque.ajouter_livre(livre1)
    ma_bibliotheque.ajouter_livre(livre2)
    ma_bibliotheque.ajouter_livre(livre3)
    print("-" * 20)
    
    # 3. Ajout d'utilisateurs
    etudiant1 = Etudiant("E001", "Dupont", "Jean", "2000-05-15", "10 Rue des Fleurs", "0612345678", "jean.dupont@univ.fr", "Informatique", "L3", "C-001")
    employe1 = Employe("A001", "Martin", "Sophie", "1985-08-20", "25 Avenue de la Paix", "0687654321", "s.martin@univ.fr", "Bibliothécaire", "M-001", "2010-01-10")

    ma_bibliotheque.ajouter_utilisateur(etudiant1)
    ma_bibliotheque.ajouter_utilisateur(employe1)
    print("-" * 20)

    # 4. Effectuer un emprunt
    print("Tentative d'emprunt de 'Les Misérables' par Jean Dupont :")
    ma_bibliotheque.effectuer_emprunt(etudiant1.get_id(), livre1.get_isbn(), 14)
    print(livre1.get_details())
    print("-" * 20)
    
    # 5. Consulter les emprunts actifs
    print("Emprunts actifs :")
    for emprunt in ma_bibliotheque.get_emprunts_actifs().values():
        print(emprunt.get_details())
    print("-" * 20)
    
    # 6. Effectuer un retour
    print("Tentative de retour du livre 'Les Misérables' :")
    id_emprunt_a_retourner = list(ma_bibliotheque._emprunts_actifs.keys())[0] # Récupère le premier emprunt actif
    ma_bibliotheque.effectuer_retour(id_emprunt_a_retourner)
    print(livre1.get_details())
    print("-" * 20)
    
if __name__ == "__main__":
    main()