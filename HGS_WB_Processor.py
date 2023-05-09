# Import Required Libraries
import pandas as pd
from IPython.display import display

with open("CBCR_UnsatClimDewatero.water_balance.dat", "r") as fin:
    lines = fin.readlines()
with open("WB.dat", "w") as fout:
    for line in lines:
        line = line.lstrip()
        if "VARIABLES =" in line:
            line = line.replace("VARIABLES =","").replace(",","   ").replace('"',"").replace("_","")
            line = line.lstrip()
        if line.strip("\n") != "# Tecplot Point File" and line.strip("\n") != 'zone t="CBCR_UnsatClimDewater"' and line.strip("\n") != "#I=IMAX#####" and line.strip("\n") != 'Title = "Transient water balance summary"' and line.strip("\n") != "VARIABLES =":
            fout.write(line)
        
df = pd.read_table("WB.dat", sep = "  ")
display(df)

df.reset_index(inplace = True)
df['CBay_Gal_m3_day'] = df[' Helev3']*86400
df['CRand_Gal_m3_day'] = df[' Helev4']*86400

df.to_csv("WB.csv")

