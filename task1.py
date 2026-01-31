try:
    with open('sample.txt', 'r') as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")