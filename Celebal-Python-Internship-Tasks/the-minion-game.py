#Kevin and Stuart form substrings starting with vowels or consonants and score points.
def minion_game(string):
    vowels = "AEIOU"
    kevin = stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

minion_game(input().strip())
