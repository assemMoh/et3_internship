import os
import datetime
import shutil
import pandas as pd

def extract_images(directory):
    extensions = ['.jpg', '.jpeg', '.png', '.gif']

    all_images = [["Image", "Size", "Last modified date"]]
    os.mkdir(new_directory)
    #traverse the whole directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in extensions:
                img_path = os.path.join(root, file)
                #os.stat contains properties of image
                img = os.stat(img_path)
                last_modified = datetime.datetime.fromtimestamp(img.st_mtime)
                last_modified_formatted = last_modified.strftime("%a, %d %b %Y %H:%M:%S")
                #st_size gives size in bytes, dividing by 1024 to get size in Kilo bytes
                size = round((img.st_size / (1024)), 2)
                #splitting by '-' and removes all suffixes
                file = file.split('-')[-1]
                all_images.append([file, str(size) + " KB", last_modified_formatted])            
                #copy images to new directory
                shutil.copy(img_path, new_directory)                    
    return all_images

directory_path = 'problem1/'
new_directory = 'images_dataset'
output_csv = 'output_csv'
output_excel = 'images_datasets.xlsx'
images_info = extract_images(directory_path)

#converting list of images info into dataframe
df = pd.DataFrame(images_info)
df.to_csv(output_csv, index=False)
df.to_excel(output_excel, index=None, header=True)