def main():
    list = [1,2,4,5,6,7,8,9]
    value = 4
    low = 0
    high = (len(list) - 1)
    bsa(list, value, low, high) 

def bsa(list, value, low, high):
    list.sort()
    mid = low + (high - low)//2
    if not list:
        print("Empty list")
    elif low == high:
        print("Value Not ehh found")
    elif list[mid] == value:
        print("value found", list[mid], "Index", mid)
    elif list[mid] < value:
        low = mid + 1
        bsa(list, value, low, high)
    elif list[mid] > value:
        high = mid + 1
        bsa(list, value, low, high)
    else:
        print("Value not found")

if __name__ == "__main__":
    main()