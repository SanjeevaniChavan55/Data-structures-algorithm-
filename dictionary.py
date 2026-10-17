
def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2
    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


products = [
    ("Laptop", 55000),
    ("Mouse", 500),
    ("Keyboard", 1200),
    ("Mobile", 20000),
    ("Headphones", 1500)
]

sorted_products = merge_sort(products)

print("Products sorted by price:")
for name, price in sorted_products:
    print(name, "- ₹", price)
