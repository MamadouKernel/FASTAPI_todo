from data.json_saver import JsonSaver
from data.schemas.todo import Todo
import logging
import uuid

class TodosCnt :
    # le constructeur initialise le titre et crée une instance JsonSaver avec le fichier 'todos.json'
    def __init__(self, title):
        self.title = title
        self.data_setter = JsonSaver('todos.json')

    # méthode pour récupérer toutes les données
    def get_all(self):
        # appelle la méthode find_all de l'instance JsonSaver pour récupérer toutes les données
        data = self.data_setter.find_all()
        # écrit un message dans les logs pour indiquer que les données ont été récupérées avec succès
        logging.info("donnée recuperer")
        # retourne les données récupérées
        return data
    
    # méthode pour ajouter une nouvelle tâche
    def add(self, todo:Todo):
        # écrit un message dans les logs pour indiquer qu'une nouvelle tâche va être ajoutée
        logging.info("todocnt: valeur index {index}")
        # génère un identifiant unique et l'assigne à la tâche
        todo.id = str(uuid.uuid4())
        # définit la valeur par défaut du champ completed à False
        todo.completed = False
        # appelle la méthode add de l'instance JsonSaver pour ajouter la tâche dans le fichier json
        self.data_setter.add(todo.id,todo.json())

    # méthode pour supprimer une tâche
    def delete(self, id:str):
        # appelle la méthode delete de l'instance JsonSaver pour supprimer la tâche correspondant à l'identifiant donné
        self.data_setter.delete(id)

    # méthode pour récupérer une tâche
    def get(self, id:str):
        # appelle la méthode find de l'instance JsonSaver pour récupérer la tâche correspondant à l'identifiant donné
        return self.data_setter.find(id)
    
    # méthode pour mettre à jour une tâche
    def update(self, id:str, todo:Todo):
        # assigne l'identifiant à la tâche
        todo.id = id
        # appelle la méthode update de l'instance JsonSaver pour mettre à jour la tâche dans le fichier json
        return self.data_setter.update(id, todo.json())
