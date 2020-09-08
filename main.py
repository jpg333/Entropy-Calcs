# imports
import math


# calculate and return entropy of a string
def entropyOfString(string):
    # initialize entropy at 0
    entropy = 0

    # loop through all 256 possible ascii inputs
    for i in range(256):
        # p = probability = the occurrence count of any given ascii character divided by the total number of
        #   characters in the string
        p = string.count(chr(i)) / len(string)

        # if p = 0 then there were no occurrences of the character 'i' in this pass
        if p > 0:
            # if prob > 0, then calculate the shannon entropy for this character, and add it to total entropy
            #   (since the formula requires the summation of all the characters' entropies)
            entropy += -(p * math.log2(p))

    return entropy


def entropyOfProb(prob):
    entropy = 0
    entropy += -(prob * math.log2(prob))
    return entropy


def strToFloat(string):
    arr = string.split("/")
    flt = float(int(arr[0]) / int(arr[1]))
    return flt


# driving method from which other functions are chained
def start():
    # initial selection
    print("Select an Entropy Calculator Type:\n"
          "1. Entropy based on probabilities\n"
          "2. Entropy based on symbol frequencies in a phrase\n")

    # try-except to ensure valid input
    while True:
        try:
            answer = input("Enter '1' or '2': ")
            if answer not in ("1", "2"):
                raise ValueError
        except ValueError:
            print("Error: please enter '1' or '2'")
        else:
            break

    # decision handling for probability or symbol frequency entropy
    if answer == '1':
        # probability entropy
        odds = input("\nEnter probability: ")
        # preserve format of user input
        inp = odds

        try:
            # if input is an integer or decimal
            float(odds)
        except ValueError:
            # if input is a fraction (ex. '1/2')
            odds = strToFloat(odds)

        print("Entropy of " + str(inp) + " in bits is:\n" + str(entropyOfProb(float(odds))))

    elif answer == '2':
        # symbol frequency entropy
        phrase = input("Enter characters for entropy calculation: ")
        print("Entropy of '" + phrase + "' in bits is:\n" + str(entropyOfString(phrase)))
    else:
        return 0


start()
