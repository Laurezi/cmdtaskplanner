import argparse
import json
import os
# import pandas as pd

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
def create_planning(args):
    """
    Comment
    """
    # Check if the file already exists
    file_exist, json_file_name  = check_file_existence(args.planning)
    
    if file_exist:   
        print('Ce planning existe déjâ')
    else:
        # create file and put empty list
        with open(json_file_name, 'w') as write_file:
            json.dump({'tasks': []}, write_file)
            print('Planning créé')
        
def add_task(args):
    """
    Comment
    """
    # Check if the file exists
    file_exist, json_file_name  = check_file_existence(args.planning)
    
    if file_exist:
         # open file read old tasks and put new one
        with open(json_file_name, "r+") as file:
            # Get old tasks
            current_tasks = json.load(file)
            # append new task on old one
            current_tasks['tasks'].append({'label': args.label,'date': args.date,'status': 'en cours'})
            # Sets file's current position at offset
            file.seek(0)
            # write on json file
            json.dump(current_tasks, file, ensure_ascii=False, indent=4)
            print('tâche ajoutée')
    else:
        print("Ce planning n'existe pas, veuillez le créer avec la commande create -p nom_du_planning")       
    

def remove_task(args):
    # Check if the file exists
    file_exist, json_file_name  = check_file_existence(args.planning)
    
    if file_exist:
        # open file read old tasks and put new one
        with open(json_file_name, "r+") as file:
            # Get old tasks
            current_tasks = json.load(file)
            # remove task by id
            remain_task = [task for i, task in enumerate(current_tasks['tasks']) if i != args.id-1]
            #Check if task is truly removed
            is_remove = len(remain_task) != len(current_tasks['tasks'])
            # replace old task with remain task list
            current_tasks['tasks'] = remain_task
            # Sets file's current position at offset
            file.seek(0)
            # Truncate the file (remove existing content)
            file.truncate()
            # write on json file
            json.dump(current_tasks, file, ensure_ascii=False, indent=4)
            if is_remove:
                print('tâche supprimé')
            else:
                print("cette tâche n'existe pas")
    else:
        print("Ce planning n'existe pas, veuillez le créer avec la commande create -p nom_du_planning") 

def modif_task(args):
    print(args)

def list_task(args):
    """
    Comment
    """
    # Check if the file exists
    file_exist, json_file_name  = check_file_existence(args.planning)
    
    if file_exist:
         # open file read old tasks and put new one
        with open(json_file_name, "r") as file:
            # Get old tasks
            current_tasks = json.load(file)
            # Format and print all tasks
            print(f"####################Liste des tâches###################")
            print("id       label                       date                    status")
            for i, task in enumerate(current_tasks['tasks']):
                print(f"{i+1}       {task['label']}                     {task['date']}          {task['status']}")
    else:
        print("Ce planning n'existe pas, veuillez le créer avec la commande create -p nom_du_planning")

def mark_done(args):
    # Check if the file exists
    file_exist, json_file_name  = check_file_existence(args.planning)
    
    if file_exist:
        # open file read old tasks and put new one
        with open(json_file_name, "r+") as file:
            # Get old tasks
            current_tasks = json.load(file)
            try:
                # put status task done by id
                current_tasks['tasks'][args.id - 1]['status'] = 'terminé'
                # Sets file's current position at offset
                file.seek(0)
                # Truncate the file (remove existing content)
                file.truncate()
                # write on json file
                json.dump(current_tasks, file, ensure_ascii=False, indent=4)
                print(f"tâche {args.id} marquée terminée")
            except:
                print("cette tâche n'existe pas")
            
    else:
        print("Ce planning n'existe pas, veuillez le créer avec la commande create -p nom_du_planning") 

def delete_planning(args):
    # Check if the file exists
    file_exist, json_file_name  = check_file_existence(args.planning)
    
    if file_exist:
        try:
            os.remove(json_file_name)
            print(f"Planning  {args.planning} supprimé")
        except:
            print("Ce planning n'existe pas")
            
    else:
        print("Ce planning n'existe pas, veuillez le créer avec la commande create -p nom_du_planning")

def update_cmdtaskplanner(args):
    print(args)
    
def convert_file(args):
    print(args)
    # # Check if the file exists
    # file_exist, json_file_name  = check_file_existence(args.planning)
    
    # if file_exist:
    #     df_json = pd.read_json(json_file_name)
    #     if args.format == 'excel':
    #         df_json.to_excel("sport.xlsx", index=False)   
    #         print(f"Fichier converti en {args.format}")   
    # else:
    #     print("Ce planning n'existe pas, veuillez le créer avec la commande create -p nom_du_planning")

###########################OTHER FUNCTION AND VARIABLES##################### 
# Function
def check_file_existence(planning_args):
    """
    comment 
    """
    # Get file name from args
    json_file_name = f'{planning_args}.json'
    
    # Check if the file already exists
    return {os.path.exists(json_file_name), json_file_name}

#Variables
# tasks data
tasks_data = []

# Arguments initialization in dedicated function
def setup_args():
    parser = argparse.ArgumentParser(prog='cmdtaskplanner',description='gestionnaire des tâches en ligne de commande', epilog="Ceci est l'aide pour l'utilisation de cmdtaskplanner")
    # Subparsers
    subparsers = parser.add_subparsers()
    
    # Create parser
    subparsers_create = subparsers.add_parser("create", help="créer un planning")
    subparsers_create.add_argument('-p', '--planning', type=str, required=True, help="nom du fichier de planning")
    subparsers_create.set_defaults(func=create_planning)
    
    # Add parser
    subparsers_add = subparsers.add_parser('add', help="Ajouter une tâche")
    subparsers_add.add_argument('-p', '--planning', type=str, required=True, help="nom du fichier de planning")
    subparsers_add.add_argument('-l', '--label', type=str, required=True, help="le titre de la tâche")
    subparsers_add.add_argument('-d', '--date', type=str, required=True, help="la date de début de la tâche")
    subparsers_add.set_defaults(func=add_task)
    
    # Remove parser
    subparsers_remove = subparsers.add_parser('remove', help="Supprimer une tâche")
    subparsers_remove.add_argument('--planning', '-p', type=str, required=True, help="nom du fichier de planning")
    subparsers_remove.add_argument('--id', '-i', type=int, required=True, help="l'identifiant de la tâche")
    subparsers_remove.set_defaults(func=remove_task)
    
    # Modify parser
    subparsers_modify = subparsers.add_parser('modify', help="Modifier une tâche")
    subparsers_modify.add_argument('--planning', '-p', type=str, help="nom du fichier de planning")
    subparsers_modify.add_argument('--label', '-l', type=str, help="le titre de la tâche")
    subparsers_modify.add_argument('--date', '-d', type=str, help="la date de début de la tâche")
    subparsers_modify.add_argument('--id', '-i', type=int, help="l'identifiant de la tâche à modifier")
    subparsers_modify.add_argument('--status', '-s', type=str, choices=["en cours", "terminé"] ,help="status de la tâche")
    subparsers_modify.set_defaults(func=modif_task)
    
    # list parser
    subparsers_list = subparsers.add_parser('list', help="Lister les tâches")
    subparsers_list.add_argument('--planning', '-p', type=str, help="nom du fichier de planning")
    subparsers_list.set_defaults(func=list_task)
    
    # done parser
    subparsers_done = subparsers.add_parser('done', help="Marquer une tâche done")
    subparsers_done.add_argument('--planning', '-p', type=str, help="nom du fichier de planning")
    subparsers_done.add_argument('--id', '-i', type=int, help="l'identifiant de la tâche à modifier")
    subparsers_done.set_defaults(func=mark_done)
    
    # delete parser
    subparsers_delete = subparsers.add_parser('delete', help="Supprimer un planning")
    subparsers_delete.add_argument('--planning', '-p', type=str, required=True, help="nom du fichier de planning")
    subparsers_delete.set_defaults(func=delete_planning)
    
    # update parser
    subparsers_update = subparsers.add_parser('update', help="Mettre à jour le programme")
    subparsers_update.set_defaults(func=update_cmdtaskplanner)
    
    # Convert parser
    # Convert parser
    subparsers_convert = subparsers.add_parser('convert', help="convertir le planning dans un autre format")
    subparsers_convert.add_argument('--planning', '-p', type=str, required=True, help="nom du fichier de planning")
    subparsers_convert.add_argument('-f', '--format', type=str, choices=['excel'] ,help="le format de destination")
    subparsers_convert.set_defaults(func=convert_file)
    
    return parser

parser = setup_args()
args = parser.parse_args()
args.func(args)
# print(args)


