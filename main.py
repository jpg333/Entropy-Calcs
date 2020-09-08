# imports
import math


# calculate and return entropy of a string
def entropyCalc(string):
    # initialize entropy at 0
    entropy = 0

    # loop through all 256 possible ascii inputs
    for i in range(256):
        # prob = the occurrence count of any given ascii character divided by the total number of
        #   characters in the string
        prob = string.count(chr(i))/len(string)

        # if prob = 0 then there were no occurrences of the character 'i' in this pass
        if prob > 0:
            # if prob > 0, then calculate the shannon entropy for this character, and add it to total entropy
            #   (since the formula requires the summation of all the characters' entropies)
            entropy += -(prob * math.log2(prob))

    return entropy


phrase = input("Enter characters for entropy calculation: ")

print("Entropy of '" + phrase + "' is:\n" + str(entropyCalc(phrase)))


