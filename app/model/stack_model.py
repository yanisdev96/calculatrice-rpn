from datetime import datetime


class StackModel:
    """model de donné pour la pile """
    
    def __init__(self, id):
        self.id = id
        self.elements = []
        self.created_at = datetime.now()