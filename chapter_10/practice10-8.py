cat = 'cats.txt'
dog = 'dogs.txt'
try:
        
    with open(cat) as cats:
        for line in cats:
            print(line.strip())
    
    with open(dog) as dogs:
        for line in dogs:
            print(line.strip())
except FileNotFoundError:
    print("Sorry, can't find file.")