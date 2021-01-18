shopping_items = ["jajka", "chleb", "pomidor"]
def shopping(items):
    for item in items:
        print(item)
shopping(shopping_items)

shopping_itemss = ["chleb", "jajko", "cukier"]
def shoppingps(items, *, payment = "card", shop = "local"):
      print(items, payment, shop)
shoppingps(1,2 , keyword_only_parameters = 3)