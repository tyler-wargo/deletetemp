###############################################
# Python code to move temporary files to recycle bin
###############################################

import os
import shutil

def move_temp_files_to_recycle_bin():
    # Set the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Specify the temporary file paths
    temp_paths = ["C:\\Windows\\Temp", "C:\\Users\\tyler\\AppData\\Local\\Temp"]

    # Specify the common files to exclude
    common_files = ["officeclicktorun.exe_streamserver(20230621144858CD0)",
                    "LAPTOP-7TKSH6TH-20230621-1449"]

    # Iterate through each temporary path
    for temp_path in temp_paths:
        # Walk through each directory and file within the temporary path
        for root, dirs, files in os.walk(temp_path):
            # Iterate through each file
            for file in files:
                file_path = os.path.join(root, file)

                # Check if the file path is in the common files list
                if file_path not in common_files:
                    try:
                        # Move the file to the recycle bin on the desktop
                        shutil.move(file_path, os.path.join(desktop_path, os.path.basename(file_path)))
                    except PermissionError:
                        # Handle permission errors
                        print(f"Permission denied: {file_path}")
                    except FileNotFoundError:
                        # Handle file not found errors
                        print(f"File not found: {file_path}")
                    except Exception as e:
                        # Handle other exceptions
                        print(f"Error moving file {file_path}: {str(e)}")

# Call the function to move temporary files to the recycle bin
move_temp_files_to_recycle_bin()
