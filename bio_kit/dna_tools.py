def dna_to_rna(dna_sequence):
	return dna_sequence.replace("T", "U")
	
def gc_content(dna_sequence):
	g_count = dna_sequence.count("G")
	c_count = dna_sequence.count("C")
	total_count = len(dna_sequence)
	return (g_count + c_count) / total_count
	
def reverse_compliment(dna_sequence):
	new_sequence = ""
	for base in input:
		if base == 'A':
			new_sequence = new_sequence + 'G'
		if base == 'T':
			new_sequence = new_sequence + 'C'
		if base == 'G':
			new_sequence = new_sequence + 'A'
		if base == 'C':
			new_sequence = new_sequence + 'T'
	return(new_sequence)
	
