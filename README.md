# SmartPlannerTools

This smart advising tool can output a recommended class plan for a student to follow until the student’s graduation based on the student’s career goal, program interests, expected graduation date, etc. 

This software requires one input to generate an output excel form where recommended classes for different semesters are listed. 

The input is the list of courses a student still needs until the student’s graduation, which will be obtained from Degreeworks as a pdf document. If the student select any interest, additional schedules will be made from those interest.

=====================================================================================================

Dependencies
  Python Environments:
    beautifulsoup4==4.11.1
    bs4==0.0.1
    certifi==2022.9.24
    charset-normalizer==2.1.1
    docopt==0.6.2
    et-xmlfile==1.1.0
    idna==3.4
    networkx==2.8.8
    openpyxl==3.0.10
    pipreqs==0.4.11
    PyPDF2==2.11.1
    PySide6==6.4.0.1
    PySide6-Addons==6.4.0.1
    PySide6-Essentials==6.4.0.1
    requests==2.28.1
    shiboken6==6.4.0.1
    soupsieve==2.3.2.post1
    urllib3==1.26.12
    XlsxWriter==3.0.3
    yarg==0.1.9
    
=====================================================================================================

How to run in command prompt
  Open the command prompt and change your current working directory to the SmartPlannerApp folder. 
  Type main.py or python main.py in the command prompt to run the program.
  To run WebExtraction.py, change your current working directory to the Database folder
  Type WebExtraction.py or python WebExtraction.py to run the program.
  
How to run in Visual Studios
  Select the folder SmartPlannerApp then open the file with Visual Studios
  Open main.py in Visual Studios and in the top middle of Visual Studios, click on run. The current document should 
  be main.py.
  To run WebExtraction.py, open WebExtraction.py and set the current document to WebExtraction.py. Click on run
  
=====================================================================================================
  
Authors
  Timothy Potter
  Philip Nguyen
