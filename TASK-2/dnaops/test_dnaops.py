from dnaops import (
    seq_length, count_bases, count_ambiguous, is_valid_dna, replace_invalid_with_N,
    complement, reverse_complement, gc_content, gc_content_region,
    find_all_motifs, kmer_breakdown, has_simple_repeats, longest_run
)

def test_basic_functions():
    seq = "ATGCatgcnnxyz"
    assert seq_length(seq) == 13

    counts = count_bases(seq)
    assert counts["A"] == 2
    assert counts["T"] == 2
    assert counts["G"] == 2
    assert counts["C"] == 2

    assert count_ambiguous(seq) == 3
    assert is_valid_dna("ATGCN") == True
    assert is_valid_dna(seq) == False
    assert replace_invalid_with_N(seq).endswith("NNN")

def test_complement_and_reverse_complement():
    seq = "ATGC"
    assert complement(seq) == "TACG"
    assert reverse_complement(seq) == "GCAT"

def test_gc_and_region():
    seq = "GGCCAAAT"
    assert round(gc_content(seq), 2) == 50.00
    assert round(gc_content_region(seq, 3, 6), 2) == 50.00

def test_motifs_and_kmers():
    seq = "ATATAT"
    assert find_all_motifs(seq, "AT") == [1, 3, 5]

    kmers = kmer_breakdown("ATGCATGC", 4)
    assert kmers["ATGC"] == 2

def test_repeats_and_runs():
    seq = "AAATTTGGGCCCAAAAA"
    runs = longest_run(seq)
    assert runs["longest_base"] == "A"
    assert runs["length"] == 5

def test_simple_repeats():
    # AT repeated 3 times -> simple repeat
    seq = "ATATATGG"
    assert has_simple_repeats(seq, min_repeat_len=2, threshold=3) == True
