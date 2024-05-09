def main(mylist, search_value):
    lowerBound = 0 
    upperBound = len(mylist) - 1

    if not mylist:
        print("Empty list")
    else:
        bsa(mylist, search_value, lowerBound, upperBound)



def bsa(mylist, search_value, lowerBound, upperBound):
    midValue = (upperBound + lowerBound) // 2
    if lowerBound >= upperBound:
        print("Value not found")
    elif mylist[midValue] == search_value:
        print("Found")
    elif search_value > mylist[midValue]:
        lowerBound = midValue + 1
        bsa(mylist, search_value, lowerBound, upperBound)
    elif search_value < mylist[midValue]:
        upperBound = midValue - 1
        bsa(mylist, search_value, lowerBound, upperBound)


if __name__ == "__main__":
    mylist = list(range(1,5001))   
    search_value = 19
    main(mylist, search_value)