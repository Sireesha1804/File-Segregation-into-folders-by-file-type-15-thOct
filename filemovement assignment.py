import os
import shutil

def segregate_files(source_directory):
    # Define file categories and their extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png"],
        "Documents": [".pdf", ".txt"],
        "Videos": [".mp4", ".mov"]
    }

    # Create folders for each category if they don't exist
    for folder in categories:
        os.makedirs(os.path.join(source_directory, folder), exist_ok=True)

    # Loop through each file in the source directory
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        # Only process files
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()  # Get file extension

            # Move file to the appropriate folder
            moved = False
            for folder, extensions in categories.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(source_directory, folder, filename))
                    print(f"Moved '{filename}' to '{folder}' folder.")
                    moved = True
                    break

            # If the file extension doesn't match, move it to "Others"
            if not moved:
                other_folder = os.path.join(source_directory, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved '{filename}' to 'Others' folder.")

# Specify the directory containing the files to organize
source_directory = "C:/Users/shire/Downloads"  # actual directory path

# Run the function
segregate_files(source_directory)
