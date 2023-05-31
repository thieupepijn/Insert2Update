import sys


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
    



insertsfilepath =  sys.argv[1]
insertsfile = open(insertsfilepath)



for insertline in insertsfile:
    insertline = insertline.strip('\n')
    insertlineparts = splitline(insertline);
    updateline = insertlineparts2updateline(insertlineparts)
    print(updateline)

