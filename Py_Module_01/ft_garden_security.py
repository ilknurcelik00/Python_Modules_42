class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0
        h = str(round(self._height, 1))
        n = self.name
        print("Plant created:", n + ":", h + "cm,", self._age, "days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value < 0:
            print(self.name + ": Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(value)
            print("Height updated: " + str(int(value)) + "cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(self.name + ": Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print("Age updated: " + str(value) + " days")

    def show(self) -> None:
        h = str(round(self._height, 1))
        print(self.name + ":", h + "cm,", self._age, "days old")

    def current_state(self) -> None:
        h = str(round(self._height, 1))
        n = self.name
        print("Current state:", n + ":", h + "cm,", self._age, "days old")


if __name__ == "__main__":
    print("\n=== Garden Security System ===")
    plant1 = Plant("Rose", 15.0, 10)

    print()
    plant1.set_height(25)
    plant1.set_age(30)

    print()
    plant1.set_height(-5)
    plant1.set_age(-3)

    print()
    plant1.current_state()
