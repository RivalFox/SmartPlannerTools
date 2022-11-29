import Database


def test_db_not_null():
    db = Database.getDatabase()
    assert db is not None


def test_db_has_data():
    # {'Name': 'ACCT 3111', 'Description': 'Intermediate Accounting I', 'Credits': '3',
    #  'Semester': {'Spring': True, 'Summer': False, 'Fall': True},
    #  'Prerequisite': {'ENGL 1101': '', 'ENGL 1102': '', 'ACCT 2101': '', 'ACCT 2102': '', 'ECON 2105': '',
    #                   'ECON 2106': '', 'BUSA 2115': '', 'BUSA 2100': '', 'MATH 1001': '', 'MATH 1101': '',
    #                   'MATH 1111': '', 'MATH 1113': '', 'MATH 1125': '', 'MATH 1131': ''}}

    db: dict = Database.getDatabase()
    assert len(db.keys()) > 0


def test_db_has_valid_data():
    # {'Name': 'ACCT 3111', 'Description': 'Intermediate Accounting I', 'Credits': '3',
    #  'Semester': {'Spring': True, 'Summer': False, 'Fall': True},
    #  'Prerequisite': {'ENGL 1101': '', 'ENGL 1102': '', 'ACCT 2101': '', 'ACCT 2102': '', 'ECON 2105': '',
    #                   'ECON 2106': '', 'BUSA 2115': '', 'BUSA 2100': '', 'MATH 1001': '', 'MATH 1101': '',
    #                   'MATH 1111': '', 'MATH 1113': '', 'MATH 1125': '', 'MATH 1131': ''}}

    db: dict = Database.getDatabase()
    all_possible_keys = ['Name', 'Description', 'Credits', 'Semester', 'Prerequisite']

    for k, v in db.items():
        present_keys = list(v.keys())
        assert set(present_keys).issubset(set(all_possible_keys))

        assert type(v['Name']) is str
        assert type(v['Description']) is str
        assert type(v['Credits']) is str
        assert type(v['Semester']) is dict
        if 'Prerequisite' in present_keys:
            assert type(v['Prerequisite']) is dict

        semester_keys = v['Semester'].keys()
        assert set(semester_keys) == {'Spring', 'Summer', 'Fall'}

        split = v['Name'].split(' ')
        split_ = split[0]
        assert len(split_) <= 4

        assert type(v['Semester']['Spring']) is bool
        assert type(v['Semester']['Summer']) is bool
        assert type(v['Semester']['Fall']) is bool
