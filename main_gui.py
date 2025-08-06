import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Importez vos classes existantes
from personne import Personne
from etudiant import Etudiant
from employe import Employe
from livre import Livre
from emprunt import Emprunt
from bibliotheque import Bibliotheque

class BibliothequeApp:
    def __init__(self, master):
        self.master = master
        master.title("Gestionnaire de Bibliothèque Universitaire")
        master.geometry("800x600")

        self.bibliotheque = Bibliotheque("Bibliothèque Centrale U", "123 Rue de l'Université")
        self.initialiser_donnees()

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        # Création des onglets
        self.frame_livres = ttk.Frame(self.notebook)
        self.frame_emprunts = ttk.Frame(self.notebook)
        self.frame_utilisateurs = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_livres, text="Livres")
        self.notebook.add(self.frame_emprunts, text="Emprunts")
        self.notebook.add(self.frame_utilisateurs, text="Utilisateurs")

        self.creer_widgets_livres(self.frame_livres)
        self.creer_widgets_emprunts(self.frame_emprunts)
        self.creer_widgets_utilisateurs(self.frame_utilisateurs)

    def initialiser_donnees(self):
        # Ajout de données initiales pour le test
        livre1 = Livre("978-2070360868", "Les Misérables", "Victor Hugo", 1862, 5, "Roman")
        livre2 = Livre("978-0321765723", "The Lord of the Rings", "J.R.R. Tolkien", 1954, 3, "Fantaisie")
        self.bibliotheque.ajouter_livre(livre1)
        self.bibliotheque.ajouter_livre(livre2)

        etudiant1 = Etudiant("E001", "Dupont", "Jean", "2000-05-15", "10 Rue des Fleurs", "0612345678", "jean.dupont@univ.fr", "Informatique", "L3", "C-001")
        employe1 = Employe("A001", "Martin", "Sophie", "1985-08-20", "25 Avenue de la Paix", "0687654321", "s.martin@univ.fr", "Bibliothécaire", "M-001", "2010-01-10")
        self.bibliotheque.ajouter_utilisateur(etudiant1)
        self.bibliotheque.ajouter_utilisateur(employe1)

    def creer_widgets_livres(self, frame):
        # Widgets pour la gestion des livres
        frame_ajout = ttk.LabelFrame(frame, text="Ajouter un Livre")
        frame_ajout.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_ajout, text="ISBN:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.isbn_entry = ttk.Entry(frame_ajout)
        self.isbn_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_ajout, text="Titre:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.titre_entry = ttk.Entry(frame_ajout)
        self.titre_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_ajout, text="Auteur:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.auteur_entry = ttk.Entry(frame_ajout)
        self.auteur_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_ajout, text="Année:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.annee_entry = ttk.Entry(frame_ajout)
        self.annee_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame_ajout, text="Exemplaires:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.exemplaires_entry = ttk.Entry(frame_ajout)
        self.exemplaires_entry.grid(row=4, column=1, padx=5, pady=5)
        
        ttk.Label(frame_ajout, text="Catégorie:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.categorie_entry = ttk.Entry(frame_ajout)
        self.categorie_entry.grid(row=5, column=1, padx=5, pady=5)

        bouton_ajouter_livre = ttk.Button(frame_ajout, text="Ajouter le Livre", command=self.ajouter_livre)
        bouton_ajouter_livre.grid(row=6, column=0, columnspan=2, pady=10)

        # Affichage du catalogue
        frame_catalogue = ttk.LabelFrame(frame, text="Catalogue de Livres")
        frame_catalogue.pack(padx=10, pady=10, fill="both", expand=True)

        self.catalogue_listbox = tk.Listbox(frame_catalogue)
        self.catalogue_listbox.pack(fill="both", expand=True)
        self.charger_catalogue()

    def creer_widgets_emprunts(self, frame):
        # Widgets pour la gestion des emprunts
        frame_emprunt_retour = ttk.LabelFrame(frame, text="Emprunt / Retour")
        frame_emprunt_retour.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_emprunt_retour, text="ID Utilisateur:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.id_utilisateur_emprunt_entry = ttk.Entry(frame_emprunt_retour)
        self.id_utilisateur_emprunt_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_emprunt_retour, text="ISBN du Livre:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.isbn_livre_emprunt_entry = ttk.Entry(frame_emprunt_retour)
        self.isbn_livre_emprunt_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_emprunt_retour, text="Durée (jours):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.duree_emprunt_entry = ttk.Entry(frame_emprunt_retour)
        self.duree_emprunt_entry.grid(row=2, column=1, padx=5, pady=5)

        bouton_emprunter = ttk.Button(frame_emprunt_retour, text="Emprunter", command=self.effectuer_emprunt)
        bouton_emprunter.grid(row=3, column=0, padx=5, pady=10)

        self.id_emprunt_retour_entry = ttk.Entry(frame_emprunt_retour)
        self.id_emprunt_retour_entry.grid(row=4, column=1, padx=5, pady=5)
        ttk.Label(frame_emprunt_retour, text="ID Emprunt à retourner:").grid(row=4, column=0, padx=5, pady=5, sticky="w")

        bouton_retourner = ttk.Button(frame_emprunt_retour, text="Retourner", command=self.effectuer_retour)
        bouton_retourner.grid(row=5, column=0, columnspan=2, pady=10)

        # Affichage des emprunts actifs
        frame_emprunts_actifs = ttk.LabelFrame(frame, text="Emprunts Actifs")
        frame_emprunts_actifs.pack(padx=10, pady=10, fill="both", expand=True)

        self.emprunts_listbox = tk.Listbox(frame_emprunts_actifs)
        self.emprunts_listbox.pack(fill="both", expand=True)
        self.charger_emprunts_actifs()

    def creer_widgets_utilisateurs(self, frame):
        # Widgets pour la gestion des utilisateurs
        frame_ajout_utilisateur = ttk.LabelFrame(frame, text="Ajouter un Utilisateur")
        frame_ajout_utilisateur.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_ajout_utilisateur, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.user_id_entry = ttk.Entry(frame_ajout_utilisateur)
        self.user_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_ajout_utilisateur, text="Nom:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.user_nom_entry = ttk.Entry(frame_ajout_utilisateur)
        self.user_nom_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_ajout_utilisateur, text="Prénom:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.user_prenom_entry = ttk.Entry(frame_ajout_utilisateur)
        self.user_prenom_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_ajout_utilisateur, text="Type:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.user_type_combobox = ttk.Combobox(frame_ajout_utilisateur, values=["Etudiant", "Employe"])
        self.user_type_combobox.grid(row=3, column=1, padx=5, pady=5)
        self.user_type_combobox.current(0) # Sélectionne 'Etudiant' par défaut

        bouton_ajouter_utilisateur = ttk.Button(frame_ajout_utilisateur, text="Ajouter l'Utilisateur", command=self.ajouter_utilisateur)
        bouton_ajouter_utilisateur.grid(row=4, column=0, columnspan=2, pady=10)

        # Affichage des utilisateurs
        frame_utilisateurs_list = ttk.LabelFrame(frame, text="Liste des Utilisateurs")
        frame_utilisateurs_list.pack(padx=10, pady=10, fill="both", expand=True)

        self.utilisateurs_listbox = tk.Listbox(frame_utilisateurs_list)
        self.utilisateurs_listbox.pack(fill="both", expand=True)
        self.charger_utilisateurs()

    # Logique métier liée aux boutons
    def ajouter_livre(self):
        isbn = self.isbn_entry.get()
        titre = self.titre_entry.get()
        auteur = self.auteur_entry.get()
        annee = self.annee_entry.get()
        exemplaires = self.exemplaires_entry.get()
        categorie = self.categorie_entry.get()

        if isbn and titre and auteur:
            try:
                nouveau_livre = Livre(isbn, titre, auteur, int(annee), int(exemplaires), categorie)
                self.bibliotheque.ajouter_livre(nouveau_livre)
                messagebox.showinfo("Succès", f"Livre '{titre}' ajouté avec succès.")
                self.charger_catalogue()
                self.effacer_champs_livre()
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides pour l'année et le nombre d'exemplaires.")
        else:
            messagebox.showerror("Erreur", "Les champs ISBN, Titre et Auteur sont obligatoires.")

    def ajouter_utilisateur(self):
        id_user = self.user_id_entry.get()
        nom = self.user_nom_entry.get()
        prenom = self.user_prenom_entry.get()
        user_type = self.user_type_combobox.get()
        
        if id_user and nom and prenom:
            if user_type == "Etudiant":
                nouvel_utilisateur = Etudiant(id_user, nom, prenom, "2000-01-01", "", "", "", "Non renseigné", "Non renseigné", "Non renseigné")
            else: # Employe
                nouvel_utilisateur = Employe(id_user, nom, prenom, "1990-01-01", "", "", "", "Non renseigné", "Non renseigné", "Non renseigné")
            
            self.bibliotheque.ajouter_utilisateur(nouvel_utilisateur)
            messagebox.showinfo("Succès", f"Utilisateur {nom} {prenom} ajouté.")
            self.charger_utilisateurs()
            self.effacer_champs_utilisateur()
        else:
            messagebox.showerror("Erreur", "Les champs ID, Nom et Prénom sont obligatoires.")

    def effectuer_emprunt(self):
        id_user = self.id_utilisateur_emprunt_entry.get()
        isbn = self.isbn_livre_emprunt_entry.get()
        try:
            duree = int(self.duree_emprunt_entry.get())
            if self.bibliotheque.effectuer_emprunt(id_user, isbn, duree):
                messagebox.showinfo("Succès", "Emprunt effectué avec succès.")
                self.charger_emprunts_actifs()
                self.charger_catalogue()
            else:
                messagebox.showerror("Erreur", "L'emprunt n'a pas pu être effectué. Vérifiez les informations.")
        except ValueError:
            messagebox.showerror("Erreur", "La durée doit être un nombre.")

    def effectuer_retour(self):
        id_emprunt = self.id_emprunt_retour_entry.get()
        if id_emprunt:
            penalite = self.bibliotheque.effectuer_retour(id_emprunt)
            if penalite is not None:
                messagebox.showinfo("Succès", f"Livre retourné avec succès. Pénalité : {penalite:.2f} €")
                self.charger_emprunts_actifs()
                self.charger_catalogue()
            else:
                messagebox.showerror("Erreur", "Emprunt non trouvé.")
        else:
            messagebox.showerror("Erreur", "Veuillez entrer l'ID de l'emprunt.")
    
    # Fonctions de mise à jour des listes
    def charger_catalogue(self):
        self.catalogue_listbox.delete(0, tk.END)
        for livre in self.bibliotheque._catalogue_livres.values():
            self.catalogue_listbox.insert(tk.END, f"{livre.get_isbn()} - {livre.get_titre()} ({livre.get_auteur()}) - Dispo: {livre._nombre_exemplaires_disponibles}/{livre._nombre_exemplaires_total}")
    
    def charger_emprunts_actifs(self):
        self.emprunts_listbox.delete(0, tk.END)
        for emprunt in self.bibliotheque._emprunts_actifs.values():
            self.emprunts_listbox.insert(tk.END, f"{emprunt.get_id()} - {emprunt.get_livre().get_titre()} par {emprunt.get_etudiant().get_nom()} - Retour prévu: {emprunt._date_retour_prevue}")
    
    def charger_utilisateurs(self):
        self.utilisateurs_listbox.delete(0, tk.END)
        for user in self.bibliotheque._utilisateurs.values():
            user_type = "Étudiant" if isinstance(user, Etudiant) else "Employé"
            self.utilisateurs_listbox.insert(tk.END, f"{user.get_id()} - {user.get_prenom()} {user.get_nom()} ({user_type})")

    # Fonctions pour effacer les champs après l'ajout
    def effacer_champs_livre(self):
        self.isbn_entry.delete(0, tk.END)
        self.titre_entry.delete(0, tk.END)
        self.auteur_entry.delete(0, tk.END)
        self.annee_entry.delete(0, tk.END)
        self.exemplaires_entry.delete(0, tk.END)
        self.categorie_entry.delete(0, tk.END)

    def effacer_champs_utilisateur(self):
        self.user_id_entry.delete(0, tk.END)
        self.user_nom_entry.delete(0, tk.END)
        self.user_prenom_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliothequeApp(root)
    root.mainloop()