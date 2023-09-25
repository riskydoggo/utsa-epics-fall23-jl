import os

folder_path = '\Users\jjlof\OneDrive\Desktop\python'  # Change this to the path of your folder
start_number = 1  # Change this to the starting number for renaming

# List all files in the folder
files = os.listdir(folder_path)

# Sort the files to ensure a consistent order
files.sort()

# Initialize a counter for sequential renaming
count = start_number

# Iterate through the files and rename them sequentially
for filename in files:
    old_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a subfolder)
    if os.path.isfile(old_path):
        # Split the file name and extension
        name, ext = os.path.splitext(filename)
        
        # Create the new file name with sequential number
        new_name = f'file{count}{ext}'
        
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} to {new_name}')
        
        # Increment the counter
        count += 1
