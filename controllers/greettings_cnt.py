# Définition d'une classe nommée GreetingCont
class GreetingCont:

    # Définition d'une méthode spéciale __init__ qui est appelée lorsqu'une instance de la classe est créée.
    # Cette méthode prend un argument "title" de type string et l'assigne à l'attribut "self.title" de l'instance.
    def __init__(self, title: str):
        self.title = title

    # Définition d'une méthode nommée "say_hello" qui prend "self" en tant que premier argument (représentant l'instance de la classe).
    # Cette méthode retourne une chaîne de caractères "hello user".
    def say_hello(self):
        return "hello user"

    # Définition d'une méthode nommée "say_bye" qui prend "self" en tant que premier argument (représentant l'instance de la classe).
    # Cette méthode retourne une chaîne de caractères "bye user".
    def say_bye(self):
        return "bye user"
