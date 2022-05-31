class Person:
    def __init__(self, name):
        self.name = name
        print(f"Constructor call for {self.name}.")

    def talk(self):
        print(f"Talk call for {self.name}.")


Person("spk").talk()
Person("psk").talk()
