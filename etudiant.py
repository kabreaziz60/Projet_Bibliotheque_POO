from personne import Personne

class Etudiant(Personne):
    def __init__(self, id_personne, nom, prenom, date_naissance, adresse, telephone, email, filiere, niveau_etude, carte_etudiant):
        # Appel du constructeur de la classe mère (Personne)
        super().__init__(id_personne, nom, prenom, date_naissance, adresse, telephone, email)

        # Attributs spécifiques à la classe Etudiant
        self._filiere = filiere
        self._niveau_etude = niveau_etude
        self._carte_etudiant = carte_etudiant
        self._emprunts_en_cours = []  # Liste pour stocker les objets Emprunt

    def get_details(self):
        # Surcharge de la méthode get_details() de la classe Personne
        details_personne = super().get_details()
        return (f"{details_personne}\n"
                f"Filière: {self._filiere}\n"
                f"Niveau d'étude: {self._niveau_etude}\n"
                f"Carte étudiant: {self._carte_etudiant}")

    # Méthodes spécifiques à la classe Etudiant
    def ajouter_emprunt(self, emprunt):
        self._emprunts_en_cours.append(emprunt)
        print(f"L'emprunt {emprunt.get_id()} a été ajouté à l'étudiant {self._prenom}.")

    def retirer_emprunt(self, emprunt):
        if emprunt in self._emprunts_en_cours:
            self._emprunts_en_cours.remove(emprunt)
            print(f"L'emprunt {emprunt.get_id()} a été retiré de l'étudiant {self._prenom}.")
        else:
            print("Erreur: Cet emprunt n'est pas en cours pour cet étudiant.")

    # Getters spécifiques à la classe Etudiant
    def get_filiere(self):
        return self._filiere

    def get_niveau_etude(self):
        return self._niveau_etude
    
    def get_carte_etudiant(self):
        return self._carte_etudiant
    
    def get_emprunts_en_cours(self):
        return self._emprunts_en_cours