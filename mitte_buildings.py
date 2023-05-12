import numpy as np
import pandas
import geopandas

## get Mitte addresses
# load address data base
address_data = pandas.read_csv('data/HKO_EPSG5650/adressen-be_mitPLZ.txt', delimiter=';', header=None)
# filter for Mitte
mitte = address_data[address_data.iloc[:, 6] == 1].iloc[:, [9, 13]]
# merge street & house number
mitte = mitte[13] + ' ' + mitte[9].astype(str)

## load PV potential data
solar_data = geopandas.read_file("./data/pv_2021/gebaeude_pv_2021.gpkg").drop(columns='geometry')
solar_data.sort_values('sum_modarea', ascending=False, inplace=True)
solar_data["Mitte?"] = np.nan

# iterate through buildings to check if in Mitte, limited to N largest for computational speed
N = 10000
count = 0
for index, row in solar_data.iterrows():
    count = count + 1
    street = row['lage']
    if not isinstance(street, str):
        continue
    switch = 0
    for i in range(len(street)):
        if not street[i].isnumeric():
            if switch == 1:
                street = street[:i]
                break
        else:
            switch = 1

    if street in set(mitte):
        solar_data.loc[index, "Mitte?"] = 1
    else:
        solar_data.loc[index, "Mitte?"] = 0

    if count == N:
        break

# save dataset to Excel file
solar_data.iloc[:N, :].to_excel("solar_data_mitte.xlsx")
