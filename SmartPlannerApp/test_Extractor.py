import Extractor

sample_input_file = './Input/Sample Input1.pdf'


def test_extract_data():
    r = Extractor.extractData(sample_input_file)
    assert type(r) is list


def test_extract_data1():
    r = Extractor.extractData(sample_input_file)
    assert len(r) == 2


def test_extract_data2():
    r = Extractor.extractData(sample_input_file)
    r0 = r[0]
    r1 = r[1]
    assert type(r0) is list
    assert type(r1) is list


def test_extract_data3():
    r = Extractor.extractData(sample_input_file)
    r1 = r[1]
    assert set(r1) == {'CPSC 1302', 'CPSC 1301K', 'CPSC 2108', 'CPSC 4115', 'CPSC 4111', 'CPSC 6180', 'CPSC 6185',
                       'CPSC 6985',
                       'CYBR 2159', 'CYBR 2160', 'CYBR 3106', 'CYBR 3108', 'CYBR 3115', 'CYBR 3119'}


def test_extract_data4():
    import os
    inputFile = './Input/inputText.txt'
    if os.path.isfile(inputFile):
        os.remove(inputFile)
    Extractor.extractData(sample_input_file)
    assert os.path.isfile(inputFile)


def test_create_list():
    r = Extractor.createList('./Input', 'inputText.txt')
    assert set(r[1]) == {'CPSC 1302', 'CPSC 1301K', 'CPSC 2108', 'CPSC 4115', 'CPSC 4111', 'CPSC 6180', 'CPSC 6185',
                         'CPSC 6985',
                         'CYBR 2159', 'CYBR 2160', 'CYBR 3106', 'CYBR 3108', 'CYBR 3115', 'CYBR 3119'}
