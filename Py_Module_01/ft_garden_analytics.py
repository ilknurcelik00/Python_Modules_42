class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def record_grow(self) -> None:
            self.__grow_calls += 1

        def record_age(self) -> None:
            self.__age_calls += 1

        def record_show(self) -> None:
            self.__show_calls += 1

        def display(self, name: str) -> None:
            print("[statistics for " + name + "]")
            print("Stats:", self.__grow_calls, "grow,",
                  self.__age_calls, "age,",
                  self.__show_calls, "show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.__statistics = Plant.Statistics()

    def show(self) -> None:
        h = round(self._height, 1)
        print(self.name + ":", str(h) + "cm,", self._age, "days old")
        self.__statistics.record_show()

    def grow(self, amount: float = 8.0) -> None:
        self._height = self._height + amount
        self.__statistics.record_grow()

    def age(self, days: int = 1) -> None:
        self._age = self._age + days
        self.__statistics.record_age()

    def show_statistics(self) -> None:
        self.__statistics.display(self.name)

    @staticmethod
    def check_year(age: int) -> None:
        if age > 365:
            print("Is", age, "days more than a year? -> True")
        else:
            print("Is", age, "days more than a year? -> False")

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
        print(" Color:", self.color)
        if self._bloomed:
            print("", self.name, "is blooming beautifully!")
        else:
            print("", self.name, "has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.__shade_calls = 0

    def produce_shade(self) -> None:
        h = round(self._height, 1)
        t = round(self.trunk_diameter, 1)
        print("Tree", self.name, "now produces a shade of",
              str(h) + "cm long and", str(t) + "cm wide.")
        self.__shade_calls += 1

    def show(self) -> None:
        super().show()
        print(" Trunk diameter:",
              str(round(self.trunk_diameter, 1)) + "cm")

    def show_statistics(self) -> None:
        super().show_statistics()
        print(self.__shade_calls, "shade")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed_number = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed_number = 42

    def grow(self) -> None:
        super().grow(30.0)

    def age(self) -> None:
        super().age(20)

    def show(self) -> None:
        super().show()
        print("Seeds:", self.seed_number)


def display_statistics(plant: Plant) -> None:
    plant.show_statistics()


if __name__ == "__main__":
    print("\n=== Garden statistics ===")
    print("=== Check year-old ===")
    Plant.check_year(30)
    Plant.check_year(400)

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)
