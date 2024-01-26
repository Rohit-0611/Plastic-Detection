from GeoTagExtractor import GeoTagExtractor  

#Make Sure the image has latitude and longitude information in it's metadata... You can check it in properites of the image under details tab.

img_path = "./DJI_0185.jpg"  # Provide the complete image path
geo_tag_extractor = GeoTagExtractor(img_path)
google_maps_link = geo_tag_extractor.get_google_maps_link()
if google_maps_link:
    print(f"Image.jpg URL: {google_maps_link}")
else:
        print("No geotag information found.")

