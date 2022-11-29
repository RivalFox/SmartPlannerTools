import Analyzer
import Compiler
import Database
import Extractor


def test_compile_data_full_time():
    name = 'user'
    stdID = 'password'
    # Full-time
    # Three quarter-time
    # Half-time
    # Less than half-time
    crHrs = 'Full-time'
    choice1 = 'Psychology'
    choice2 = 'Journalism'
    choice3 = 'Statistics'
    inputFile = './Input/Sample Input1.pdf'

    db = Database.getDatabase()

    classList = Extractor.extractData(inputFile)

    scheduleList, inputDict = Analyzer.analyzeData(classList, db)

    import os
    inputFiles = ['./ExcelFiles/Path to Graduation 1.xlsx', './ExcelFiles/Path to Graduation 2.xlsx']
    for inputFile in inputFiles:
        if os.path.isfile(inputFile):
            os.remove(inputFile)
    Compiler.compileData(scheduleList, inputDict, name, stdID, crHrs)
    for inputFile in inputFiles:
        assert os.path.isfile(inputFile)


def test_compile_data_schedule_in_xlsx():
    name = 'user1'
    stdID = 'password1'
    # Full-time
    # Three quarter-time
    # Half-time
    # Less than half-time
    crHrs = 'Full-time'
    choice1 = 'Psychology'
    choice2 = 'Journalism'
    choice3 = 'Statistics'
    inputFile = './Input/Sample Input1.pdf'
    db = Database.getDatabase()
    classList = Extractor.extractData(inputFile)
    scheduleList, inputDict = Analyzer.analyzeData(classList, db)
    inputFiles = ['./ExcelFiles/Path to Graduation 1.xlsx', './ExcelFiles/Path to Graduation 2.xlsx']
    Compiler.compileData(scheduleList, inputDict, name, stdID, crHrs)

    import pandas as pd

    for inputFile in inputFiles:
        try:
            dataframe = pd.read_excel(inputFile, sheet_name='Schedule')
            assert dataframe is not None
            print(dataframe.to_string())
            cn = dataframe.columns.values
            # check that if user and password cols are there or not
            assert name in cn
            assert stdID in cn
            print(cn)
        except:
            # if anyexception reading sheet: Schedule, ValueError will be raised
            # So we are failing this test as no exception should be thrown
            assert False
