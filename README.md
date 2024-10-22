# hpa

## Name
HPA-1: Human Protein Atlas 

## Description
HPA-1 is a tool designed for analyzing gene expression data from the Human Protein Atlas. It enables users to extract and analyze data related to tissue-specific gene expression, including the number of distinct genes, tissues associated with specific genes, and more. The project leverages the data from the Human Protein Atlas to provide insights into gene expression levels across various tissues.

The project uses a `.tsv` file containing data about genes, tissues, cell types, and their respective expression levels. You can learn more about the Human Protein Atlas and its background [here](https://www.proteinatlas.org/about/history). It also contains a test_software.py file which contains unit tests for the Analyzer class in the tools.py file.

## Features
- **Distinct Gene Count**: Calculate the number of distinct genes in the dataset.
- **Gene Search**: Retrieve all tissues associated with a specific gene.
- **Data Loading**: Efficiently loads and parses the Human Protein Atlas `.tsv` files.


## Installation
1. Clone the HPA repository in a new window 
2. Navigate to the project directory
3. Set up enivornment 
4. Install packages/dependencies (pytest)

## Usage

1. **Gene Expression Data**
The input data is a TSV file containing columns:

Gene: A unique gene identifier (e.g., ENSG00000000003).
Gene name: The name of the gene (e.g., TSPAN6).
Tissue: The type of tissue where the gene is expressed (e.g., adipose tissue).
Cell type: The type of cells where the gene is expressed (e.g., adipocytes).
Level: The expression level (e.g., High, Medium, Not detected).
Reliability: The reliability of the data (e.g., Approved, Uncertain)

2. **tools.py - Analyzer Class**
The Analyzer class is designed to process and analyze gene expression data from a TSV file. Here's a breakdown of the components:

*Attributes:*
url_or_path: The file path or URL of the TSV file.
data: A list of dictionaries, each dictionary representing a row in the TSV file. The dictionary keys are the column names from the file.

*Methods:*
__init__(self, url_or_path: str): Initializes the class by taking the file path and loads the data.

load_data(self) -> List[Dict[str, str]]: Reads the TSV file using the csv.DictReader and stores each row as a dictionary. This allows easy access to each column by its name.

get_number_of_genes(self) -> int: Returns the number of distinct genes present in the dataset.

get_distinct_genes(self) -> List[str]: Returns a sorted list of distinct gene identifiers from the data.

get_tissues_by_gene_name(self, gene_name: str) -> List[str]: For a given gene name, it returns a sorted list of distinct tissues where the gene is expressed.

3. **test_software.py - Unit Tests**
This file contains unit tests to ensure the Analyzer class methods work as expected.

test_number_of_genes(): Tests if the get_number_of_genes() method returns the correct number of distinct genes. The expected result in the test is 3.

test_distinct_genes(): Tests if the get_distinct_genes() method returns a list of all distinct genes correctly. The expected distinct genes in this case are ["ENSG00000000003", "ENSG00000000005", "ENSG00000000419"].

test_tissues_by_gene_name(): Tests if get_tissues_by_gene_name("TSPAN6") returns the expected list of tissues, which should be ["adipose tissue", "vagina"].

Run the test using pytest tests/test_software.py


4. **Results Code (Script)**
The script processes the data and writes the results to a file results.txt.

num_genes: Stores the number of distinct genes found by calling get_number_of_genes().

distinct_genes: Stores the list of distinct gene identifiers found by calling get_distinct_genes().

tissues: Stores the list of tissues where the gene TSPAN6 is expressed by calling get_tissues_by_gene_name("TSPAN6").

Output: All results are written to a file results.txt for later inspection.

## Support
For help or issues, please open an issue in the repository or reach out via email at s22sfati@uni-bonn.de.

## Roadmap
hpa-1
├── data
│   └── normal_tissue.tsv
├── hpa
│   ├── _init_.py
│   └── tools.py
├── tests
│   ├── _init_.py
│   └── test_software.py
└── venv
    ├── Include
    ├── Lib
    └── Scripts

data: Contains the normal_tissue.tsv file with the Human Protein Atlas data.
hpa: The main Python package for the project, including the Analyzer class in tools.py.
tests: Contains unit tests for the Analyzer class in test_software.py.
venv: The virtual environment directory, which includes the Python interpreter, libraries, and scripts.


## Authors and acknowledgment
Samana Fatima

## License
This project is currently unlicensed.

## Project status
Completed
