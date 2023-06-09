#Script to transform sql-update-staments in a text to insert-statements
#the update-staments can only consist of two columns
#INSERT INTO TABLENAME (COLUMN1, COLUMN2), VALUES(COLUMNVALUE1, COLUMNVALUE2)
#the statements will be transformed to
#UPDATE TABLENAME SET COLUMN2 = COLUMNVALUE2 WHERE COLUMN1 = COLUMNVALUE1


import sys
import os.path


def splitline(line):
  lineparts = line.split(" ", 7)
  return lineparts;

def insertlineparts2updateline(insertlineparts):
    tablename = insertlineparts[2]
    setcolumn = insertlineparts[4].strip(')')
    setcolumnvalue = insertlineparts[7]
    setcolumnvalue = setcolumnvalue.strip(';')
    setcolumnvalue = setcolumnvalue.strip(')')
    
    
    wherecolumn = insertlineparts[3].strip('(').strip(',');
    wherecolumnvalue = insertlineparts[6].strip('(').strip(','); 
    return 'UPDATE ' + tablename + ' SET ' + setcolumn + ' = ' + setcolumnvalue + ' WHERE ' + wherecolumn + ' = ' + wherecolumnvalue + ';'
    

if len(sys.argv) < 2:
    print('Usage: Insert2Update <path to file with sql-insert statements>')
else:
    insertsfilepath = sys.argv[1]

    if os.path.isfile(insertsfilepath):
        insertsfile = open(insertsfilepath)
        try:
            for insertline in insertsfile:
                insertline = insertline.strip('\n')
                insertlineparts = splitline(insertline);
                updateline = insertlineparts2updateline(insertlineparts)
                print(updateline)
        except:
            print('cannot read file ' + insertsfilepath)
        insertsfile.close()
    else:
        print('file ' + insertsfilepath + ' does not exist')


