import os
import json
import urllib.request

# Unsplash high quality infrastructure & construction image IDs
# Real Unsplash image URLs: https://images.unsplash.com/photo-<ID>?w=1000&auto=format&fit=crop&q=80

photo_urls = {
    # Road / Bridge / Construction / Buildings / Water Infra
    "site-001-before": "https://images.unsplash.com/photo-1541888946425-d0fbb186a5b7?w=1000&auto=format&fit=crop&q=80", # bridge crack / concrete construction
    "site-001-after":  "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=1000&auto=format&fit=crop&q=80", # repaired structure
    
    "site-002-before": "https://images.unsplash.com/photo-1584463674656-78e24c6530ec?w=1000&auto=format&fit=crop&q=80", # damaged road
    "site-002-after":  "https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1000&auto=format&fit=crop&q=80", # paved new asphalt road
    
    "site-003-before": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1000&auto=format&fit=crop&q=80", # building roof work
    "site-003-after":  "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1000&auto=format&fit=crop&q=80", # modern renovated building roof
    
    "site-004-before": "https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=1000&auto=format&fit=crop&q=80", # exposed trench / pipes
    "site-004-after":  "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=1000&auto=format&fit=crop&q=80", # properly installed water infrastructure
    
    "site-005-before": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1000&auto=format&fit=crop&q=80", # architectural structure framework
    "site-005-after":  "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1000&auto=format&fit=crop&q=80", # clean hospital building block
    
    "site-006-before": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1000&auto=format&fit=crop&q=80", # mountain slope / landslide site
    "site-006-after":  "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1000&auto=format&fit=crop&q=80", # stabilized mountain road highway
    
    "site-007-before": "https://images.unsplash.com/photo-1588072432836-e10032774350?w=1000&auto=format&fit=crop&q=80", # old school facility building
    "site-007-after":  "https://images.unsplash.com/photo-1577896851231-70ef18881754?w=1000&auto=format&fit=crop&q=80", # bright vibrant modern anganwadi facility
    
    "site-008-before": "https://images.unsplash.com/photo-1590069261209-f8e9b8642343?w=1000&auto=format&fit=crop&q=80", # under construction housing site
    "site-008-after":  "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1000&auto=format&fit=crop&q=80", # completed housing apartment block
    
    "site-009-before": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=1000&auto=format&fit=crop&q=80", # river embankment flood area
    "site-009-after":  "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1000&auto=format&fit=crop&q=80", # reinforced river bank spur wall
    
    "site-010-before": "https://images.unsplash.com/photo-1517649763962-0c623266010b?w=1000&auto=format&fit=crop&q=80", # flyover expansion joint gap
    "site-010-after":  "https://images.unsplash.com/photo-1494526585095-c41746248156?w=1000&auto=format&fit=crop&q=80", # smooth flyover bridge surface
    
    "site-011-before": "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=1000&auto=format&fit=crop&q=80", # empty room lab under work
    "site-011-after":  "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1000&auto=format&fit=crop&q=80", # fully equipped modern science lab
    
    "site-012-before": "https://images.unsplash.com/photo-1509391365360-2e959784a276?w=1000&auto=format&fit=crop&q=80", # solar installation work
    "site-012-after":  "https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=1000&auto=format&fit=crop&q=80", # operational solar pump field
    
    "site-013-before": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1000&auto=format&fit=crop&q=80", # flooded drain ditch construction
    "site-013-after":  "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=1000&auto=format&fit=crop&q=80", # clean stormwater concrete box drain
    
    "site-014-before": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1000&auto=format&fit=crop&q=80", # bare metal truss steel frame
    "site-014-after":  "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1000&auto=format&fit=crop&q=80", # completed public canteen facility
    
    "site-015-before": "https://images.unsplash.com/photo-1581094288338-2314dddb7ecc?w=1000&auto=format&fit=crop&q=80", # pile foundation work near water
    "site-015-after":  "https://images.unsplash.com/photo-1569263979104-865ab7cd8d13?w=1000&auto=format&fit=crop&q=80"  # finished river jetty platform
}

os.makedirs("shared/photos", exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

print("Downloading photos to shared/photos/...")
for key, url in photo_urls.items():
    dest_path = f"shared/photos/{key}.jpg"
    if not os.path.exists(dest_path):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp, open(dest_path, 'wb') as out_file:
                out_file.write(resp.read())
            print(f"Downloaded {key}.jpg")
        except Exception as e:
            print(f"Error downloading {key}: {e}")
    else:
        print(f"Already exists: {key}.jpg")

