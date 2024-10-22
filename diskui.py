import tkinter as tk
from tkinter import messagebox

def calculer_pourcentage():
    try:
        espace_total = float(entree_total.get())
        espace_utilise = float(entree_utilise.get())
        
        if espace_total <= 0:
            raise ValueError("L'espace total doit être supérieur à zéro.")
        
    
        pourcentage = (espace_utilise / espace_total) * 100
        
    
        espace_disponible = espace_total - espace_utilise
        
    
        messagebox.showinfo("Résultat", f"Pourcentage d'utilisation : {pourcentage:.2f}%\nEspace disponible : {espace_disponible:.2f} Go")
        
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

fenetre = tk.Tk()
fenetre.title("Calculateur de pourcentage d'utilisation du disque")

label_total = tk.Label(fenetre, text="Espace total (en Go) :")
label_total.pack(pady=5)

entree_total = tk.Entry(fenetre)
entree_total.pack(pady=5)

label_utilise = tk.Label(fenetre, text="Espace utilisé (en Go) :")
label_utilise.pack(pady=5)

entree_utilise = tk.Entry(fenetre)
entree_utilise.pack(pady=5)

bouton_calculer = tk.Button(fenetre, text="Calculer", command=calculer_pourcentage)
bouton_calculer.pack(pady=20)

if __name__ == '__main__':
    fenetre.mainloop()