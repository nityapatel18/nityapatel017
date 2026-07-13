Questions = [
    ["What is the capital of india?", "Delhi", "Mumbai", "Kolkata", "Chennai", 1],
    ["What is the largest planet in our solar system?", "Jupiter", "Saturn", "Neptune", "Uranus", 1],
    ["What is the capital of france?", "Paris", "London", "Berlin", "Rome", 1],
    ["What is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["What is the currency of japan?", "Yen", "Dollar", "Euro", "Pound", 1],
    ["What is the highest mountain in the world?", "Mount Everest", "K2", "Kangchenjunga", "Lhotse", 1],
    ["What is the largest desert in the world?", "Sahara Desert", "Gobi Desert", "Kalahari Desert", "Arabian Desert", 1],
    ["What is the capital of australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", 3],
    ["What is the largest country in the world by land area?", "Russia", "Canada", "China", "United States", 1],
    ["What is the smallest country in the world by land area?", "Vatican City", "Monaco", "Nauru", "San Marino", 1],
    ["What is the largest mammal in the world?", "Blue Whale", "Elephant", "Giraffe", "Hippopotamus", 1],
    ["What is the largest bird in the world?", "Ostrich", "Eagle", "Albatross", "Penguin", 1],
    ["What is the largest reptile in the world?", "Saltwater Crocodile", "Komodo Dragon", "Green Anaconda", "Nile Crocodile", 1],
    ["What is the largest fish in the world?", "Whale Shark", "Great White Shark", "Manta Ray", "Tiger Shark", 1],
    ["What is the largest amphibian in the world?", "Chinese Giant Salamander", "Axolotl", "Hellbender", "Cane Toad", 1],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(len(Questions)):
    print(f"Question {i+1}: {Questions[i][0]}")
    print(f"1. {Questions[i][1]}")
    print(f"2. {Questions[i][2]}")
    print(f"3. {Questions[i][3]}")
    print(f"4. {Questions[i][4]}")
    answer = int(input("Enter your answer (1-4): "))
    if answer == Questions[i][5]:
        money = levels[i]
        print(f"Correct! You have won Rs. {money}.")
    else:
        print("Incorrect answer. Game over.")
        break 
