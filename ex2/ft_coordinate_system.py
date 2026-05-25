import math


def get_player_pos():
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts = user_input.split(",")

        # Önce syntax kontrolü
        try:
            parts[0]
            parts[1]
            parts[2]
        except IndexError:
            print("Invalid syntax")
            continue

        # Fazla eleman kontrolü
        try:
            parts[3]
            print("Invalid syntax")
            continue
        except IndexError:
            pass

        # Float conversion
        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())

            return (x, y, z)

        except ValueError as error:
            invalid_value = ""

            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    invalid_value = part.strip()
                    break

            print(
                f"Error on parameter "
                f"'{invalid_value}': {error}"
            )


print("=== Game Coordinate System ===")

print("Get a first set of coordinates")
first_pos = get_player_pos()

print(f"Got a first tuple: {first_pos}")

print(
    f"It includes: "
    f"X={first_pos[0]}, "
    f"Y={first_pos[1]}, "
    f"Z={first_pos[2]}"
)

distance_to_center = math.sqrt(
    first_pos[0] ** 2
    + first_pos[1] ** 2
    + first_pos[2] ** 2
)

print(
    f"Distance to center: "
    f"{round(distance_to_center, 4)}"
)

print("Get a second set of coordinates")
second_pos = get_player_pos()

distance_between = math.sqrt(
    (second_pos[0] - first_pos[0]) ** 2
    + (second_pos[1] - first_pos[1]) ** 2
    + (second_pos[2] - first_pos[2]) ** 2
)

print(
    "Distance between the 2 sets of coordinates:",
    round(distance_between, 4)
)