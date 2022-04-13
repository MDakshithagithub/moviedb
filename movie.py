class Movie:
    """A sample Movie class"""

    def __init__(self, name, actor, actress, director, year):
        self.name = name
        self.actor = actor
        self.actress = actress
        self.director= director
        self.year = year

    
    def __rtrn__(self):
        return "Movie('{}', '{}', {})".format(self.name, self.actor, self.actress,self.director,self.year)