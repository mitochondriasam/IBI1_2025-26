def calculate_mass(sequence):
    """Calculate the mass of a protein sequence.

    Args:
        sequence (str): A string representing the amino acid sequence of the protein.

    Returns:
        float: The calculated mass of the protein.
    """
    # Define the mass of each amino acid
    aa_mass = {
        'G': 57.02,
        'A': 71.04,
        'S': 87.03,
        'P': 97.05,
        'V': 99.07,
        'T': 101.05,
        'C': 103.01,
        'I': 113.08,
        'L': 113.08,
        'N': 114.04,
        'D': 115.03,
        'Q': 128.06,
        'K': 128.09,
        'E': 129.04,
        'M': 131.04,
        'H': 137.06,
        'F': 147.07,
        'R': 156.10,
        'Y': 163.06,
        'W': 186.08
    }

    total_mass = 0.0

    for aa in sequence:
        if aa in aa_mass:
            total_mass += aa_mass[aa]
        else:
            raise ValueError(f"Invalid amino acid '{aa}' in sequence.")

    return total_mass

if __name__ == "__main__":
    # Example usage
    protein_sequence = input("Enter the amino acid sequence of the protein: ").upper()
    mass = calculate_mass(protein_sequence)
    print(f"The mass of the protein is: {mass:.2f} amu")