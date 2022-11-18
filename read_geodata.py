import geopandas

data = geopandas.read_file("./data/dachflaechen_geeignet_pv_2021.gpkg")

data["area"] = data.area

data = data.drop(columns=['geb_id','geometry'])

data.to_csv("area_rad")

print(data)