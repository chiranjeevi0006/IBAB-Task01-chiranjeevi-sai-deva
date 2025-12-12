from .utils import _upper, _safe_index
from .transform import reverse_complement

def gc_content(seq):

    s = _upper(seq)
    length = len(s)

    if length == 0:
        return 0

    gc = 0
    for ch in s:
        if ch == "G" or ch == "C":
            gc += 1

    percent = (gc / length) * 100
    return percent


def at_content(seq):

    s = _upper(seq)
    length = len(s)

    if length == 0:
        return 0

    at = 0
    for ch in s:
        if ch == "A" or ch == "T":
            at += 1

    percent = (at / length) * 100
    return percent


def gc_content_region(seq, start, end):

    s = _upper(seq)
    length = len(s)

    start0, end1 = _safe_index(start, end, length)
    region = s[start0:end1]

    return gc_content(region)


def is_palindrome(seq):

    s = _upper(seq)
    revcomp = reverse_complement(s)

    if s == revcomp:
        return True
    else:
        return False


def find_first_motif(seq, motif):

    s = _upper(seq)
    m = _upper(motif)


    index = s.find(m)

    if index == -1:
        return -1
    else:
        return index + 1   # convert to 1-based


def find_all_motifs(seq, motif):

    s = _upper(seq)
    m = _upper(motif)

    positions = []
    start = 0

    while True:
        index = s.find(m, start)

        if index == -1:
            break

        positions.append(index + 1)  # convert to 1-based
        start = index + 1  # allow overlapping matches

    return positions


def kmer_breakdown(seq, k):

    s = _upper(seq)
    n = len(s)

    if k <= 0 or k > n:
        return {}

    kmers = {}

    i = 0
    while i <= n - k:
        kmer = s[i:i+k]

        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1

        i += 1

    return kmers


def has_simple_repeats(seq, min_repeat_len=2, threshold=3):

    s = _upper(seq)
    n = len(s)

    # not enough length to have repeats
    if n < min_repeat_len * threshold:
        return False

    unit_len = min_repeat_len
    while unit_len <= 5:  # limit unit length for speed
        i = 0
        while i <= n - unit_len * threshold:
            unit = s[i:i+unit_len]

            repeated = True
            j = 1
            while j < threshold:
                start = i + j * unit_len
                end = start + unit_len
                if s[start:end] != unit:
                    repeated = False
                    break
                j += 1

            if repeated:
                return True

            i += 1

        unit_len += 1

    return False


def longest_run(seq):

    s = _upper(seq)

    if len(s) == 0:
        return {"A":0, "T":0, "G":0, "C":0, "N":0,
                "longest_base": None, "length": 0}

    runs = {"A":0, "T":0, "G":0, "C":0, "N":0}

    current_char = s[0]
    current_len = 1

    i = 1
    while i < len(s):
        if s[i] == current_char:
            current_len += 1
        else:
            if current_char in runs:
                if current_len > runs[current_char]:
                    runs[current_char] = current_len

            current_char = s[i]
            current_len = 1

        i += 1

    # finalize last run
    if current_char in runs:
        if current_len > runs[current_char]:
            runs[current_char] = current_len

    # find overall longest
    longest_base = None
    longest_length = 0

    for base in runs:
        if runs[base] > longest_length:
            longest_length = runs[base]
            longest_base = base

    runs["longest_base"] = longest_base
    runs["length"] = longest_length

    return runs

