from cat import Cat

cat1 = Cat("БАРОН", "МАЛЬЧИК", 2)
cat2 = Cat("СЭМ", "МАЛЬЧИК", 2)

cats_list = [cat1, cat2]

for cats in cats_list:
    print(cats.get_cats())
