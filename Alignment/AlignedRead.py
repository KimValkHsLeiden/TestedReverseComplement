import AlignmentInfo


class AlignedRead:
    def __init__(self, fwd_read_sequence, rev_read_sequence, reference_sequence, alignment_info):
        self.fwdReadSequence: int
        self.alignmentInfo: AlignmentInfo
        self.fwdReadSequence = fwd_read_sequence
        self.revReadSequence = rev_read_sequence
        self.referenceSequence = reference_sequence
        if type(alignment_info) != AlignmentInfo:
            print("Complain loudly")
        self.alignmentInfo = alignment_info

    def calculate_dna_insert_length(self):
        start_reference_index = self.alignmentInfo.start_fwd
        stop_reference_index = self.alignmentInfo.start_rev
        dna_insert_length = stop_reference_index - start_reference_index
        return dna_insert_length

    def calculate_dna_insert_v2(self, allele):
        allele_indexes = self.alignmentInfo.get_allele_indexes(allele)
        dna_insert_length = allele_indexes[0] - allele_indexes[1]
        return dna_insert_length
