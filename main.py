def check_parity(binary_number):
    """
    Checks the parity of an 8-bit binary number.
    :param binary_number: A string of length 8 representing a binary number.
    :return: "Even" if the number of 1-bits is even, "Odd" otherwise.
    """
    # Initialize XOR result to 0
    result = 0

    # Calculate XOR for all bits in the number
    for bit in binary_number:
        result ^= int(bit)  # XOR the current result with the bit

    # If XOR result is 0, the number of 1-bits is even
    return "Even" if result == 0 else "Odd"


def main():
    """
    Main function of the program.
    """
    print("Binary Parity Checker")
    print("Enter an 8-bit binary number (e.g., 10101100):")

    try:
        # Prompt the user to enter a binary number
        binary_number = input("Enter the number: ")

        # Validate the input: it must be exactly 8 bits consisting only of 0s and 1s
        if len(binary_number) != 8 or not all(bit in '01' for bit in binary_number):
            raise ValueError("Input must be an 8-bit binary number (only 0s and 1s).")

        # Call the function to check parity
        parity = check_parity(binary_number)

        # Display the result
        print(f"The number of 1-bits in the binary number is {parity.lower()}.")

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()


