"""
    Type de commentaire pour docstrings.  
"""
# Génération d'une documentation : Sphynx & Docstrings (à regarder)
'''
Install l'extension PythonDocsString Generator si sous VScode.
https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

Sinon,
pip install sphinx 
sphinx-quickstart
extensions = ['sphinx.ext.autodoc'] (inclusion des docsstrings, configuration de conf.py)
makehtml
'''

# from module import MyClass

def main():
    '''Point d'entrée principal du programme.'''
    # mon_obj = MyClass()




if __name__ == "__main__" : 
    main()



# Rappel sur les Classes en python, on les placera à la racine du projet. 
'''
class MyClass:
    """Exemple de classe dans module1.py."""

    def __init__(self, name: str):
        """
        Initialise l'instance de la classe.

        Args:
            name (str): Le nom à associer à cette instance.
        """
        self.name = name

    def method(self):
        """Affiche un message avec le nom."""
        print(f"Hello from {self.name} in MyClass1!")
'''
