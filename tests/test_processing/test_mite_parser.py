import pytest
from mite_extras.processing.data_classes import (
    Changelog,
    ChangelogEntry,
    Entry,
    EnzymeAux,
    Evidence,
    Reaction,
    ReactionEx,
)
from mite_extras.processing.mite_parser import MiteParser


@pytest.fixture
def mite_json():
    return {
        "accession": "MITE0000000",
        "quality": "medium",
        "status": "pending",
        "retirementReasons": ["Example reason"],
        "changelog": {
            "releases": [
                {
                    "version": "1.0",
                    "date": "2024-07-30",
                    "entries": [
                        {
                            "contributors": ["AAAAAAAAAAAAAAAAAAAAAAAA"],
                            "reviewers": ["AAAAAAAAAAAAAAAAAAAAAAAA"],
                            "date": "2024-03-21",
                            "comment": "Initial entry.",
                        },
                        {
                            "contributors": ["AAAAAAAAAAAAAAAAAAAAAAAA"],
                            "reviewers": ["AAAAAAAAAAAAAAAAAAAAAAAA"],
                            "date": "2024-03-21",
                            "comment": "Initial entry.",
                        },
                    ],
                }
            ]
        },
        "enzyme": {
            "name": "aviG6",
            "description": "putative methyltransferase",
            "databaseIds": ["genpept:AAK83186.1", "mibig:BGC0000026"],
            "auxiliaryEnzymes": [
                {
                    "name": "AbcD",
                    "description": "A nonexisting enzyme",
                    "databaseIds": ["genpept:AAK83186.1", "mibig:BGC0000026"],
                }
            ],
            "references": ["pubmed:15489167"],
        },
        "reactions": [
            {
                "tailoring": ["Methylation"],
                "reactionSMARTS": {
                    "reactionSMARTS": "[#6:1]-[#8:21]-[#6:22]-[#6@H:58]-1-[#8:57]-[#6@@H:56](-[#8:51]-[#6@@H:50]-2-[#8:45]-[#6:46]-[#6@@H:47]-3-[#8:44][C@:43]4([#8:42]-[#6@H:48]-3-[#6@H:49]-2-[#8:28]-[#6:27](=[O:26])-[#6:25](-[#6:23])-[#6:24])[#8:37]-[#6@H:38](-[#6:36])[C@:39]([#8:32])([#6:40]-2-[#8:31]-[#6:30]-[#8:29]-[#6:41]4-2)[#6:35](-[#6:33])=[O:34])-[#6@@H:55](-[#8:52])-[#6@@H:54](-[#8:53])-[#6@@H:59]-1-[#8:60]-[#6@@H:67]-1-[#8:66]-[#6@H:65](-[#6:61])-[#6@H:64](-[#8:63]-[#6:62])-[#6@H:69](-[#8:70]-[#6@H:75]-2-[#6:74][C@@:73]3([#6:71])[#8:72][C:83]4([#6:82]-[#6@H:81](-[#8:80])-[#6@H:86](-[#8:87]-[#6@H:89]-5-[#6:90]-[#6@@H:91](-[#8:17])-[#6@H:92](-[#8:16]-[#6:15](=[O:14])-[c:13]6[c:12](-[#6:3])[c:11]([Cl:4])[c:10](-[#8:5])[c:9]([Cl:6])[c:8]6-[#8:7]-[#6:2])-[#6@@H:93](-[#6:94])-[#8:88]-5)-[#6@@H:85](-[#6:18])-[#8:84]4)[#8:79]-[#6@@H:78]3-[#6@@H:77](-[#6:19])-[#8:76]-2)-[#6@H:68]-1-[#8:20]>>[#6:1]-[#8:21]-[#6:22]-[#6@H:58]-1-[#8:57]-[#6@@H:56](-[#8:51]-[#6@@H:50]-2-[#8:45]-[#6:46]-[#6@@H:47]-3-[#8:44][C@:43]4([#8:42]-[#6@H:48]-3-[#6@H:49]-2-[#8:28]-[#6:27](=[O:26])-[#6:25](-[#6:23])-[#6:24])[#8:37]-[#6@H:38](-[#6:36])[C@:39]([#8:32])([#6:40]-2-[#8:31]-[#6:30]-[#8:29]-[#6:41]4-2)[#6:35](-[#6:33])=[O:34])-[#6@@H:55](-[#8:52]-[#6:100])-[#6@@H:54](-[#8:53])-[#6@@H:59]-1-[#8:60]-[#6@@H:67]-1-[#8:66]-[#6@H:65](-[#6:61])-[#6@H:64](-[#8:63]-[#6:62])-[#6@H:69](-[#8:70]-[#6@H:75]-2-[#6:74][C@@:73]3([#6:71])[#8:72][C:83]4([#6:82]-[#6@H:81](-[#8:80])-[#6@H:86](-[#8:87]-[#6@H:89]-5-[#6:90]-[#6@@H:91](-[#8:17])-[#6@H:92](-[#8:16]-[#6:15](=[O:14])-[c:13]6[c:12](-[#6:3])[c:11]([Cl:4])[c:10](-[#8:5])[c:9]([Cl:6])[c:8]6-[#8:7]-[#6:2])-[#6@@H:93](-[#6:94])-[#8:88]-5)-[#6@@H:85](-[#6:18])-[#8:84]4)[#8:79]-[#6@@H:78]3-[#6@@H:77](-[#6:19])-[#8:76]-2)-[#6@H:68]-1-[#8:20] |r|",
                    "isIterative": False,
                },
                "reactions": [
                    {
                        "substrate": "[CH3:1][O:21][CH2:22][C@H:58]1[O:57][C@@H:56]([O:51][C@@H:50]2[O:45][CH2:46][C@@H:47]3[O:44][C@@:43]4([O:37][C@H:38]([CH3:36])[C@@:39]([OH:32])([C:35]([CH3:33])=[O:34])[CH:40]5[O:31][CH2:30][O:29][CH:41]54)[O:42][C@H:48]3[C@H:49]2[O:28][C:27]([CH:25]([CH3:23])[CH3:24])=[O:26])[C@@H:55]([OH:52])[C@@H:54]([OH:53])[C@@H:59]1[O:60][C@@H:67]1[O:66][C@H:65]([CH3:61])[C@H:64]([O:63][CH3:62])[C@H:69]([O:70][C@H:75]2[CH2:74][C@@:73]3([CH3:71])[O:72][C:83]4([O:79][C@@H:78]3[C@@H:77]([CH3:19])[O:76]2)[CH2:82][C@H:81]([OH:80])[C@H:86]([O:87][C@@H:89]2[O:88][C@H:93]([CH3:94])[C@@H:92]([O:16][C:15]([c:13]3[c:8]([O:7][CH3:2])[c:9]([Cl:6])[c:10]([OH:5])[c:11]([Cl:4])[c:12]3[CH3:3])=[O:14])[C@H:91]([OH:17])[CH2:90]2)[C@@H:85]([CH3:18])[O:84]4)[C@H:68]1[OH:20]",
                        "products": [
                            "[CH3:1][O:21][CH2:22][C@H:58]1[O:57][C@@H:56]([O:51][C@@H:50]2[O:45][CH2:46][C@@H:47]3[O:44][C@@:43]4([O:37][C@H:38]([CH3:36])[C@@:39]([OH:32])([C:35]([CH3:33])=[O:34])[CH:40]5[O:31][CH2:30][O:29][CH:41]54)[O:42][C@H:48]3[C@H:49]2[O:28][C:27]([CH:25]([CH3:23])[CH3:24])=[O:26])[C@@H:55]([O:52][CH3:100])[C@@H:54]([OH:53])[C@@H:59]1[O:60][C@@H:67]1[O:66][C@H:65]([CH3:61])[C@H:64]([O:63][CH3:62])[C@H:69]([O:70][C@H:75]2[CH2:74][C@@:73]3([CH3:71])[O:72][C:83]4([O:79][C@@H:78]3[C@@H:77]([CH3:19])[O:76]2)[CH2:82][C@H:81]([OH:80])[C@H:86]([O:87][C@@H:89]2[O:88][C@H:93]([CH3:94])[C@@H:92]([O:16][C:15]([c:13]3[c:8]([O:7][CH3:2])[c:9]([Cl:6])[c:10]([OH:5])[c:11]([Cl:4])[c:12]3[CH3:3])=[O:14])[C@H:91]([OH:17])[CH2:90]2)[C@@H:85]([CH3:18])[O:84]4)[C@H:68]1[OH:20]"
                        ],
                        "isBalanced": False,
                        "isIntermediate": False,
                    }
                ],
                "evidence": [
                    {
                        "evidenceCode": ["Knock-out studies"],
                        "references": ["pubmed:15489167"],
                    }
                ],
            }
        ],
    }


def test_get_changelog_entries_valid(mite_json):
    parser = MiteParser()
    log = parser.get_changelog_entries(
        entries=mite_json.get("changelog").get("releases")[0].get("entries")
    )
    assert len(log) == 2
    assert isinstance(log[0], ChangelogEntry)


def test_get_changelog_valid(mite_json):
    parser = MiteParser()
    log = parser.get_changelog(releases=mite_json.get("changelog").get("releases"))
    assert len(log) == 1
    assert isinstance(log[0], Changelog)


def test_get_auxenzymes_valid(mite_json):
    parser = MiteParser()
    log = parser.get_auxenzymes(
        auxenzymes=mite_json.get("enzyme").get("auxiliaryEnzymes")
    )
    assert len(log) == 1
    assert isinstance(log[0], EnzymeAux)


def test_get_reactionex_valid(mite_json):
    parser = MiteParser()
    log = parser.get_reactionex(
        reactions=mite_json.get("reactions")[0].get("reactions")
    )
    assert len(log) == 1
    assert isinstance(log[0], ReactionEx)


def test_get_evidence_valid(mite_json):
    parser = MiteParser()
    log = parser.get_evidence(evidences=mite_json.get("reactions")[0].get("evidence"))
    assert len(log) == 1
    assert isinstance(log[0], Evidence)


def test_get_reactions_valid(mite_json):
    parser = MiteParser()
    log = parser.get_reactions(reactions=mite_json.get("reactions"))
    assert len(log) == 1
    assert isinstance(log[0], Reaction)


def test_parse_raw_json_valid(mite_json):
    parser = MiteParser()
    parser.parse_mite_json(data=mite_json)
    assert isinstance(parser.entry, Entry)
