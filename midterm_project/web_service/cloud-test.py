import requests

url = 'http://cemk.pythonanywhere.com/predict'


building = {"compactness": 0.9,
        "surface_area": 563.5,
        "wall_area": 318.5,
        "roof_area": 122.5,
        "height": 7.0,
        "orientation": 5.0,
        "glazing_area": 0.4,
        "glazing_distribution": 4.0}


response = requests.post(url, json=building).json()

print(response)


