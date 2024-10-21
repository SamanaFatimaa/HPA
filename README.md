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

## Visuals
-

## Installation
1. Clone the HPA repository in a new window 
2. Navigate to the project directory
3. Set up enivornment 
4. Install packages/dependencies (pytest)

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

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

## Contributing
-

## Authors and acknowledgment
Samana Fatima

## License
This project is currently unlicensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
