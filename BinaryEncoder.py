def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def binary_to_text(binary):
    binary_values = binary.split(' ')
    text_result = ''.join(chr(int(binary, 2)) for binary in binary_values)
    return text_result

def main():
    print("Binary Code Translator")

    while True:
        print("\nChoose an option:")
        print("1. Text to Binary")
        print("2. Binary to Text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_text = input("Enter the text to convert to binary: ")
            binary_result = text_to_binary(input_text)
            print("Binary Code:", binary_result)

        elif choice == '2':
            input_binary = input("Enter the binary code to convert to text (separated by spaces): ")
            text_result = binary_to_text(input_binary)
            print("Text:", text_result)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
