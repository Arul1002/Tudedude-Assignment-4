with open("output.txt", "w") as file:
    user_input = input("Enter text to write to the file: ")
    file.write(user_input + "\n")
    print("Data succesfully witten to output.txt.")

with open("output.txt", "a") as file:
    additional_data = input("Enter additional text to append to the file: ")
    file.write(additional_data + "\n")
    print("Data succesfully appended")

with open("output.txt", "r") as file:
    print("\nFinal content of the file:")
    print(file.read())