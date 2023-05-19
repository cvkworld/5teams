with open("SampleTextFile.txt", "r") as f:
    for line in f:
        words = line.split()
        for word in words:
            print(word)
