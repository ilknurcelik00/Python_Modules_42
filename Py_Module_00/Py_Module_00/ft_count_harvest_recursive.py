
def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    def helper(day):
        if day > x:
            return
        print("Day", day)
        helper(day + 1)
    helper(1)
    print("Harvest time!")
