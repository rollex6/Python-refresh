# Selection Sort


def sort(nums):

    for i in range(5):
        mainposition = i
        for j in range(i,6):
            if nums[j] < nums[mainposition]:
                mainposition = j
        
        temp = nums[i]
        nums[i] = nums[mainposition]
        nums[mainposition] = temp

        print(nums) # print nums in order to see all the iterations

nums = [5, 3,8,6,7,2]
sort(nums)
print(nums)
