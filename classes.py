class Human:
    def __init__(self, name, occupation):  # "self" means the class itself
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "tennis player":
            print(f"{self.name} plays tennis.")
        elif self.occupation == "actor":
            print(f"{self.name} shoots movies.")

    def speaks(self):
        print(f'{self.name} says "How are you?"')


if __name__ == '__main__':
    tom = Human("Tom Cruise", "actor")
    tom.do_work()
    tom.speaks()

    maria = Human("Maria Sharapova", "tennis player")
    maria.do_work()
    maria.speaks()

