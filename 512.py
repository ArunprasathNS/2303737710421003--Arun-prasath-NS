s = int(input("Enter size: "))
el = list(map(int, input("Enter elements: ").split()))
sk = int(input("Enter search key: "))


if sk in el:
    print(f"{sk} found at position {el.index(sk) + 1}")
else:
    print(f"{sk} not found")
