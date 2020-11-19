import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = set(data["LAT"])
lon = set(data["LON"])
elev = set(data['ELEV'])

map = folium.Map(location=[38.58,-99.09],zoom_start=6,title="Stamen Terrian")

# Volcanoes Map
fgv = folium.FeatureGroup(name="Volcanoes")

# for cord in [[38.2,99.1],[39.2,-97.1]]:
#     fg.add_child(folium.Marker(location=cord, popup="i am marker",icon=folium.Icon(color="green")))

def color_producer(el):
    if el <1000:
        return 'green'
    elif 1000<= el < 3000:
        return 'orange'
    else:
        return 'red'

# Marker
# for lt,ln,el in zip(lat,lon,elev):
#     fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m",icon=folium.Icon(color_producer(el))))

# CircleMarker
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=str(el)+" m",icon=folium.Icon(color_producer(el)),fill_color=color_producer(el),color="grey",fill_opacity=0.7))

# popup= folium.Popup(str(el),parse_html=True)

# Population Map
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000 else 'black' if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save('map1.html')
