class Plant:
    def __init__(self, name: str, height: float, ages: int) -> None:
        self.name = name
        self.height = height
        self.ages = ages

    def show(self) -> None:
        h = round(self.height, 1)
        print(self.name + ":", str(h) + "cm,", self.ages, "days old")

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.ages = self.ages + 1


if __name__ == "__main__":
    print("\n=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 30)
    first = plant1.height
    plant1.show()
    for i in range(1, 8):
        print("=== Day", i, "===")
        plant1.grow()

        plant1.age()

        plant1.show()
    growth = plant1.height - first
    print("Growth this week:", str(round(growth, 1)) + "cm")
