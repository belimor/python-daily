#!/usr/bin/python3

import os
import tarfile
import time
from datetime import datetime

def archive_files_individually(folder_path,days_old):
    # Ensure the folder exist
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return

    current_time = time.time()
    cutoff_time = current_time - (days_old * 86400) # 7 days in seconds

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
        
            # Get creation time of the file
            file_creation_time = os.path.getctime(file_path)

            if file_creation_time < cutoff_time:
                # Fromat the archive name as [date_of_the_fiel]_[filename].tar
                file_date = datetime.fromtimestamp(file_creation_time).strftime("%Y-%m-%d")
                archive_name = f"{file_date}_{file}.tar"
                archive_path = os.path.join(folder_path, archive_name)

                #Archive the file using tarfile
                with tarfile.open(archive_path, "w") as tar:
                    print(f"Archiving: {file_path} -> {archive_path}")
                    tar.add(file_path, arcname=file)

            # Optionally remove the original file after archiving
            #os.remove(file_path)
    print("Archiving complete")

archive_files_individually("./", 7)

