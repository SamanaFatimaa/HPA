import csv
from typing import List, Dict

class Analyzer:
    """
    A class to analyze gene expression data from a TSV file.

    Attributes:
    -----------
    path : str
        The file path to the TSV file containing gene expression data.
    data : List[Dict[str, str]]
        The data loaded from the TSV file, where each row is represented
        as a dictionary with keys corresponding to the column names.
    """
     
    def __init__(self, path: str):
        """
        Initialize the Analyzer with the given file path and load the data.

        Parameters:
        -----------
        path : str
            The path to the TSV file containing gene expression data.
        """
        
        self.path = path
        self.data = self.load_data()

    def load_data(self) -> List[Dict[str, str]]:
        """
        Load the gene expression data from the specified TSV file.

        Returns:
        --------
        List[Dict[str, str]]:
            A list of dictionaries where each dictionary corresponds to a row in the
            TSV file, with column names as keys and the respective values.
        """
        with open(self.path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='\t') 
            return list(reader)

    def get_number_of_genes(self) -> int:
        """Return the number of distinct genes."""
        return len(self.get_distinct_genes())

    def get_distinct_genes(self) -> List[str]:
        """Return a list of distinct genes."""
        return sorted(list({row['Gene'] for row in self.data}))

    def get_tissues_by_gene_name(self, gene_name: str) -> List[str]:
        """Return distinct tissues for the given gene name as a list of strings."""
        tissues = set()
        for row in self.data:
            if row['Gene name'] == gene_name:  # Compare with 'Gene name' column
                tissues.add(row['Tissue'])
        return sorted(list(tissues))

    