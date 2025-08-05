class Personne:
    def __init__(self, id_personne, nom, prenom, date_naissance, adresse, telephone, email):
        self._id_personne = id_personne
        self._nom = nom
        self._prenom = prenom
        self._date_naissance = date_naissance
        self._adresse = adresse
        self._telephone = telephone
        self._email = email

    def get_details(self):
        return (f"ID: {self._id_personne}\n"
                f"Nom: {self._nom} {self._prenom}\n"
                f"Date de naissance: {self._date_naissance}\n"
                f"Adresse: {self._adresse}\n"
                f"Téléphone: {self._telephone}\n"
                f"Email: {self._email}")

    def modifier_coordonnees(self, nouvelle_adresse=None, nouveau_telephone=None, nouvel_email=None):
        if nouvelle_adresse:
            self._adresse = nouvelle_adresse
        if nouveau_telephone:
            self._telephone = nouveau_telephone
        if nouvel_email:
            self._email = nouvel_email
        print(f"Coordonnées de {self._prenom} {self._nom} modifiées avec succès.")

    # Getters (méthodes pour accéder aux attributs privés) - très utile en POO
    def get_id(self):
        return self._id_personne
    
    def get_nom(self):
        return self._nom
    
    def get_prenom(self):
        return self._prenom
    
    # Vous pouvez ajouter d'autres getters si nécessaire