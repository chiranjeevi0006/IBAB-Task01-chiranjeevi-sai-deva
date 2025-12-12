from .utils import _upper


_COMPLEMENT_TABLE = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
    "N": "N"
}

def complement(seq):

    s = _upper(seq)
    result = ""

    for ch in s:
        if ch in _COMPLEMENT_TABLE:
            result += _COMPLEMENT_TABLE[ch]
        else:

            result += "N"

    return result


def reverse_seq(seq):

    return seq[::-1]


def reverse_complement(seq):

    comp = complement(seq)
    rev = reverse_seq(comp)
    return rev


def standardize_seq(seq):

    s = _upper(seq)
    result = ""

    for ch in s:
        if ch in "ATGCN":
            result += ch
        else:
            result += "N"

    return result


def replace_with_map(seq, mapping):

    s = _upper(seq)
    result = ""


    new_map = {}
    for k in mapping:
        new_map[k.upper()] = mapping[k].upper()


    for ch in s:
        if ch in new_map:
            result += new_map[ch]
        else:
            result += ch
