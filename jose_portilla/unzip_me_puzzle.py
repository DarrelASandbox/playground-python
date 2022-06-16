import os
import re
import shutil

shutil.unpack_archive(
    "./jose_portilla/unzip_me_for_instructions.zip",
    "./jose_portilla/extracted_content_unzip_me",
    "zip",
)

for path, folders, files in os.walk(
    os.getcwd() + "/jose_portilla/extracted_content_unzip_me"
):
    for file in files:
        if file.endswith(".txt"):
            open_file = open(f"{path}/{file}", "r")
            text = open_file.read()
            phone_number = re.findall(r"\d{3}-\d{3}-\d{4}", text)
            if phone_number != []:
                print(f"The phone number is: {phone_number}")
