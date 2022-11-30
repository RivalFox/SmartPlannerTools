import Extractor

sample_input_file = './Input/Sample Input1.pdf'


def test_extract_data():
    r = Extractor.extractData(sample_input_file)
    assert type(r) is list


def test_extract_data1():
    r = Extractor.extractData(sample_input_file)
    assert len(r) == 1


def test_extract_data2():
    r = Extractor.extractData(sample_input_file)
    r0 = r[0]
    assert type(r0) is list


def test_extract_data3():
    r = Extractor.extractData(sample_input_file)
    r0 = r[0]
    assert set(r0) == {'POLS 1101', 'CPSC 3165', 'CPSC 4000', 
                        'CPSC 3121', 'CPSC 5115', 'CPSC 4135', 
                        'CPSC 5135', 'CPSC 4148', 'CPSC 5128', 
                        'CPSC 4155', 'CPSC 5155', 'CPSC 4157', 
                        'CPSC 5157', 'CPSC 4175', 'CPSC 4176', 
                        'MATH 3111', 'DSCI 3111'}


def test_extract_data4():
    import os
    inputFile = './Input/inputText.txt'
    if os.path.isfile(inputFile):
        os.remove(inputFile)
    Extractor.extractData(sample_input_file)
    assert os.path.isfile(inputFile)


def test_create_list():
    r = Extractor.createList('./Input', 'inputText.txt')
    assert set(r[0]) == {'POLS 1101', 'CPSC 3165', 'CPSC 4000', 
                        'CPSC 3121', 'CPSC 5115', 'CPSC 4135', 
                        'CPSC 5135', 'CPSC 4148', 'CPSC 5128', 
                        'CPSC 4155', 'CPSC 5155', 'CPSC 4157', 
                        'CPSC 5157', 'CPSC 4175', 'CPSC 4176', 
                        'MATH 3111', 'DSCI 3111'}
