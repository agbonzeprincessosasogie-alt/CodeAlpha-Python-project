import os
import shutil

source = "source_folder"
destination = "destination_folder"
moved = 0
for file in os.listdir(source):

    if file.lower().endswith(".jpg"):

        shutil.move(
            os.path.join(source, file),
            os.path.join(destination, file)
        )
        moved += 1
print(f"{moved} Image(s) moved successfully")