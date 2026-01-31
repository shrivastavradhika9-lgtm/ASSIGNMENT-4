text=input("Enter text to write to the file: ")
with open('output.txt', 'w') as f:
    f.write(text)
print("data successfully written to 'output.txt'.")
additional_text = input("Enter additional text to append to the file: ")
with open('output.txt', 'a') as f:
    f.write('\n' + additional_text)
print("Data successfully appended.\n")
print("final content of 'output.txt':")
with open('output.txt', 'r') as f:
        content = f.read()
        print(content)