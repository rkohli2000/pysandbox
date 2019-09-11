



class Solution(object):
    # O(n2) | O(1)
    """ Two sum """
    """
     Two sum:
     Find all doubles in an input array that sum up to target
     and return a two dimensional array of these pairs. In
     ascending order. 

     Given array nums = [-1, 0, 1, 2, -1, -4],

     A solution set is:
     [
       [-1, 1],
     ]
     """
    def twoSum(self, array, targetSum):
        for i in range(len(array) - 1):
            firstNum = array[i]
            for j in range(i + 1, len(array)):
                secondNum = array[j]
                if firstNum + secondNum == targetSum:
                    return sorted([firstNum, secondNum])
        return []


    """
    # 1) Three sum:
    Find all triplets in an input array that sum up to target
    and return a two dimensional array of these triplets. In
    ascending order. 

    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    """
    # O(n2) | O(n)
    def threeSum(self, array, targetSum):
        array.sort()
        triplets = []
        for i in range(len(array) - 2):
            left = i + 1
            right = len(array) - 1
            while left < right:
                currentSum = array[i] + array[left] + array[right]
                if currentSum == targetSum:
                    # prevent duplicates
                    if [array[i], array[left], array[right]] not in triplets:
                        triplets.append([array[i], array[left], array[right]])
                    left += 1
                    right -= 1
                elif currentSum < targetSum:
                    left += 1
                elif currentSum > targetSum:
                    right -= 1
        return triplets


if __name__ == "__main__":

    inp = [-1, 0, 1, 2, -1, -4]
    s = Solution()

    print("input %s, tgt %s, twosum=%s" % (inp, 0, s.twoSum(inp, 0)))
    print("input %s, tgt %s, threesum=%s" % (inp, 0, s.threeSum(inp, 0)))