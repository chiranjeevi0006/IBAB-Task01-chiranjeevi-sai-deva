def split_into_codons():
    rna = input("Enter RNA sequence: ").upper()

    codons = []

    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) == 3:
            codons.append(codon)

    print("Codons:", " ".join(codons))
    return codons


# split_into_codons()
def translate_rna():
    rna = input("Enter RNA sequence or codons: ").upper()

    codon_table = {
        "AUG": "Met",

        "UUU": "Phe", "UUC": "Phe",
        "UUA": "Leu", "UUG": "Leu",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",

        "GGC": "Gly", "GGU": "Gly", "GGA": "Gly", "GGG": "Gly",

        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",

        "AAA": "Lys", "AAG": "Lys",

        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }


    if " " in rna:
        codons = rna.split()
    else:
        codons = [rna[i:i+3] for i in range(0, len(rna), 3)]

    protein = []
    started = False

    for codon in codons:
        if codon == "AUG" and not started:
            started = True
            protein.append("Met")
            continue

        if started:
            if codon in codon_table:
                if codon_table[codon] == "STOP":
                    break
                protein.append(codon_table[codon])
            else:
                protein.append("X")

    if protein:
        print("Protein sequence:", " ".join(protein))
    else:
        print("No valid protein found")
# translate_rna()
def detect_mutations():
    ref = input("Enter reference DNA sequence: ").upper()
    sample = input("Enter sample DNA sequence: ").upper()

    mutations = []

    for i in range(min(len(ref), len(sample))):
        if ref[i] != sample[i]:
            mutations.append((i+1, ref[i], sample[i]))

    if mutations:
        print("Mutations found:")
        for pos, r, s in mutations:
            print(f"Position {pos}: {r} → {s}")
    else:
        print("No mutations found")
# detect_mutations()
def find_orfs():
    dna = input("Enter DNA sequence: ").upper()

    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []

    for i in range(0, len(dna)-2):
        if dna[i:i+3] == "ATG":
            for j in range(i, len(dna)-2, 3):
                codon = dna[j:j+3]
                if codon in stop_codons:
                    orfs.append(dna[i:j+3])
                    break

    if orfs:
        print("ORFs found:")
        for orf in orfs:
            print(orf)
    else:
        print("No ORFs found")

def most_frequent_codon():
    rna = input("Enter RNA sequence: ").upper()

    codon_count = {}

    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        if len(codon) == 3:
            if codon in codon_count:
                codon_count[codon] += 1
            else:
                codon_count[codon] = 1

    if not codon_count:
        print("No codons found")
        return

    max_codon = max(codon_count, key=codon_count.get)

    print("Most frequent codon:", max_codon)
    print("Frequency:", codon_count[max_codon])

def conserved_regions():
    seq1 = input("Enter first sequence: ").upper()
    seq2 = input("Enter second sequence: ").upper()

    conserved = []
    current = ""

    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] == seq2[i]:
            current += seq1[i]
        else:
            if current:
                conserved.append(current)
                current = ""

    if current:
        conserved.append(current)

    if conserved:
        print("Conserved regions:")
        for region in conserved:
            print(region)
    else:
        print("No conserved regions found")


