# 1. load roughness data for each pipe from a CSV file
# 1.1. import CsvReader from LumenWorks.Framework.IO.dll
# 1.1.1. reference to the dll
import clr
from System.Reflection import Assembly
assemblyPath = r"C:\Users\tavanai2\Desktop\CodeTests\LumenWorks.Framework.IO.dll"
assembly = Assembly.LoadFile(assemblyPath)
clr.AddReference(assembly)

# 1.1.2. import StreamReader and CsvReader
from System.IO import StreamReader
from LumenWorks.Framework.IO.Csv import CsvReader

# 1.2. read the CSV file and save it in a list "pipeRogh"
fileReader = StreamReader("C:/Users/tavanai2/Desktop/CodeTests/RoghnessTable.csv")
csvReader = CsvReader(fileReader, False)
pipeRogh = []
while csvReader.ReadNextRecord():
    row = []
    colCount = csvReader.FieldCount
    for i in range(colCount):
        row.append(csvReader[i])
    pipeRogh.append(row)
print pipeRogh
csvReader.Close()
fileReader.Close()
