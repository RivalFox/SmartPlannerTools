import Database


def test_db_not_null():
    db = Database.getDatabase()
    assert db is not None


def test_db_has_data():

    db: dict = Database.getDatabase()
    assert len(db.keys()) > 0


def test_db_has_valid_data():

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
