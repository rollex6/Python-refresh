# Bubble Sorting


def sort(nums):
    for i in range(len(nums)-1,0,-1): # -1 is the end of the list when counting with index numbers
        for j in range (i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
nums = [5, 3,8,6,7,2]
sort(nums)
print(nums)