def to_rna(dna_strand):
    alpha = "AGCT"
    for nuc in dna_strand :
        if nuc in alpha :
            continue
        else : raise ValueError("Invalid Letter")
    dna_strand = dna_strand.replace("A","U")
    dna_strand = dna_strand.replace("T","A")
    dna_strand = dna_strand.replace("C","K")
    dna_strand = dna_strand.replace("G","C")
    dna_strand = dna_strand.replace("K","G")
    return(dna_strand)

print(to_rna("CAGTCAGT"))