import sys

print("Добрый день! \n"
      "Это программа нарисует из твоего сообщения карту мира!")
print("Введи сообщения для создания изображения")
message = input("> ")

if message == "":
    sys.exit()

f = open("map.txt", "r")
world_map = f.read()

for line in world_map.splitlines():
    for i, bit in enumerate(line):
        if bit == " ":
            print(" ", end="")
        else:
            print(message[i % len(message)], end="")
    print()
