# dnaops

This is a small Python package that contains different functions for working with DNA sequences.
This was done as part of Hackathon Task-2.

The package has functions for:
- checking and counting bases
- validating DNA
- replacing wrong characters
- complement, reverse, reverse-complement
- GC and AT percentage
- GC percentage of a region
- finding motifs
- k-mer breakdown
- checking simple repeats
- longest run of a nucleotide

# How to install (local)
Go to the main folder of the project and run:

pip install -e .


# Example

from dnaops import gc_content, reverse_complement

print(gc_content("ATGC"))
print(reverse_complement("ATGC"))


### Files
- seq.py - base counts, validation
- transform.py - complement, reverse
- analysis.py - GC%, motifs, repeats
- utils.py - helper functions
- __init__.py - connects all functions

