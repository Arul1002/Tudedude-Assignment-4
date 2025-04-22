try:

    with open('sample.txt','r') as file:
        print('Reading a file:')
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")