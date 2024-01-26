from PIL import Image
from PIL.ExifTags import TAGS

class GeoTagExtractor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.geotag_label = self._get_geotag_label()

    def _convert_to_degrees(self, value):
        d, m, s = value
        return d + (m / 60.0) + (s / 3600.0)

    def _get_geotag_label(self):
        image = Image.open(self.image_path)

        if hasattr(image, '_getexif'):
            exif_data = image._getexif()

            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)

                if tag_name == 'GPSInfo':
                    lat = self._convert_to_degrees(value[2])
                    lon = self._convert_to_degrees(value[4])
                    lat_ref = value[1]
                    lon_ref = value[3]

                    if lat_ref == 'S':
                        lat = -lat
                    if lon_ref == 'W':
                        lon = -lon

                    return f"Latitude: {lat}, Longitude: {lon}"

        return None

    def split_geotag_label(self):
        if self.geotag_label:
            latitude_start_index = self.geotag_label.find(":") + 1
            latitude_end_index = self.geotag_label.find(",") 
            latitude = self.geotag_label[latitude_start_index:latitude_end_index].strip()

            longitude_start_index = self.geotag_label.find("Longitude:") + len("Longitude:") + 1
            longitude = self.geotag_label[longitude_start_index:].strip()

            return latitude, longitude
        else:
            return None

    def get_google_maps_link(self):
        if self.geotag_label:
            latitude, longitude = self.split_geotag_label()
            link = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
            return link
        else:
            return None


