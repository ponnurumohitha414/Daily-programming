s = input()

for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in s:
        print("Not Pangram")
        break
else:
    print("Pangram")
