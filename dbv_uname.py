import sys
import os
import re
from PyPDF2 import PdfFileReader
from pathlib import PurePath
from pathlib import PureWindowsPath

if len(sys.argv) == 1: 
    print("No files imported - Please drag and drop your files")
else: 
    print('Number of given files:', len(sys.argv)-1, 'Files')
    for filename in sys.argv[1:]: 
        date_pattern = "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
        reader = PdfFileReader(filename)
        page = reader.pages[0]
        page_content = page.extractText()
        dates = re.findall(date_pattern, page_content)
        rawdate= dates[0]
        converteddate = rawdate.split(".")
        year = converteddate[2]
        month = converteddate[1]
        day = converteddate[0]
        newfilename = str(PureWindowsPath(filename).parents[0])+"\\"+year+"-"+month+"-"+day+"_"+"DKB"+'_'+"Leistungsabrechnung"+'.pdf'

        print("Old Filename:")
        print(filename)

        print("New Filename:")
        print (newfilename)
        print("---------")
        try :
            os.rename(filename, newfilename)
        
        except IsADirectoryError:
            print("Source is a file but destination is a directory.")
        
        except NotADirectoryError:
            print("Source is a directory but destination is a file.")

        except NotADirectoryError:
            print("Source is a directory but destination is a file.")

        except PermissionError:
            print("Operation not permitted.")

        except OSError as error:
            print(error)


wait = input("Click to exit...") 
