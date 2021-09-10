zoo = [
	["monkey", "tiger", "elephant"],
	["frog", "snake"],
	["owl", "pigeon"],
	["hamster", "mouse", "hedgehog"]
]
for row in zoo:
    for column in row:
        count_a=column.find("a")
        if count_a != -1:
            print(column)