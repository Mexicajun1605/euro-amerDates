#Rename dates from European to American

import shutil, os, re

#Create a regex that matches files with the American Date format

datePattern = re.compile(r"""^(.*?) #all text before the date
    ((0|1)?\d)-  #one or two digits for the month
    ((0|1|2|3)?\d)- #one or two digits for the day
    ((19|20)\d\d)   #four digits for the year
    (.*?)$      #all text after the date
""", re.VERBOSE)

#Loop over the files in the working directory
for eurofilename in os.listdir('.'):
    mo = datePattern.search(eurofilename)

    #skip files without a date
    if mo == None:
        continue

    #Get the different parts of the file name
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #form the American style filename
    amerfilename = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart

    #Get the full, absolute file paths.
    absworkingdir = os.path.abspath('.')
    amerfilename = os.path.join(absworkingdir, amerfilename)
    eurofilename = os.path.join(absworkingdir, eurofilename)

    #Rename the files
    print('Renaming "%s" to "%s"...' % (eurofilename, amerfilename))
    #shutil.move(eurofilename, amerfilename) #uncomment after testing