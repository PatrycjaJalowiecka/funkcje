fun_items = ["balony", "czipsy", "ciastka"]
def fun_default(items, muzyka = "radio", godzina = "18.00"):
    ##print(items, muzyka, godzina)
    pass
fun_default(fun_items, muzyka = "tv")

def fun_positional(items, /, muzyka = "radio", godzina = "18.00"):
    ##print(items, muzyka, godzina)
    pass
fun_positional(fun_items, muzyka = "tv", godzina = "17.30")

def fun_keyword(items, *, muzyka = "radio", godzina = "18.00"):
    ##print(items, muzyka, godzina)
    pass
fun_keyword(fun_items, muzyka = "tv", godzina = "17.45")
