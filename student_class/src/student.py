class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        self._strings =  {
            "talk" : "I can talk!",
            "favourite" : "I love "
        }
        
    def talk(self):
        return self._strings["talk"]
    
    def say_favourite_language(self, language):
        return self._strings["favourite"] + language