class DnaComplementer:
    def __init__(self):
        self.complement_dict = {'T': 'A',
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

    def complement_nucleotide(self, nucleotide):

        if nucleotide not in self.complement_dict:
            error_msg = "Character: '" + nucleotide + "' was found, this does not represent a nucleotide!"
            raise ValueError(error_msg)
        complement_nuc = self.complement_dict.get(nucleotide)

        return complement_nuc

    def reverse_complement(self, dna_sequence):
        reverse_complement_sequence = []  # Initiate result variable
        # Raise error if type is wrong
        if type(dna_sequence) != str:
            raise TypeError("reverse_complement only accepts string types")

        # Raise error if string is length 1
        if len(dna_sequence) == 1:
            raise TypeError(
                "This function was not built for single nucleotides. Reverse complement does not make sense. " +
                "Use function 'complement' from same namespace.")

        # loop over reverse range (to start at end of dna sequence
        for nuc_index in reversed(range(len(dna_sequence))):
            current_nuc = dna_sequence[nuc_index]  # define nucleotide to match/case
            if current_nuc == 'U':
                raise ValueError("reverse_complement on a RNA-sequence does not make sense. Create reverse_transcribe "
                                 "function")
            complement_nuc = self.complement_nucleotide(current_nuc)
            reverse_complement_sequence.append(complement_nuc)
        reverse_complement_as_string = ''.join(reverse_complement_sequence)
        return reverse_complement_as_string

    def complement_sequence(self, dna_sequence):
        complement_string = ''
        for nucleotide in dna_sequence:
            complement_nuc = self.complement_nucleotide(nucleotide)
            complement_string += complement_nuc

        return complement_string
