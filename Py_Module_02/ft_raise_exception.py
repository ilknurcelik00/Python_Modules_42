def input_temperature(temp_str: str) -> int:
    temp_val = int(temp_str)

    if temp_val > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    elif temp_val < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")

    return temp_val


def test_temperture() -> None:
    temp_str = "25"
    try:
        print(f"Input data is '{temp_str}'")
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print()

    temp_str = "abc"
    try:
        print(f"Input data is '{temp_str}'")
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print()

    temp_str = "100"
    try:
        print(f"Input data is '{temp_str}'")
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print()

    temp_str = "-50"
    try:
        print(f"Input data is '{temp_str}'")
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperture()
    print("All tests completed - program didn't crash!")
