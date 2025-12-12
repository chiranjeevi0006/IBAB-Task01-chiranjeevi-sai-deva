# Design Notes

I created the dnaops package using multiple Python files.
Each file has related functions so the code is easier to understand and update.

- seq.py - functions for length, counting bases, validation, ambiguous bases
- transform.py - complement, reverse, reverse-complement, replace using map
- analysis.py - GC%, AT%, GC of a region, motifs, k-mers, repeats, longest run
- utils.py - helper functions like uppercase and safe indexing

I used 1-based indexing for motif positions because it is common in biology and easier to understand.

A simple pytest file is added in the tests/ folder to check if important functions work correctly.

Future improvements:
- FASTA file reading
- IUPAC support for ambiguous bases
- Better repeat detection system

