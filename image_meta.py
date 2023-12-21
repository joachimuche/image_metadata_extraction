from PIL import Image
import os
from datetime import datetime
from PIL.ExifTags import TAGS

def extract_info(path):
    with Image.open(path) as img:
        metadata = {
            "format": img.format,
            "mode" : img.mode,
            "size":img.size,
            "file_size": os.path.getsize(path),
            "creation_date": os.path.getctime(path),
            "mod_date": os.path.getmtime(path),
            "more_info": img.info    
            }
        
        return metadata

#extract long and Lat and Device
def extract_location_device_info(path):
    with Image.open(path) as img:
        data = img.getexif()
        if data is not None:
           
            if 0x8825 in data:
                print(data)
                gps_info = data[0x8825]
                lat = gps_info[2][0] / gps_info[2][1]
                long = gps_info[4][0] / gps_info[4][1]
                print(f" GPS: Latitude{lat}, Longitude{long}")

            if 0x0110 in data:
                camera_info = data[0x0110]
                print(f"Camera Model:{camera_info}")

            if 271 in data:
                cam_name = data[271]
                print(f"cam name is {cam_name}")

            if 0x0112 in data:
                orien = data[0x0112]
                if orien == 1:
                    print(f" the orientation is {orien} - Horizontal")

                #insert other orientations here

                ''' def switch(orien):
                    if orien == 1:
                        return "Horizonal"
                    elif orien == 2:
                        return "Mirror horizontal Rotate 180."
                    elif orien == 3:
                        return "Rotate 180"
                    elif orien == 4:
                        return "You can become a Blockchain developer."

                '''
                
            
            if 0x8298 in data:
                copyright = data[0x8298]
                print(f"cpyright - {copyright}")

            if 0x000b in data:
                sw = data[0x000b]
                print(f"cpyright - {sw}")

            if 0x0132 in data:
                DateCreated = data[0x0132]
                print(f"date created - {DateCreated}")

#convert UNIX timeformat to Datetime
def convert_time(data):
    date_time = datetime.fromtimestamp(data)
    new_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
    
    return new_date


if __name__ =="__main__":
    path = "/path/to/your/image_file"
    #e.g - "/Users/knight/Downloads/All_png/sky.jpeg"

    #calling the ei function
    metadata = extract_info(path)
    print("image metadata:", metadata)

    #checking creation date
    creation_date = convert_time(os.path.getctime(path))
    modified_date= convert_time(os.path.getmtime(path))
    
    print("creation_date:", creation_date)
    print("modificate_date:", modified_date)
    extract_location_device_info(path)

