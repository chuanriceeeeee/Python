#os
# os.path.exists() -- judge whether target_directory exsits
# os.path.join(target_dir,"")

import os
if __name__ == "__main__":
    # if directory doesn't exists
    target_dir = "/home/chuanrice/dev_python"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    source_path = "student_info.txt"
    target_path = os.path.join(target_dir, "student_info_backup.txt")
    with open(source_path,
              "r", encoding="utf-8") as f, open(target_path,
                                                "w",
                                                encoding="utf-8") as output:
        output.write(f.read())
