import pandas
import geopandas


def read_geodata():
    data = geopandas.read_file("./data/solar/gebaeude_pv_2021.gpkg")
    data.sort_values('sum_modarea', ascending=False, inplace=True)
    data["total area"] = data.area
    data.drop(columns=['geometry'], inplace=True)
    file = pandas.HDFStore('data/solar/solar_data.h5')
    data['lage'] = data['lage'].astype(str)
    data['geb_id'] = data['geb_id'].astype(str)
    data['geb_funktion'] = data['geb_funktion'].astype(str)
    file['solar_data'] = data
