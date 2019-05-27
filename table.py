from prettytable import PrettyTable

arr = [
    [1, 55, 88],
    [2, 78, 32],
    [3, 22, 1]
]

def main():
    t = PrettyTable(['a', 'b', 'c'])
    for row in arr:
        t.add_row(row)
    print(t)


if __name__ == "__main__":
    main()