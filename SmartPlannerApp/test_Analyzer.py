import Analyzer
import Database
import Extractor

sample_input_file = './Input/Sample Input1.pdf'


def test_analyze_data1():
    db = Database.getDatabase()
    classList = Extractor.extractData(sample_input_file)
    scheduleList, inputDict = Analyzer.analyzeData(classList, db)
    assert type(scheduleList) is list


def test_analyze_data2():
    db = Database.getDatabase()
    classList = Extractor.extractData(sample_input_file)
    scheduleList, inputDict = Analyzer.analyzeData(classList, db)
    assert type(inputDict) is dict


def test_analyze_data3():
    db = Database.getDatabase()
    classList = Extractor.extractData(sample_input_file)
    scheduleList, inputDict = Analyzer.analyzeData(classList, db)
    assert len(scheduleList) == 2


def test_analyze_data4():
    db = Database.getDatabase()
    classList = Extractor.extractData(sample_input_file)
    scheduleList, inputDict = Analyzer.analyzeData(classList, db)
    assert type(scheduleList[0]) is list


def test_analyze_data5():
    db = Database.getDatabase()
    classList = Extractor.extractData(sample_input_file)
    scheduleList, inputDict = Analyzer.analyzeData(classList, db)
    assert type(scheduleList[1]) is list


def test_analyze_data6():
    db = Database.getDatabase()
    classList = Extractor.extractData(sample_input_file)
    scheduleList, inputDict = Analyzer.analyzeData(classList, db)
    for l in scheduleList:
        for w in l:
            parts = w.split(' ')
            assert not parts[0][0].isdigit()
            assert parts[0].isupper()
            assert len(parts[0]) == 4


def test_analyze_data7():
    db = Database.getDatabase()
    classList = Extractor.extractData(sample_input_file)
    scheduleList, inputDict = Analyzer.analyzeData(classList, db)
    for l in scheduleList:
        for w in l:
            parts = w.split(' ')
            assert parts[1][0].isdigit()
            assert len(parts[1]) >= 4
