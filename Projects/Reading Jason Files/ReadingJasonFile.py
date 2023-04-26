
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json
import pandas as pd
#import plotly_express as px
import json
print("Library imported")

def getJsonFile(path):
    with open(path) as file:
        f = json.load(file)
    return f

metadata_dict = getJsonFile(r"C:\Users\Manuela.Chadreque\OneDrive - EOH\02. STUDY\Data Eng\Python\Project\Json File\list_of_metadata_10k.json")
print(metadata_dict['0'])


# Creating the table with all the infos related to the Budz¶

budz_df = pd.DataFrame(metadata_dict).T.reset_index()

budz_df["index"]= budz_df["index"].astype(int)

print("++++++++++++++++++++++++++++++++++++++++++")
print(budz_df.head())