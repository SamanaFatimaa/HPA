from hpa.tools import Analyzer

test_file_path = "./tests/data/normal_tissue_test.tsv"


def test_number_of_genes():
    """Test if get_number_of_genes return the correct number of distinct genes."""
    analyzer = Analyzer(url_or_path=test_file_path)
    assert analyzer.get_number_of_genes() == 3


def test_distinct_genes():
    """Test if get_distinct_genes returns all distinct genes."""
    analyzer = Analyzer(url_or_path=test_file_path)
    expected_data = ["ENSG00000000003", "ENSG00000000005", "ENSG00000000419"]
    assert expected_data == analyzer.get_distinct_genes()


def test_tissues_by_gene_name():
    """Test if get_tissues_by_gene_name returns distinct tissues as list of strings."""
    analyzer = Analyzer(url_or_path=test_file_path)
    expected_data: list[str] = ["adipose tissue", "vagina"]
    assert expected_data == analyzer.get_tissues_by_gene_name("TSPAN6")