import argparse

"""
Fonctionnalités
- Créer un planning
- Ajouter des tâches d'un planning
- Supprimer une tâche d'un planning
- Modifier une tâche d'un planning
- Afficher la liste des tâche d'un planning
- Marquer une tâche terminée
- Supprimer un planning
- Mettre à jour cmdtaskplanner

Format du fichier planning :
[{label: "Aller à l'espace", "30-01-2024", "termine"},
{label: "rendre devoir", "30-01-2024", "en cours"}]
"""

# Functions for all operations
# Créer planning : create file.json with this format {id, label, deadline, status}
def create_planning():
    print('ok')

def add_task():
    print('ok')

def remove_task():
    print('ok')

def modif_task():
    print('ok')

def print_task():
    print('ok')

def mark_done():
    print('ok')

def delete_planning():
    print('ok')

def update_cmdtaskplanner():
    print('ok')

# Arguments initialization
parser = argparse.ArgumentParser(prog='cmdtaskplanner',description='gestionnaire des tâches en ligne de commande', epilog="Ceci est l'aide pour l'utilisation de cmdtaskplanner")

