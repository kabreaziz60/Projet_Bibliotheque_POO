from livre import Livre
from etudiant import Etudiant
from datetime import date, datetime, timedelta

class Emprunt:
    def __init__(self, id_emprunt, livre, etudiant, date_emprunt, date_retour_prevue):
        self._id_emprunt = id_emprunt
        self._livre = livre
        self._etudiant = etudiant
        self._date_emprunt = datetime.strptime(date_emprunt, "%Y-%m-%d").date()
        self._date_retour_prevue = datetime.strptime(date_retour_prevue, "%Y-%m-%d").date()
        self._statut = "en cours"

    def get_details(self):
        return (f"ID Emprunt: {self._id_emprunt}\n"
                f"Livre: {self._livre.get_titre()} (ISBN: {self._livre.get_isbn()})\n"
                f"Étudiant: {self._etudiant.get_prenom()} {self._etudiant.get_nom()}\n"
                f"Date d'emprunt: {self._date_emprunt.strftime('%Y-%m-%d')}\n"
                f"Date de retour prévue: {self._date_retour_prevue.strftime('%Y-%m-%d')}\n"
                f"Statut: {self._statut}")

    def calculer_retard(self):
        aujourdhui = date.today()
        if aujourdhui > self._date_retour_prevue and self._statut == "en cours":
            retard = (aujourdhui - self._date_retour_prevue).days
            return retard
        return 0

    def retourner_livre(self):
        if self._statut == "en cours":
            self._livre.incrementer_disponibilite()
            self._statut = "rendu"
            retard = self.calculer_retard()
            if retard > 0:
                print(f"Livre retourné avec {retard} jour(s) de retard.")
                # On pourrait ajouter ici un calcul de pénalité
                return retard
            else:
                print("Livre retourné à temps.")
                return 0
        else:
            print("Erreur: Le livre a déjà été retourné.")
            return 0
    
    # Getters
    def get_id(self):
        return self._id_emprunt

    def get_livre(self):
        return self._livre
    
    def get_etudiant(self):
        return self._etudiant