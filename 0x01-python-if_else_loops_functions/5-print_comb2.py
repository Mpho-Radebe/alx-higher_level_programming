#!/usr/bin/python3
for num in range(0, 100):
    print(f"{num:02}{'' if num == 99 else ', '}", end="")
print()
