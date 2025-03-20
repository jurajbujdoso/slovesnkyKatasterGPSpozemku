#!/usr/bin/python3
import math
import sys
import json

def web_mercator_to_wgs84(x, y):
    """
    Konvertuje súradnice z Web Mercator (EPSG:3857) na WGS84 (EPSG:4326)
    Vracia [longitude, latitude]
    """
    # Konštanty
    EARTH_RADIUS = 6378137.0  # Polomer Zeme v metroch
    
    # Konverzia x na longitude
    longitude = (x * 180) / (EARTH_RADIUS * math.pi)
    
    # Konverzia y na latitude
    y = y / EARTH_RADIUS
    latitude = (2 * math.atan(math.exp(y)) - (math.pi / 2)) * 180 / math.pi
    
    return [longitude, latitude]

def main():
    # Kontrola, či bol zadaný parameter príkazového riadku
    if len(sys.argv) < 2:
        print("Použitie: python program.py 'cesta_k_suboru.json'")
        print("alebo: python program.py '{\"rings\": [[[x1,y1], [x2,y2], ...]]}'")
        sys.exit(1)
    
    input_data = sys.argv[1]
    
    try:
        # Skús spracovať vstup priamo ako JSON
        data = json.loads(input_data)
        
        # Skontroluj či vstupný JSON obsahuje kľúč 'rings' alebo 'geometry'
        if "rings" in data:
            rings = data["rings"]
        elif "geometry" in data and "rings" in data["geometry"]:
            rings = data["geometry"]["rings"]
        elif "features" in data and len(data["features"]) > 0:
            rings = data["features"][0]["geometry"]["rings"]
        else:
            print("Chyba: Nepodarilo sa nájsť 'rings' v zadaných dátach.")
            sys.exit(1)
    
    except json.JSONDecodeError:
        # Ak vstup nie je validný JSON, skús ho načítať ako cestu k súboru
        try:
            with open(input_data, 'r') as file:
                data = json.load(file)
                
                # Skontroluj či vstupný súbor obsahuje kľúč 'rings' alebo 'geometry'
                if "rings" in data:
                    rings = data["rings"]
                elif "geometry" in data and "rings" in data["geometry"]:
                    rings = data["geometry"]["rings"]
                elif "features" in data and len(data["features"]) > 0:
                    rings = data["features"][0]["geometry"]["rings"]
                else:
                    print("Chyba: Nepodarilo sa nájsť 'rings' v zadanom súbore.")
                    sys.exit(1)
        
        except Exception as e:
            print(f"Chyba pri čítaní súboru: {e}")
            sys.exit(1)
    
    # Konverzia všetkých bodov
    gps_coordinates = []
    for ring in rings:
        gps_ring = []
        for point in ring:
            x, y = point
            gps_point = web_mercator_to_wgs84(x, y)
            gps_ring.append(gps_point)
        gps_coordinates.append(gps_ring)
    
    # Výpis výsledkov
    print("Latitude,Longitude,Name")
    for i, ring in enumerate(gps_coordinates):
        for j, point in enumerate(ring):
            print(f"{point[1]:.6f}, {point[0]:.6f}, P{i}Bod{j+1}")

if __name__ == "__main__":
    main()
