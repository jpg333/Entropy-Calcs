# imports
import math


# calculate and return entropy of a string
def entropyOfString(string):
    # initialize entropy at 0
    entropy = 0

    # loop through all 256 possible ascii inputs
    for i in range(256):
        # p = probability = the frequency of any given ascii character divided by the total number of
        #   characters in the string
        p = string.count(chr(i)) / len(string)

        # if p = 0 then there were no occurrences of the character 'i' in this pass
        if p > 0:
            # if prob > 0, then calculate the shannon entropy for this character, and add it to total entropy
            #   (since the formula requires the summation of all the characters' entropies)
            entropy += -(p * math.log2(p))

    return entropy


def entropyOfProb(prob):
    #complement = float(1.0 - prob)
    entropy = 0
    entropy += -(prob * math.log2(prob))
    #entropy += -(complement * math.log2(complement))
    return entropy


def strToFloat(string):
    arr = string.split("/")
    flt = float(int(arr[0]) / int(arr[1]))
    return flt


def probCalc():
    itemList = []
    itemCount = int(input("Enter the number of unique items in your set: "))
    totalEntropy = 0

    print("Does every unique element have the same frequency?")

    # try-except to ensure valid input
    while True:
        try:
            sameOp = input("Enter 'y' or 'n': ")
            if sameOp not in ("y", "Y", "n", "N"):
                raise ValueError
        except ValueError:
            print("Error: choice must be 'y' or 'n'")
        else:
            break

    if sameOp in ("y", "Y"):
        while True:
            try:
                freq = int(input("Enter the frequency of each unique item: "))
            except ValueError:
                print("Error: Item frequency must be an integer")
            else:
                break
        setSize = freq * itemCount

        for i in range(itemCount):
            totalEntropy += entropyOfProb(freq / setSize)

        print("Set:\n"
              "Number of unique items:          " + str(itemCount) + "\n"
              "Frequency of each item:          " + str(freq) + "\n"
              "Total number of items in set:    " + str(setSize) + "\n"
              "Entropy of set:                  " + str(totalEntropy))

    else:
        for i in range(itemCount):
            while True:
                try:
                    itemList.append(
                        int(input("Enter the number frequency of item " + str(i + 1) + " in your set: ")))
                except ValueError:
                    print("Error: Item frequency must be an integer")
                else:
                    break

        setSize = sum(itemList)

        for i in range(len(itemList)):
            totalEntropy += entropyOfProb(itemList[i] / setSize)

        print("Set:")
        for i in range(len(itemList)):
            print("Item " + str(i+1) + ": " + str(itemList[i]))

        print("Entropy of set: " + str(totalEntropy))
    return


# driving method from which other functions are chained
def start():
    # initial selection
    print("Select an Entropy Calculator Type:\n"
          "1. Entropy based on probabilities\n"
          "2. Entropy based on item frequencies in a set\n"
          "3. Entropy based on symbol frequencies in a phrase\n")

    # try-except to ensure valid input
    while True:
        try:
            answer = input("Enter '1', '2', or '3': ")
            if answer not in ("1", "2", "3"):
                raise ValueError
        except ValueError:
            print("Error: choice must be '1', '2', or '3'")
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
        probCalc()

    else:
        # symbol frequency entropy
        phrase = input("Enter characters for entropy calculation: ")
        print("Entropy of\n'" + phrase + "'\nin bits is: " + str(entropyOfString(phrase)))


start()
