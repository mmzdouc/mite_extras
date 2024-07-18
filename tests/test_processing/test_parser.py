import pytest
from mite_extras.processing.parser import Parser


@pytest.fixture
def raw_json():
    return {
        "Tailoring": [
            ["enzymes-0-enzyme-0-name", "embB"],
            ["enzymes-0-enzyme-0-description", "Cytochrome P450 installing crosslink"],
            ["enzymes-0-enzyme-0-databaseIds", '"genpept:MYS84939.1"'],
            ["enzymes-0-enzyme-0-references", '"doi:10.1101/2023.11.03.565440"'],
            ["enzymes-0-reactions-0-tailoring-0-function", "Biaryl bond formation"],
            ["enzymes-0-reactions-0-tailoring-0-details", ""],
            ["enzymes-0-reactions-0-description", ""],
            [
                "enzymes-0-reactions-0-reaction_smarts-0-reactionSMARTS",
                "[#6]-[#6]-[#6@H](-[#6])-[#6@H](-[#7]-[#6](=O)-[#6@H](-[#6]-[#6]-1=[#6]-[#6]=[#6]-[#6]=[#6]-1)-[#7]-[#6](=O)-[#6@@H](-[#7])-[#6]-[#6]-1=[#6]-[#7]-[#6]-2=[#6]-1-[#6]=[#6]-[#6]=[#6]-2)-[#6](=O)-[#7]-[#6@@H](-[#6]-[#6]-1=[#6]-[#7]-[#6]-2=[#6]-1-[#6]=[#6]-[#6]=[#6]-2)-[#6](-[#8])=O>>[#6]-[#6]-[#6@H](-[#6])-[#6@@H]-1-[#7]-[#6](=O)-[#6@H](-[#6]-[#6]-2=[#6]-[#6]=[#6]-[#6]=[#6]-2)-[#7]-[#6](=O)-[#6@@H](-[#7])-[#6]-[#6]-2=[#6]-[#7]-[#6]-3=[#6]-2-[#6]=[#6]-[#6]=[#6]-3-[#7@@]-2-[#6]=[#6](-[#6]-[#6@H](-[#7]-[#6]-1=O)-[#6](-[#8])=O)-[#6]-1=[#6]-2-[#6]=[#6]-[#6]=[#6]-1",
            ],
            [
                "enzymes-0-reactions-0-reaction_smarts-0-evidence_sm-0-evidenceCode",
                "Heterologous expression",
            ],
            [
                "enzymes-0-reactions-0-reaction_smarts-0-evidence_sm-0-references",
                '"doi:10.1101/2023.11.03.565440"',
            ],
            ["enzymes-0-reactions-0-reaction_smarts-0-databaseIds", ""],
            [
                "enzymes-0-reactions-0-validated_reactions-0-substrate_substructure",
                "CC[C@H](C)[C@H](NC(=O)[C@H](CC1=CC=CC=C1)NC(=O)[C@@H](N)CC1=CNC2=C1C=CC=C2)C(=O)N[C@@H](CC1=CNC2=C1C=CC=C2)C(O)=O",
            ],
            [
                "enzymes-0-reactions-0-validated_reactions-0-product_substructure-0",
                "CC[C@H](C)[C@@H]1NC(=O)[C@H](CC2=CC=CC=C2)NC(=O)[C@@H](N)CC2=CNC3=C2C=CC=C3N2C=C(C[C@H](NC1=O)C(O)=O)C1=C2C=CC=C1",
            ],
            ["enzymes-0-reactions-0-validated_reactions-0-isBalanced", "no"],
            ["enzymes-0-reactions-0-validated_reactions-0-isAuthentic", "yes"],
            ["enzymes-0-reactions-0-validated_reactions-0-isIntermediate", "no"],
            [
                "enzymes-0-reactions-0-validated_reactions-0-evidence_val-0-evidenceCode",
                "Heterologous expression",
            ],
            [
                "enzymes-0-reactions-0-validated_reactions-0-evidence_val-0-references",
                '"doi:10.1101/2023.11.03.565440"',
            ],
            ["enzymes-0-reactions-0-validated_reactions-0-description", ""],
            ["enzymes-0-reactions-0-validated_reactions-0-databaseIds", ""],
            ["enzymes-0-comment", ""],
            ["submit", "Submit"],
        ]
    }


def test_parse_raw_json_valid(raw_json):
    out_dict = Parser().parse_raw_json(name="newfile", input_data=raw_json)
    assert out_dict is not None
