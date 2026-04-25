with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am Aaryav i ma 15")
file.close()

with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are.....")
    for line in data:
        words = line.split()
        print(words)
file.close()