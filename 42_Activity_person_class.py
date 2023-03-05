class Person:
    # def __init__(self, name, speech):
    def __init__(self, name):
        self.name = name
        # self.speech = speech
    def talk(self, speech):
        print(speech)


individual = Person("Mary Jane")
individual.talk(f"Hello Everyone!, I am {individual.name}")