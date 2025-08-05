class Livre:
    def __init__(self, isbn, titre, auteur, annee_publication, nombre_exemplaires_total, categorie):
        self._isbn = isbn
        self._titre = titre
        self._auteur = auteur
        self._annee_publication = annee_publication
        self._nombre_exemplaires_total = nombre_exemplaires_total
        self._nombre_exemplaires_disponibles = nombre_exemplaires_total
        self._categorie = categorie

    def get_details(self):
        return (f"ISBN: {self._isbn}\n"
                f"Titre: {self._titre}\n"
                f"Auteur: {self._auteur}\n"
                f"Année de publication: {self._annee_publication}\n"
                f"Catégorie: {self._categorie}\n"
                f"Exemplaires disponibles: {self._nombre_exemplaires_disponibles}/{self._nombre_exemplaires_total}")

    def est_disponible(self):
        return self._nombre_exemplaires_disponibles > 0

    def decrementer_disponibilite(self):
        if self.est_disponible():
            self._nombre_exemplaires_disponibles -= 1
            return True
        return False

    def incrementer_disponibilite(self):
        if self._nombre_exemplaires_disponibles < self._nombre_exemplaires_total:
            self._nombre_exemplaires_disponibles += 1
            return True
        return False

    # Getters
    def get_isbn(self):
        return self._isbn
    
    def get_titre(self):
        return self._titre
    
    def get_auteur(self):
        return self._auteur
    
    # Vous pouvez ajouter d'autres getters si nécessaire