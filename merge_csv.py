import os
import shutil

# Define the source directory containing the images
source_directory = '/Users/ritvikpatra/Downloads/basilleafdataset/Master-Images'

# Create a destination directory to store the organized folders
destination_directory = '/Users/ritvikpatra/Downloads/basilleafdataset/final'

# Ensure the destination directory exists or create it
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterate through the files in the source directory
for filename in os.listdir(source_directory):
    # Extract the plant name from the filename (e.g., P1, P2, ..., P50)
    plant_name = filename.split('-')[0]

    # Create a folder for each plant in the destination directory
    plant_folder = os.path.join(destination_directory, plant_name)
    os.makedirs(plant_folder, exist_ok=True)

    # Copy the file to the corresponding plant folder
    source_path = os.path.join(source_directory, filename)
    destination_path = os.path.join(plant_folder, filename)
    shutil.copy(source_path, destination_path)

print("Images organized into plant-specific folders.")
