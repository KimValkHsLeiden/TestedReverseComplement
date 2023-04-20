def reverse_complement_v1(dna_sequence):
    reverse_complement_sequence = []  # Initiate result variable

    # loop over reverse range (to start at end of dna sequence
    for nuc_index in reversed(range(len(dna_sequence))):
        current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
        match current_nuc:
            case 'T':
                complement_nuc = 'A'
            case 'A':
                complement_nuc = 'T'
            case 'G':
                complement_nuc = 'C'
            case 'C':
                complement_nuc = 'G'
            case _:
                complement_nuc = ' '
        reverse_complement_sequence.append(complement_nuc)
    return reverse_complement_sequence


def reverse_complement_v2(dna_sequence):
    reverse_complement_sequence = []  # Initiate result variable

    # loop over reverse range (to start at end of dna sequence
    for nuc_index in reversed(range(len(dna_sequence))):
        current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
        match current_nuc:
            case 'T':
                complement_nuc = 'A'
            case 'A':
                complement_nuc = 'T'
            case 'G':
                complement_nuc = 'C'
            case 'C':
                complement_nuc = 'G'
            case _:
                complement_nuc = ' '
        reverse_complement_sequence.append(complement_nuc)
    reverse_complement_as_string = ''.join(reverse_complement_sequence)
    return reverse_complement_as_string
#
#
def reverse_complement_v3(dna_sequence):
    reverse_complement_sequence = []  # Initiate result variable

    # loop over reverse range (to start at end of dna sequence
    for nuc_index in reversed(range(len(dna_sequence))):
        current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
        match current_nuc:
            case 'T':
                complement_nuc = 'A'
            case 'A':
                complement_nuc = 'T'
            case 'G':
                complement_nuc = 'C'
            case 'C':
                complement_nuc = 'G'
            case 'N':
                complement_nuc = 'N'
            case 'W':
                complement_nuc = 'W'
            case 'S':
                complement_nuc = 'S'
            case 'M':
                complement_nuc = 'K'
            case 'K':
                complement_nuc = 'M'
            case 'R':
                complement_nuc = 'Y'
            case 'Y':
                complement_nuc = 'R'
            case 'B':
                complement_nuc = 'V'
            case 'D':
                complement_nuc = 'H'
            case 'H':
                complement_nuc = 'D'
            case 'V':
                complement_nuc = 'B'
            case '-':
                complement_nuc = '-'
            case _:
                complement_nuc = ' '
        reverse_complement_sequence.append(complement_nuc)
    reverse_complement_as_string = ''.join(reverse_complement_sequence)
    return reverse_complement_as_string
#
#
def reverse_complement_v4(dna_sequence):
    reverse_complement_sequence = []  # Initiate result variable

    # loop over reverse range (to start at end of dna sequence
    for nuc_index in reversed(range(len(dna_sequence))):
        current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
        match current_nuc:
            case 'T':
                complement_nuc = 'A'
            case 'A':
                complement_nuc = 'T'
            case 'G':
                complement_nuc = 'C'
            case 'C':
                complement_nuc = 'G'
            case 'N':
                complement_nuc = 'N'
            case 'W':
                complement_nuc = 'W'
            case 'S':
                complement_nuc = 'S'
            case 'M':
                complement_nuc = 'K'
            case 'K':
                complement_nuc = 'M'
            case 'R':
                complement_nuc = 'Y'
            case 'Y':
                complement_nuc = 'R'
            case 'B':
                complement_nuc = 'V'
            case 'D':
                complement_nuc = 'H'
            case 'H':
                complement_nuc = 'D'
            case 'V':
                complement_nuc = 'B'
            case '-':
                complement_nuc = '-'
            case _:
                error_msg = "Character: '" + current_nuc + "' was found, this does not represent a nucleotide!"
                raise ValueError(error_msg)
        reverse_complement_sequence.append(complement_nuc)
    reverse_complement_as_string = ''.join(reverse_complement_sequence)
    return reverse_complement_as_string
#
#
def reverse_complement_v5(dna_sequence):
    reverse_complement_sequence = []  # Initiate result variable

    # loop over reverse range (to start at end of dna sequence
    for nuc_index in reversed(range(len(dna_sequence))):
        current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
        complement_nuc = complement_nucleotide(current_nuc)
        reverse_complement_sequence.append(complement_nuc)
    reverse_complement_as_string = ''.join(reverse_complement_sequence)
    return reverse_complement_as_string
#
#
def reverse_complement_v5(dna_sequence):
    reverse_complement_sequence = []  # Initiate result variable
    # Raise error if type is wrong
    if type(dna_sequence) != str:
        raise TypeError("reverse_complement only accepts string types")

    # loop over reverse range (to start at end of dna sequence
    for nuc_index in reversed(range(len(dna_sequence))):
        current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
        complement_nuc = complement_nucleotide(current_nuc)
        reverse_complement_sequence.append(complement_nuc)
    reverse_complement_as_string = ''.join(reverse_complement_sequence)
    return reverse_complement_as_string

#
def reverse_complement_v7(dna_sequence):
    reverse_complement_sequence = []  # Initiate result variable
    # Raise error if type is wrong
    if type(dna_sequence) != str:
        raise TypeError("reverse_complement only accepts string types")

    # Raise error if string is length 1
    if len(dna_sequence) == 1:
        raise TypeError("This function was not built for single nucleotides. Reverse complement does not make sense. " +
                        "Use function 'complement' from same namespace.")

    # loop over reverse range (to start at end of dna sequence
    for nuc_index in reversed(range(len(dna_sequence))):
        current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
        complement_nuc = complement_nucleotide(current_nuc)
        reverse_complement_sequence.append(complement_nuc)
    reverse_complement_as_string = ''.join(reverse_complement_sequence)
    return reverse_complement_as_string


def reverse_complement(dna_sequence):
    reverse_complement_sequence = []  # Initiate result variable
    # Raise error if type is wrong
    if type(dna_sequence) != str:
        raise TypeError("reverse_complement only accepts string types")

    # Raise error if string is length 1
    if len(dna_sequence) == 1:
        raise TypeError("This function was not built for single nucleotides. Reverse complement does not make sense. " +
                        "Use function 'complement' from same namespace.")

    # loop over reverse range (to start at end of dna sequence
    for nuc_index in reversed(range(len(dna_sequence))):
        current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
        if current_nuc == 'U':
            raise ValueError("reverse_complement on a RNA-sequence does not make sense. Create reverse_transcribe "
                             "function")
        complement_nuc = complement_nucleotide(current_nuc)
        reverse_complement_sequence.append(complement_nuc)
    reverse_complement_as_string = ''.join(reverse_complement_sequence)
    return reverse_complement_as_string

#
def complement_nucleotide_v1(nucleotide):
    match nucleotide:
        case 'T':
            complement_nuc = 'A'
        case 'A':
            complement_nuc = 'T'
        case 'G':
            complement_nuc = 'C'
        case 'C':
            complement_nuc = 'G'
        case 'N':
            complement_nuc = 'N'
        case 'W':
            complement_nuc = 'W'
        case 'S':
            complement_nuc = 'S'
        case 'M':
            complement_nuc = 'K'
        case 'K':
            complement_nuc = 'M'
        case 'R':
            complement_nuc = 'Y'
        case 'Y':
            complement_nuc = 'R'
        case 'B':
            complement_nuc = 'V'
        case 'D':
            complement_nuc = 'H'
        case 'H':
            complement_nuc = 'D'
        case 'V':
            complement_nuc = 'B'
        case '-':
            complement_nuc = '-'
        case _:
            error_msg = "Character: '" + nucleotide + "' was found, this does not represent a nucleotide!"
            raise ValueError(error_msg)
    return complement_nuc

#
def complement_nucleotide(nucleotide):
    complement_dict = {'T': 'A',
                       'A': 'T',
                       'G': 'C',
                       'C': 'G',
                       'U': 'A',
                       'N': 'N',
                       'W': 'W',
                       'S': 'S',
                       'M': 'K',
                       'K': 'M',
                       'R': 'Y',
                       'Y': 'R',
                       'B': 'V',
                       'D': 'H',
                       'H': 'D',
                       'V': 'B',
                       '-': '-'}
    if nucleotide not in complement_dict:
        error_msg = "Character: '" + nucleotide + "' was found, this does not represent a nucleotide!"
        raise ValueError(error_msg)
    complement_nuc = complement_dict.get(nucleotide)

    return complement_nuc
#
#
def complement_sequence(dna_sequence):
    complement_string = ''
    for nucleotide in dna_sequence:
        complement_nuc = complement_nucleotide(nucleotide)
        complement_string += complement_nuc

    return complement_string


# Extra comment