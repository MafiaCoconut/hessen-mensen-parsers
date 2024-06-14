from src.infrastructure.interfaces_impl.marburg_parsers_impl.marburg_bistro_parser_interface_impl import MarburgBistroParserInterfaceImpl

def test_parse():
    assert isinstance(MarburgBistroParserInterfaceImpl().parse(), dict)