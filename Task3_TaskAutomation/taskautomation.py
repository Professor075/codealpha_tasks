import os
import shutil

# Set the directory where the files are located
source_dir = "/mnt/c/Users/Admin/Downloads"  # Change this to the directory you want to organize

# Define categories based on file extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".sh"]
}

# Function to organize files
def organize_files():
    # Loop through files in the directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            # Find the category
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    category_path = os.path.join(source_dir, category)

                    # Create the category folder if it does not exist
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)

                    # Move the file into the respective folder
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved {filename} → {category}")

    print("✅ File organization complete!")

# Run the function
if __name__ == "__main__":
    organize_files()
