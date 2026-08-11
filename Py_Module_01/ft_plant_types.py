class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._ages = age

    def show(self) -> None:
        h = round(self._height, 1)
        print(self.name + ":", str(h) + "cm,", self._ages, "days old")

    def grow(self) -> None:
        self._height = self._height + 2.1

    def age(self) -> None:
        self._ages = self._ages + 1


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print("Color:", self.color)
        if self._bloomed:
            print("", self.name, "is blooming beautifully!")
        else:
            print("", self.name, "has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        h = round(self._height, 1)
        t = round(self.trunk_diameter, 1)
        print("Tree", self.name, "now produces a shade of",
              str(h) + "cm long and", str(t) + "cm wide.")

    def show(self) -> None:
        super().show()
        print(" Trunk diameter:", str(round(self.trunk_diameter, 1)) + "cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()

    def show(self) -> None:
        super().show()
        print(" Harvest season:", self.harvest_season)
        print(" Nutritional value:", self.nutritional_value)


if __name__ == "__main__":
    print("\n=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
