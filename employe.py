from personne import Personne

class Employe(Personne):
    def __init__(self, id_personne, nom, prenom, date_naissance, adresse, telephone, email, poste, numero_employe, date_embauche):
        # Appel du constructeur de la classe mère (Personne)
        super().__init__(id_personne, nom, prenom, date_naissance, adresse, telephone, email)

        # Attributs spécifiques à la classe Employe
        self._poste = poste
        self._numero_employe = numero_employe
        self._date_embauche = date_embauche

    def get_details(self):
        # Surcharge de la méthode get_details() de la classe Personne
        details_personne = super().get_details()
        return (f"{details_personne}\n"
                f"Poste: {self._poste}\n"
                f"Numéro employé: {self._numero_employe}\n"
                f"Date d'embauche: {self._date_embauche}")

    # Getters spécifiques à la classe Employe
    def get_poste(self):
        return self._poste

    def get_numero_employe(self):
        return self._numero_employe