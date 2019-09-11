import statistics


def getMedian(data):
    return statistics.median(data)



if __name__ == "__main__":
    # get median
    lst = [5, 1, 3, 6, 10, 20, 20]  # 6 is median, 20 is mode
    lst.sort()
    print(lst)
    t = getMedian(lst)
    print(t)

    print (statistics.mode(lst))
    
    print (statistics.mean(lst))