from Utensil import Utensil

fork = Utensil("fork", "metal")

knife = Utensil("knife", "gold")

spoon = Utensil("spoon", "plastic")


print(fork.type)
print(knife.type)
print(spoon.type)

print()
knife.cut()
spoon.pickup()