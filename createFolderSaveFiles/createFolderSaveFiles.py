import csv
import os
import shutil

#folderPath = input('Enter folder path: ')
with open('demoInputData.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for rows in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(rows)}')
            line_count += 1
        else:
            #print(f'\t{rows[0]}, \t{rows[1]}')
            directoryNew = rows[0]
            fileToMove = rows[1]
            fullpath = os.path.join(os.getcwd(),directoryNew)
            isExists = os.path.exists(fullpath)
            if not isExists:
                os.mkdir(fullpath)
                print("Directory created at path ",fullpath)
            
            isFileExists = os.path.isfile(fileToMove)
            if(isFileExists):
                shutil.copy(fileToMove,fullpath)
                print("File successfully copy from [%s] to new folder at path [%s]",fileToMove,fullpath)
            line_count += 1
    print(f'Processed {line_count} lines')
