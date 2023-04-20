class AlignmentInfo:
    def __init__(self, start_fwd, start_rev, read_length):
        self.start_fwd = start_fwd  # The start index on the reference sequence
        self.start_rev = start_rev  # The start index on the reference sequence
        self.stop_fwd = start_fwd + read_length
        self.stop_rev = start_rev - read_length

        # return is list of 4 integers (start_fwd, start_rev, stop_fwd, stop_rev)

    def get_allele_indexes(self, allele):
        allele_indexes = []
        start_fwd = "think of beautiful code"
        start_rev = "something similar here"
        stop_fwd = "42"
        stop_rev = "6.9"
        allele_indexes.append(start_fwd)
        allele_indexes.append(start_rev)
        allele_indexes.append(stop_fwd)
        allele_indexes.append(stop_rev)
        return allele_indexes
