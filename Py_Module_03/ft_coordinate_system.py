import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parameters = user_input.split(",")

        if len(parameters) != 3:
            print("Invalid syntax")
            continue

        coordinates: list[float] = []
        valid = True

        for parameter in parameters:
            parameter = parameter.strip()

            try:
                coordinates.append(float(parameter))
            except ValueError as error:
                print(f"Error on parameter '{parameter}': {error}")
                valid = False
                break

        if valid:
            return (
                coordinates[0],
                coordinates[1],
                coordinates[2],
            )


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    first_position = get_player_pos()
    print(f"Got a first tuple: {first_position}")

    x1, y1, z1 = first_position
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance_to_center = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance to center: {round(distance_to_center, 4)}")

    print("\nGet a second set of coordinates")
    second_position = get_player_pos()

    x2, y2, z2 = second_position

    distance_between = math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
        + (z2 - z1) ** 2
    )

    print(
        "Distance between the 2 sets of coordinates:",
        round(distance_between, 4),)