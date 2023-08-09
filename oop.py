class Apple:
    pass

class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())
golden = Apple()
golden.color = "yellow"
golden.flavor = "soft"
print(golden.color)

class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"
violet = Flower()
violet.color = "blue"
this_pun_is_for_you = "Sugar is sweet, and so are you."

print("Roses are {},".format(rose.color))
print("Violets are {},".format(violet.color))
print(this_pun_is_for_you) 