# with open("wordlist.txt") as wordlist:
import re
wordlist = open("wordlist.txt").read()
# length = int(input("Enter Word Length: "))
Letters = "abcdefghijklmnopqrstuvwxyz"
words = input("Enter Words Entered So Far split with a comma: ").lower()
words = ''.join(str(e) for e in re.split("\\s", words))
known, valid = 0,0
def unique(word_list):
    max_unique_count = 0
    word_with_max_unique = ""

    for word in word_list:
        unique_letters_count = len(set(word))
        if unique_letters_count > max_unique_count:
            max_unique_count = unique_letters_count
            word_with_max_unique = word

    return word_with_max_unique
def filter2(word_list, letters):
    filtered_words = []
    for word in word_list:
        if all(letter in word for letter in letters):
            filtered_words.append(word)
    return filtered_words
def remLetters():
    global Letters
    Letters = list(Letters)
    for i in words:
        if i not in known:
            try:
                Letters.pop(Letters.index(i))
            except ValueError:
                pass
    Letters = ''.join(str(e) for e in Letters)
def filter(word_list, letters):
    pattern = r'^[' + letters + ']+$'
    filtered_words = [word for word in word_list if re.match(pattern, word)]
    return filtered_words

def guessAll(known, valid):
    finalReg = ""
    for i in valid:
        if i == "_":
            finalReg += f"[{Letters}]"
        else:
            finalReg += i
    return filter2(re.findall(finalReg, wordlist), known)

while True:
    known=input("Enter All Letters known to be present:")
    valid = list(input(f"Enter Word Known So Far (enter '_' if unknown): "))
    remLetters()
    guess = unique(guessAll(known, valid))
    print("Guess Word:", guess)
    a = input("Press Any Button To Guess. Press Q to quit: ")
    words += guess
    print(words)
    if a == "Q" or a == "q":
        print(a)
        exit()
    else:
        continue
