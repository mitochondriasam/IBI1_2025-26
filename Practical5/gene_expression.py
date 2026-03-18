import matplotlib.pyplot as plt

genes = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}
print(f"Gene Expression Levels: {genes}")
genes["MYC"] = 11.6
print(f"Updated Gene Expression Levels: {genes}")

plt.bar(genes.keys(), genes.values())
plt.xlabel("Genes")
plt.ylabel("Expression Level")
plt.title("Gene Expression Analysis")
plt.show()

gene_of_interest = input("Enter a gene to check its expression level: ")
while not gene_of_interest in genes:
    print("Gene not found.")
    gene_of_interest = input("Enter a gene to check its expression level: ")
print(f"{gene_of_interest} expression level: {genes[gene_of_interest]}")
    
avg = round(sum(genes.values()) / len(genes), 2)
print(f"Average gene expression level: {avg}")