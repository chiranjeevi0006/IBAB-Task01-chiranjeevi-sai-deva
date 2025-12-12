from .utils import _upper, VALID_BASES, _is_base_valid

def seq_length(seq):

    return len(seq)


def count_bases(seq):

    s = _upper(seq)

    counts = {"A": 0, "T": 0, "G": 0, "C": 0}

    for ch in s:
        if ch == "A":
            counts["A"] += 1
        elif ch == "T":
            counts["T"] += 1
        elif ch == "G":
            counts["G"] += 1
        elif ch == "C":
            counts["C"] += 1

    return counts


def count_ambiguous(seq):

    s = _upper(seq)
    count = 0

    for ch in s:
        if ch not in VALID_BASES:
            count += 1

    return count


def is_valid_dna(seq):

    s = _upper(seq)

    for ch in s:
        if not _is_base_valid(ch):
            return False

    return True


def replace_invalid_with_N(seq):
    s = _upper(seq)
    result = ""

    for ch in s:
        if _is_base_valid(ch):
            result += ch
        else:
            result += "N"

    return result


def count_purines(seq):
    s = _upper(seq)
    count = 0

    for ch in s:
        if ch == "A" or ch == "G":
            count += 1

    return count


def count_pyrimidines(seq):
    s = _upper(seq)
    count = 0

    for ch in s:
        if ch == "T" or ch == "C":
            count += 1

    return count


def nucleotide_frequency(seq):
    s = _upper(seq)
    freq = {"A":0, "T":0, "G":0, "C":0, "N":0, "other":0}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq["other"] += 1

    return freq


def percentage_report(seq):

    total = len(seq)
    if total == 0:
        total = 1

    freq = nucleotide_frequency(seq)
    percent = {}

    for base in freq:
        percent[base] = (freq[base] / total) * 100

    return percent
