#Test Code for Morpheus

import glob
import os
try:
    list_of_mwb_files = glob.glob('C:\\ProgramData\\Malwarebytes\\Malwarebytes\' Anti-Malware\\Logs\\*')# * means all if need specific format then *.csv

    fileArr = []

    for file in list_of_mwb_files:
        if file[60] == 'm':
            fileArr.append(file)
            
    latest_mwb_file = max(fileArr, key=os.path.getctime)

    logArr = []

    with open(latest_mwb_file, encoding='utf16') as f:
        for line in f:
            logArr.append(line)

    
    for x in logArr:
        if "Detected:" in x:
            print(x)
        
except ValueError:
    print("MWB Directory must not exist...")
  
