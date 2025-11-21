# for _ in range(0, 1):
#   print(_)
# output1
# overwrite: "w" "w+"
# add: "r+" read before write, "a" pure add
# x: write only if file dosen't exist


def get_prime_add(m: int, n: int) -> int:
    # judge prime number and add
    # include 2
    summary = sum([
        x for x in range(m + 1, n)
        if len([_ for _ in range(2, x) if x % _ == 0]) == 0 or x == 2
    ])
    return summary


if __name__ == "__main__":
    while True:
        try:
            m = int(input("Input m:\n"))
        except ValueError:
            print("Please enter an integer!")
            continue
        break
    while True:
        try:
            n = int(input("Input n:\n"))
        except ValueError:
            print("Please enter an integer!")
            continue
        break
    if m > n:
        temp = m
        m = n
        n = temp
    summary = get_prime_add(m, n)
    print(summary)

    with open("./file.txt", mode="w", encoding="utf-8") as output:
        output.write(f"{m} {n} {summary}")
    print("Successfully create!")
    with open("./file.txt", mode="r", encoding="utf-8") as output:
        line = output.readline()
        print(line)
