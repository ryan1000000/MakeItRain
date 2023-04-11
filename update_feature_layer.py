from arcgis.gis import GIS
from arcgis.features import FeatureLayer
from datetime import datetime

def update_maintenance_dates():
    # Replace with your ArcGIS Online account credentials
    username = 'GISGreendrop'
    password = 'Greendrop01'

    # URL of your hosted feature layer
    feature_layer_url = 'https://services8.arcgis.com/HQs4mlvbVkaKMcl1/arcgis/rest/services/wpg_trees_2023/FeatureServer/0'

    # Authenticate and connect to your GIS
    gis = GIS('https://www.arcgis.com', username, password)

    # Access the hosted feature layer
    feature_layer = FeatureLayer(feature_layer_url, gis)

    # Update the maintenancedate20 field with the current date
    current_date = datetime.now()

    # Query all features in the hosted feature layer
    features = feature_layer.query(where='1=1')

    # Update the maintenancedate20 field for all features
    for feature in features:
        feature.attributes['maintenancedate20'] = current_date

    # Apply the updates to the hosted feature layer
    result = feature_layer.edit_features(updates=features)
