with open('cook_book.py') as f:
    data = f.read()
    print(type(f))

def is_closed(f):
    if f.closed:
        print("File is closed")
    else:
        print("File is open")

    is_closed(f)
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in data:
            for ingredient in data[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity

    return shop_list

result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result)
