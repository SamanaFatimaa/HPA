from hpa.tools import Analyzer

analyzer = Analyzer(url_or_path="./data/normal_tissue_test.tsv")

with open("results.txt", "w") as f:
    num_genes = analyzer.get_number_of_genes()
    f.write(f"Number of distinct genes: {num_genes}\n")

    distinct_genes = analyzer.get_distinct_genes()
    f.write(f"Distinct genes: {distinct_genes}\n")

    tissues = analyzer.get_tissues_by_gene_name("TSPAN6")
    f.write(f"Tissues for TSPAN6: {tissues}\n")

# Confirmation message
print("Results have been written to results.txt")