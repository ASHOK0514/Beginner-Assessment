import io
import pandas as pd
import json

df=pd.read_csv("data.csv")

dc=df.to_dict(orient='index')

with io.open("Final.json","w",encoding="utf-8") as f2:
    f2.write(json.dumps(dc,indent=4))
    f2.close
    