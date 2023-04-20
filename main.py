# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Biology_statics import reverse_complement, complement_sequence
from DnaComplementer import DnaComplementer
import random
import time


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Define settings for creating random sequences
    amount_of_sequences = 20000
    length_of_sequences = 150

    # Initialize list of random sequences
    random_sequences = []
    # Loop over amount of sequences
    for _ in range(amount_of_sequences):
        # Create random sequence
        random_sequence = ''.join(random.choice('CGTA') for _ in range(length_of_sequences))
        # Add to list
        random_sequences.append(random_sequence)

    print(random_sequences[0])
    # ====================function based======================
    start_time_fun = time.time()

    # Create complement sequences
    complement_sequences = []
    for sequence in random_sequences:
        complement_seq = complement_sequence(sequence)

    # Initialize reverse_complemented_sequences
    reverse_complemented_sequences = []
    for sequence in random_sequences:
        reverse_complemented_sequences.append(reverse_complement(sequence))

    stop_time_fun = time.time()

    # ====================class based 1======================
    start_time_class1 = time.time()

    # Create complement sequences
    complement_sequences = []
    for sequence in random_sequences:
        dna_complementer = DnaComplementer()
        complement_sequences.append(dna_complementer.complement_sequence(sequence))

    # Initialize reverse_complemented_sequences
    reverse_complemented_sequences = []
    for sequence in random_sequences:
        dna_complementer = DnaComplementer()
        reverse_complemented_sequences.append(dna_complementer.reverse_complement(sequence))

    stop_time_class1 = time.time()

    # ====================class based 2======================
    start_time_class2 = time.time()
    # Initialize DNA complementer
    dna_complementer = DnaComplementer()

    # Initialize lists
    complement_sequences = []
    reverse_complemented_sequences = []
    for sequence in random_sequences:
        complement_sequences.append(dna_complementer.complement_sequence(sequence))
        reverse_complemented_sequences.append(dna_complementer.reverse_complement(sequence))

    stop_time_class2 = time.time()

    print("function based")
    print(start_time_fun)
    print(stop_time_fun)
    print(stop_time_fun-start_time_fun)
    print("dumb class based")
    print(start_time_class1)
    print(stop_time_class1)
    print(stop_time_class1 - start_time_class1)
    print("smart class based")
    print(start_time_class2)
    print(stop_time_class2)
    print(stop_time_class2 - start_time_class2)
