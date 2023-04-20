from Biology_statics import reverse_complement
import pytest


def test_reverse_complement_correct_dna_seq_returns_reverse_complement():
    starting_sequence = "ATCGGGCCTTAT"
    expected_result = "ATAAGGCCCGAT"
    actual_result = reverse_complement(starting_sequence)
    assert actual_result == expected_result


def test_reverse_complement_dna_seq_with_uncommon_nucleotide_returns_reverse_complement():
    uncommon_nucleotides = ['W', 'S', 'M', 'K', 'R', 'Y', 'B', 'D', 'H', 'V']
    complementary_bases = ['W', 'S', 'K', 'M', 'Y', 'R', 'V', 'H', 'D', 'B']
    for i in range(len(uncommon_nucleotides)):
        starting_sequence = "AT" + uncommon_nucleotides[i] + "CGGGCCTTAT"
        expected_result = "ATAAGGCCCG" + complementary_bases[i] + "AT"
        actual_result = reverse_complement(starting_sequence)
        assert actual_result == expected_result
#
#
# def test_reverse_complement_dna_seq_with_unexpected_character_raises_specific_value_error():
#     unexpected_characters = ['Q', 'E', 'U', 'I', 'O', 'P', 'F', 'J', 'L', 'Z', 'X']
#     for unexp_char in unexpected_characters:
#         input_to_test = "ATC" + unexp_char + "CCAAAGGGT"
#         expected_error_msg = "Character: '" + unexp_char + "' was found, this does not represent a nucleotide!"
#         with pytest.raises(ValueError, match=expected_error_msg):
#             reverse_complement(input_to_test)

#
def test_reverse_complement_dna_seq_with_unexpected_character_raises_value_error_v2():
    unexpected_characters = ['Q', 'E', 'I', 'O', 'P', 'F', 'J', 'L', 'Z', 'X']
    for unexp_char in unexpected_characters:
        input_to_test = "ATC" + unexp_char + "CCAAAGGGT"
        expected_error_msg = "Character: '" + unexp_char + "' was found, this does not represent a nucleotide!"
        with pytest.raises(ValueError, match=expected_error_msg):
            reverse_complement(input_to_test)

#
def test_reverse_complement_wrong_type_raises_type_error():
    wrong_type_input = 1
    with pytest.raises(TypeError, match="reverse_complement only accepts string types"):
        reverse_complement(wrong_type_input)


def test_reverse_complement_single_nucleotide_raises_custom_type_error():
    single_nucleotide = 'C'
    error_msg = "This function was not built for single nucleotides. Reverse complement does not make sense. " \
                "Use function 'complement' from same namespace."
    with pytest.raises(TypeError, match=error_msg):
        reverse_complement(single_nucleotide)


def test_reverse_complement_rna_sequence_raises_specific_value_error():
    rna_sequence = "AUCGGGCCUUAU"
    error_msg = "reverse_complement on a RNA-sequence does not make sense. Create reverse_transcribe function"
    with pytest.raises(ValueError, match=error_msg):
        reverse_complement(rna_sequence)
