# Binary search
def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = None
    while first <= last and not found:
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = f"The item is found: {item}"
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


print(binary_search([11, 22, 30, 33, 40, 44, 55, 60, 66, 77, 80, 88, 99], 303))
