import os
import folium
import gpxpy


if __name__ == "__main__":
    print('Creating map started...')
    # List the GPX files from the directory:
    routes = []
    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".gpx"):
                routes.append(filepath)
    # Construct a base map:
    map = folium.Map(location=[52.45923056388143, 6.019973188923583], zoom_start=7.7)
    # Read the GPX files and add the routes to the map:
    for route in routes:
        gpx = gpxpy.parse(open(route))
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        name = route.split('/')[-1][:-4]
        # Create a FG per route, for layer control
        fg = folium.FeatureGroup(name=name)
        folium.PolyLine(points, color='red', weight=4.5, opacity=.5).add_to(fg)
        map.add_child(fg)
    # Provide layer control for end user:
    folium.LayerControl(collapsed=True).add_to(map)
    map.save("Map1.html")
    print('All done')

