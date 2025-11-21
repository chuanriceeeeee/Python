# .strip()
# readline
# with open("name",mode="",encoding="") as xx:

if __name__ == "__main__":

    name = input("Input your name:\n")
    student_id = input("Input you ID:\n")

    with open("student_info.txt", "w", encoding="utf-8") as f:
        f.write(f"Name:{name}\n")
        f.write(f"Student ID:{student_id}\n")
    with open("student_info.txt", "r", encoding="utf-8") as f:
        line1 = f.readline()
        line2 = f.readline()
    print(f"{line1.strip()}\n{line2.strip()}")
