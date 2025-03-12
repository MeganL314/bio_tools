aa_weights = {
    'A': 71.08, 'C': 103.14, 'D': 115.09, 'E': 129.11, 'F': 147.18,
    'G': 57.05, 'H': 137.14, 'I': 113.16, 'K': 128.17, 'L': 113.16,
    'M': 131.19, 'N': 114.11, 'P': 97.12, 'Q': 128.13, 'R': 156.19,
    'S': 87.08, 'T': 101.11, 'V': 99.14, 'W': 186.21, 'Y': 163.18
}

essential_aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

def find_molecular_weight(aa_sequence):
	weight = 0
	for aa in aa_sequence:
		weight = weight + aa_weights[aa]
	return weight
	
def find_essential_aa(aa_sequence):
    return [aa for aa in aa_sequence if aa in essential_aa]