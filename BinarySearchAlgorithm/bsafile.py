def main():
    mylist = []
    for i in range(1, 5001):
        mylist.append(i)    
    value = 800
    low = 0
    high = (len(mylist) - 1)
    bsa(mylist, value, low, high) 

def bsa(mylist, value, low, high):
    mylist.sort()
    mid = low + (high - low)//2
    if not mylist:
        print("Empty mylist")
    elif low == high:
        print("Value Not ehh found")
    elif mylist[mid] == value:
        print("value found", mylist[mid], "Index", mid)
    elif mylist[mid] < value:
        low = mid + 1
        bsa(mylist, value, low, high)
    elif mylist[mid] > value:
        high = mid + 1
        bsa(mylist, value, low, high)
    else:
        print("Value not found")

if __name__ == "__main__":
    main()