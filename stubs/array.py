""" product sum
Function that takes in a special array and returns its product sum.
A special array is a non empty  that contains either integers or other special arrays.
The product sum of a special array is the sum of its elements, where special arrays inside
it should be summed up themselves and then multiplied by their level of depth.
Input: [5,2,[7,-1],3,[6,[-13,8],4]]
Output: 12 (5+2+2*(7-1) + 3 + 2*(6 + 3(-13 + 8) + 4)
"""
def productSum(inArr, levelMult = 1):
    sum = 0
    for i in inArr:
        if type(i) is list:
            sum += productSum(i, levelMult + 1)
        else:
            sum += i
    return sum * levelMult

# reverse the words in a sentence
def reverseWords(instr):
    inlist = instr.split(" ")
    #print("Debug: instr=%s" % instr)
    rev = inlist[::-1]
    revstr = ' '.join(rev)
    #print('Debug: %s' % (revstr))
    return revstr

def squaredInts(a_list):
    squared_ints = [e ** 2 for e in a_list if type(e) == int]
    return squared_ints


def kadanesAlgorithm(arr):
    maxEndingHere = arr[0]
    maxSoFar = arr[0]
    for i in range(1, len(arr)):
        num = arr[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar



if __name__ == "__main__":
    print('test 1')
    inp = [5,2,[7,-1],3,[6,[-13,8],4]]
    s = productSum(inp)
    print ("inp %s product sum is %d" % (str(inp), s))

    print('\ntest 2')
    instr = "This is a test string"
    rev = reverseWords(instr)
    print ("input string = %s \nReverse = %s" % (instr, rev))

    print ('\ntest 3')
    a_lis = [1, '4', 9, 'a', 0, 4]
    print(a_lis)
    res = squaredInts(a_lis)
    print('squares=', res)

    print ('\ntest 4')
    inp = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]  # ans 19
    k = kadanesAlgorithm(inp)
    print('kadanes', k)
