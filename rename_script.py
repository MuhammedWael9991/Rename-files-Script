import os
import shutil

def rename_and_copy_files(source_folder, dest_folder, prefix="", postfix=""):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
         
            name, ext = os.path.splitext(filename)
            new_name = prefix + name.lower().replace(" ", "_") + postfix + ext

            dest_path = os.path.join(dest_folder, new_name)

            shutil.copy2(source_path, dest_path)
            print(f"Copied: {filename} -> {new_name}")


source = input("file path: ").strip()
destination = os.path.join(source, "new_assets")


prefix = ""
postfix = ""

print("add prefix (y/n)")
if input().lower() == "y":
    prefix = input("prefix: ").strip()

print("add postfix (y/n)")
if input().lower() == "y":
    postfix = input("postfix: ").strip()

rename_and_copy_files(source, destination, prefix, postfix)

