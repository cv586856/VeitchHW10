#Corbin Veitch HW 10 recostructSentence.py
# Description: Reads two text files with twist word order and reconstructs the complete output.
# Command Line Arguments: input1.txt input2.txt
# Example Invocation: python3 reconstructSentence.py input1.txt input2.txt

import sys

def main():
 # Checking if correct number of command-line arguments
    if len(sys.argv) != 3:

        print("Usage: python3 reconstructSentence.py <input_file1> <input_file2>")
        sys.exit(1)


# Extract input file names from command line arguments
    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
    

# basic list declareations
    f1 = open(input_file1)
    f2 = open(input_file2)
    f3 = open("output.txt","w")
    out = []


# Steps through and Len each list
    for line1 in f1.readlines():
        list1 = line1.split()
        list1_length = len(list1)

    for line2 in f2.readlines():
        list2 = line2.split()
        list2_length = len(list2)


# Go through the lists and put together the output list
# strait stepped breaks the problem to make debugging a tad easier
    if (list1_length > list2_length):

        while list1_length >0:

            if(list2_length != 0):

                out.append(list1[list1_length-1])
                out.append(list2[list2_length-1])

            else:

                out.append(list1[list1_length-1])

                break

            list1_length = list1_length - 1
            list2_length = list2_length - 1
    else:

        while list2_length > 0:

            if (list1_length != 0):

                out.append(list1[list1_length-1])
                out.append(list2[list2_length-1])
            else:

                break

            list1_length = list1_length - 1
            list2_length = list2_length - 1

    print(f"List1: {list1}")
    print(f"List2: {list2}")
    print(f"The list out: {out}")


    f3.writelines([str(i)+' ' for i in out])
    f3.close()

main()
