class Animal:
    def __init__(self, h):
        self.habitat = h

    def show_habitat(self):
        print(f"Habitat: {self.habitat}")

    def sound(self):
        print("Generic animal sound here.")


class Dog(Animal):
    def __init__(self):
        super().__init__("Owner's house.")

    def sound(self):
        print("Woof woof!")


if __name__ == '__main__':
    d = Dog()
    d.show_habitat()
    d.sound()

