def display_list(p, foods):
    print(p)
    for food in foods:
        print(food)

foods = ['pizza', 'salad', 'hamburger', 'steak', 'apple', 'orange']

display_list("foods in original order:", foods)

foods_sorted = sorted(foods)
display_list("foods in ascending alphabetical order:", foods_sorted)

foods_sorted.reverse()
display_list("foods in descending alphabetical order:", foods_sorted)

foods_sorted2 = sorted(foods)
display_list("foods2 in ascending alphabetical order:", foods_sorted2)

display_list("foods still in descending alphabetical order:", foods_sorted)

foods_sorted.reverse()
display_list("foods in ascending alphabetical order:", foods_sorted)

foods.append('carrots')
foods.append('milk')
display_list("sorted foods with carrots and milk appended to end:", foods)

foods_sorted_final = sorted(foods)
display_list("foods in ascending alphabetical order:", foods_sorted_final)

pizza_index = foods_sorted_final.index('pizza')
print('Pizza is at', pizza_index)

foods_sorted_final.insert(pizza_index, 'fries')
pizza_index = foods_sorted_final.index('pizza')
print('Pizza is now at', pizza_index)
