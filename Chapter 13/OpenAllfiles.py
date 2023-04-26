import glob
import pandas as pd

path = r"Files\*.CSV"
files= glob.glob(path)
#print(files)

data=pd.read_csv("file.CSV",  skipfooter=1, engine='python')
print(data)



