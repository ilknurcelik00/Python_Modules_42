class Plant:
    def __init__(self, name: str, height: float, ages: int) -> None:
        self.name = name
        self.height = height
        self.ages = ages

    def show(self) -> None:
        h = round(self.height, 1)
        print("Created: " + self.name + ": " + str(h) + "cm, "
              + str(self.ages) + " days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    garden = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    for plant in garden:
        plant.show()
