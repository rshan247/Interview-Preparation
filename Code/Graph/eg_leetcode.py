def removeDuplicates( nums):
        unique = nums[0]
        cur = 0
        print(nums)
        # for i in range(1, len(nums)):
        while nums:
            print("hello")
            print("hi: " )
            if nums[cur] == nums[cur-1]:
                del nums[cur]
                cur += 1
            else:
                unique = nums[cur]
        return len(nums)

# nums = [0,0,2,2,3,3,4]
# my_set = set(nums)
# nums = list(my_set) 
# print(nums)

print(removeDuplicates([1,1,1]))