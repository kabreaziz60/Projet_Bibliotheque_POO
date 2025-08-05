from livre import Livre
from etudiant import Etudiant
from employe import Employe
from emprunt import Emprunt
from datetime import datetime, timedelta

class Bibliotheque:
    def __init__(self, nom, adresse):
        self._nom = nom
        self._adresse = adresse
        self._catalogue_livres = {}  # Composition de Livres
        self._utilisateurs = {}      # Composition d'Utilisateurs
        self._emprunts_actifs = {}   # Agrégation d'Emprunts
        self._id_emprunt_counter = 1

    # Méthodes de gestion des livres
    def ajouter_livre(self, livre):
        self._catalogue_livres[livre.get_isbn()] = livre
        print(f"Livre '{livre.get_titre()}' ajouté au catalogue.")

    def rechercher_livre(self, critere_recherche):
        livres_trouves = []
        for isbn, livre in self._catalogue_livres.items():
            if (critere_recherche.lower() in livre.get_titre().lower() or
                critere_recherche.lower() in livre.get_auteur().lower() or
                critere_recherche == isbn):
                livres_trouves.append(livre)
        return livres_trouves

    # Méthodes de gestion des utilisateurs
    def ajouter_utilisateur(self, utilisateur):
        self._utilisateurs[utilisateur.get_id()] = utilisateur
        print(f"Utilisateur '{utilisateur.get_prenom()} {utilisateur.get_nom()}' ajouté.")

    def get_utilisateur(self, id_utilisateur):
        return self._utilisateurs.get(id_utilisateur)

    # Méthodes de gestion des emprunts
    def effectuer_emprunt(self, id_utilisateur, isbn_livre, duree_emprunt_jours):
        utilisateur = self.get_utilisateur(id_utilisateur)
        livre = self._catalogue_livres.get(isbn_livre)

        if not utilisateur:
            print("Erreur : Utilisateur non trouvé.")
            return False
        if not livre:
            print("Erreur : Livre non trouvé.")
            return False
        if not livre.est_disponible():
            print("Erreur : Le livre n'est pas disponible.")
            return False

        # Création de l'emprunt
        id_emprunt = f"E{self._id_emprunt_counter:04d}"
        date_emprunt = datetime.now().strftime("%Y-%m-%d")
        date_retour_prevue = (datetime.now() + timedelta(days=duree_emprunt_jours)).strftime("%Y-%m-%d")

        emprunt = Emprunt(id_emprunt, livre, utilisateur, date_emprunt, date_retour_prevue)
        
        # Mise à jour des collections
        self._emprunts_actifs[id_emprunt] = emprunt
        livre.decrementer_disponibilite()
        if isinstance(utilisateur, Etudiant):
            utilisateur.ajouter_emprunt(emprunt)
        
        self._id_emprunt_counter += 1
        print(f"Emprunt {id_emprunt} effectué avec succès.")
        return True

    def effectuer_retour(self, id_emprunt):
        emprunt = self._emprunts_actifs.get(id_emprunt)
        
        if not emprunt:
            print("Erreur : Emprunt non trouvé.")
            return 0
        
        retard = emprunt.retourner_livre() # Cette méthode met à jour le statut et incrémente la disponibilité du livre
        
        # On pourrait calculer la pénalité ici
        penalite = retard * 0.5  # Exemple de 0.5 unité monétaire par jour de retard
        
        # Déplacer l'emprunt vers un historique si nécessaire
        # (Pour cet exemple simple, nous le supprimons juste des emprunts actifs)
        del self._emprunts_actifs[id_emprunt]
        
        print(f"Le livre a été retourné. Pénalité de {penalite} calculée.")
        return penalite

    def get_emprunts_actifs(self):
        return self._emprunts_actifs