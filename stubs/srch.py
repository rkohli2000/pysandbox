
# Olog(n) time | O (log(n) space
# Input: array, target is value to find, left Idx, Right Idx


def binarySearchHelper(array, target, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1
    middle = (leftIdx + rightIdx) // 2
    potentialMatch = array[middle]
    if target == array[middle]:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, leftIdx, middle -1)
    else:
        return binarySearchHelper(array, target, middle + 1, rightIdx)

#def binarySearchHelper2(array, target, leftIdx, rightIdx):
    # while leftIdx <= rightIdx:
    #     middle = (leftIdx + rightIdx) // 2
    #     potentialMatch = array[middle]
    #     if target == potentialMatch:
    #         return middle
    #     elif target < potentialMatch:
    #         rightIdx = middle - 1
    #     else:
    #         leftIdx = middle + 1
    #
    # return -1


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

#def binarySearch2(array, target):
#    return binarySearchHelper2(array, target, 0, len(array) - 1)

if __name__ == '__main__':
    array = [1, 2, 5, 24, 53, 99, 101, 201]
    tgt = 101

    if (binarySearch(array, tgt) == -1):
        print('%d is not found' % tgt)
    else:
        print ('%d is found' % tgt)

    # if (binarySearch2(array, tgt) == -1):
    #     print('%d is not found' % tgt)
    # else:
    #     print ('%d is found' % tgt)