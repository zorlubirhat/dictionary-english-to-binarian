#------------------------------------------------------------#
# Student Name: Birhat ZORLU
# Student ID: 21427564
# BBM103 Introduction to Programming Laboratory I, Fall 2016 
# Assignment 3: Mission: Save the Earth
#------------------------------------------------------------#

# Importing the sys module that supports reading command-line arguments
import sys

infile = sys.argv[1]
infile2 = sys.argv[2]
infile3 = sys.argv[3]
outfile = "computations.txt"

dict = {}

binarian_words = []
english_words = []

calculations = []
calculations2 = []
#-------------------------------------------------#
#                   Functions                     #
#-------------------------------------------------#


def read_dictionary(file_handle):

    input_file = open(file_handle, "r")

    for line in input_file:
        items = line.strip().split(" ")
        dict[items[0]] = items[1]

    for key, value in dict.items():
        binarian_words.append(key)
        english_words.append(value)


def binary_to_decimal(number):

    list = []

    for i in str(number):
        list.append(i)

    bin = 0
    count = 0
    for digit in list[::-1]:
        bin += float(digit)*(2**count)
        count += 1
    return bin


def decimal_to_binary(number):

    decimal = " "
    while int(number) != 0:
        remainder = number % 2
        number = number // 2
        decimal += str(remainder)
    return decimal[::-1]


def ly_to_km(distance):

    dist = distance * 9.4607e+12
    return "{:.6e}".format(dist)


def binarian_to_english(text):

    input_file = open(text, "r")
    output_file = open("binarian_message.txt", "w")
    message = []

    for line in input_file.readlines():
        word = line.rstrip("\n")
        words = word.split(" ")
        for a in words:
            if word[0] == "+":
                calculations.append(a)
            elif word[0] == "#":
                pass
            else:
                message.append(a)
                message.append(" ")
        if word[0] != "+" and word[0] != "#":
            message.append("\n")

    for text_message in message:
        if text_message not in binarian_words:
            print(text_message, end="")
            output_file.write(text_message)
        else:
            mess = binarian_words.index(text_message)
            print(english_words[mess], end="")
            output_file.write(english_words[mess])
    print("")
    return output_file


def english_to_binarian(text):

    input_file = open(text, "r")
    output_file = open("message.txt", "w")

    for line in input_file.readlines():
        word = line.rstrip("\n")
        word = word.strip().split(" ")
        for words in word:
            words = words.lower()
            if words[-1] == ",":
                words = words[:-1]
                if words not in english_words:
                    print(words, end=" ")
                    output_file.write(words)
                else:
                    ind = english_words.index(words)
                    print(binarian_words[ind], end=" ")
                    output_file.write(binarian_words[ind])
                    output_file.write(" ")
            elif words[-1] == ".":
                words = words[:-1]
                if words not in english_words:
                    print(words, end=" ")
                    output_file.write(words)
                    output_file.write(" ")
                else:
                    ind = english_words.index(words)
                    print(binarian_words[ind], end=" ")
                    output_file.write(binarian_words[ind])
                    output_file.write(" ")
            elif words[-1] == "?":
                words = words[:-1]
                if words not in english_words:
                    print(words, end=" ")
                    output_file.write(words)
                    output_file.write(" ")
                else:
                    ind = english_words.index(words)
                    print(binarian_words[ind], end=" ")
                    output_file.write(binarian_words[ind])
                    output_file.write(" ")
            elif words[-1] == "!":
                words = words[:-1]
                if words not in english_words:
                    print(words, end=" ")
                    output_file.write(words)
                    output_file.write(" ")
                else:
                    ind = english_words.index(words)
                    print(binarian_words[ind], end=" ")
                    output_file.write(binarian_words[ind])
                    output_file.write(" ")
            elif words == "i":
                words = words.capitalize()
                print(words, end=" ")
                output_file.write(words)
                output_file.write(" ")
            else:
                if words not in english_words:
                    try:
                        x = decimal_to_binary(int(words))
                        print(x, end="")
                        output_file.write(x)
                        output_file.write("")
                    except ValueError:
                        print(words, end=" ")
                        output_file.write(words)
                        output_file.write(" ")
                else:
                    ind = english_words.index(words)
                    print(binarian_words[ind], end=" ")
                    output_file.write(binarian_words[ind])
                    output_file.write(" ")
        print(end="\n")
        output_file.write("\n")
    return output_file


#-------------------------------------------------#
#                 Main Program                    #
#-------------------------------------------------#

read_dictionary(infile)
binarian_to_english(infile2)

for gerek in calculations:
    if gerek in binarian_words:
        x = binarian_words.index(gerek)
        calculations2.append(english_words[x])
    else:
        calculations2.append(gerek)
for sayi in calculations2:
    a = calculations2.index("temperature")
    b = calculations2.index("orbital-speed")
    c = calculations2.index("distance")

out2 = "Data about Binarian planet:\n" \
           "Distance from the Earth: {} km\n" \
           "Planet temperature: {} degrees Celsius\n" \
           "Orbital speed: {} km/s\n"
print(out2.format(ly_to_km(int(binary_to_decimal(calculations2[c+1]))), binary_to_decimal(int(calculations2[a+1])), binary_to_decimal(int(calculations2[b+1]))))

outfile = open(outfile, "w")
outfile.write(out2.format(ly_to_km(int(binary_to_decimal(calculations2[c+1]))), binary_to_decimal(int(calculations2[a+1])), binary_to_decimal(int(calculations2[b+1]))))

english_to_binarian(infile3)

outfile.close()

# A couple of suggestions for starting:

#   1. Do not panic! This assignment is much easier than it seems. Trust me!
#   2. Take a deep breath and start with the simplest tasks first:
#       - read the input files and print them out to see if you are reading them correctly.
#   3. Store the contents of dictionary.txt in a dictionary data structure and try
#      accessing some of its elements.
#   4. Think about how you can use your dictionary to translate the message once you extract it.
#   5. Think about what you need to consider when extracting the message from the jumbled transmission:
#       - How will you check if a line starts with a special character or not?
#       - Try extraxcting relevant lines and printing them to check if you are doing it correctly.
#       - Once you have the relevant lines, think about how you will translate them word-by-word
#         using your dictionary.
#   6. Once you get started, it will get easier. Do one step at a time and check your results at each step.
#   7. Do not try to code everything at once hoping it will work in the end. In most cases, it will not. 
#	   Instead, divide your work into smaller independent parts which you will test separately.

#   I want everyone to try and complete this assignment. Even if it seems too hard for you at first,
#   I want you to get started and do as much as you can. When you get stuck, ask for advice on how to proceed.
#   The most important thing is that you believe that you can do this. If you work on the assignment
#   every day for at least 30 minutes, you will make progress fast. So don't wait until the last week to start.
#   Start now! Try to enjoy solving this to keep yourself motivated. And trust me when I tell you that:
#   YOU CAN DO THIS!
#   You just need to work on it.
#   Good luck! :)
