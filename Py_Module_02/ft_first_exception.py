def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperture() -> None:
    temp_str = "25"
    try:
        print("Input data is '" + temp_str + "'")
        temp = input_temperature(temp_str)
        print("Temperature is now", temp, "°C\n")
    except Exception:
        print("Caught input_temperature error: invalid literal "
              "for int() with base 10:'" + temp_str + "'\n")

    temp_str = "abc"
    try:
        print("Input data is '" + temp_str + "'")
        temp = input_temperature(temp_str)
        print("Temperature is now", temp, "°C")
    except Exception:
        print("Caught input_temperature error: invalid literal "
              "for int() with base 10:'" + temp_str + "'\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperture()
    print("All tests completed- program didn't crash!")
