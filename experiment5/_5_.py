import os
if __name__ == "__main__":
    target_path1 = "./file1.txt"
    target_path2 = "./file2.txt"
    if os.path.exists(target_path1)==False:
        print("file1.txt doesn't exists!\n")
    else:
        with open("meng1.txt", "w", encoding="utf-8") as target:
            try:
                file_1 = open(target_path1, 'r')
            except FileNotFoundError:
                target.write(file_1)
                file_1.close()
    if os.path.exists(target_path2)==False:
        print("file2.txt doesn't exists!\n")
    else:
        with open("meng1.txt", "a", encoding="utf-8") as target:
            file_2 = open(target_path2, 'r')
            target.write(file_2.read())
            file_2.close()
