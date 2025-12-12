VALID_BASES = set(["A", "T", "G", "C", "N"])

def _upper(seq):

    return seq.upper()

def _is_base_valid(ch):

    if ch in VALID_BASES:
        return True
    else:
        return False

def _safe_index(start, end, length):


    # handle None values
    if start is None:
        start = 1
    if end is None:
        end = length

    # prevent going out of range
    if start < 1:
        start = 1
    if end > length:
        end = length

    # convert 1-based to 0-based for Python slicing
    start0 = start - 1
    end1 = end

    return start0, end1
