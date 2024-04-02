def calculate_cube_volume(length):
    # Calculate the volume of the cube
    volume_cm = length ** 3
    # Convert volume from cm^3 to bees (where each bee is 3cm)
    volume_bees = volume_cm / 3
    return volume_bees

def main():
    # Prompt the user to enter the length of one side of the cube
    length = float(input("Enter the length of one side of the cube in cm: "))

    # Calculate the volume of the cube in bees
    volume_bees = calculate_cube_volume(length)

    # Print the result
    print(f"The volume of the cube is {volume_bees} bees.")

if __name__ == "__main__":
    main()