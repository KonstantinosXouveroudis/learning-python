class Father:
    def gardening(self):
        print("I enjoy gardening")

    def skills(self):
        print("Gardening, Programming")


class Mother:
    def cooking(self):
        print("I enjoy cooking")

    def skills(self):
        print("Cooking, Art")


class Child(Father, Mother):  # inheritance
    def sports(self):
        print("I enjoy sports")

    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")


if __name__ == '__main__':
    c = Child()
    c.gardening()
    c.cooking()
    c.sports()

    print("\nSkills of the child:")
    c.skills()

