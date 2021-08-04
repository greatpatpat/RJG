'''
Write a program that accepts a list of four non negative integers,
arranges them such that they form a largest possible number.

For example [50,2,1,9), the largest formed number is 95021

Be carefull if [10,1] the answer is not 101 but 110
'''


from typing import List
class ANS:

    def largestNumber(self, nums: List[int]) -> str:
    
        nums = list(map(str, nums))
        if len(nums) < 2:
            return "".join(nums)
        
        def compare(x, y):
            return (int(nums[x]+nums[y])) > (int(nums[y]+nums[x]))
        
        for x in range(len(nums) - 1):
            y = x + 1
            while x < len(nums) and y < (len(nums)):
                if not compare(x,y):
                    nums[y], nums[x] = nums[x], nums[y]
                y+=1

        return "".join(nums) 

nums = list(map(int, input("Enter 4 non negative integer: ").split()))
a = ANS()
l = a.largestNumber(nums)
print(l)