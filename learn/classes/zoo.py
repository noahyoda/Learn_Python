from animal import animal
from animal import cage

monkey = animal("omnivore", "gibbon", False)

print(monkey.name)
print(monkey.breath_air())

monkey_cage = cage(monkey, 3)

print(monkey_cage.capacity)
