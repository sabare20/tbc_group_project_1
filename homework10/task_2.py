def max_num_detector(*nums):
    max_num=nums[0]
    lenght_nums=len(nums)
    for i in range(1,lenght_nums):
        if nums[i]>max_num:
            max_num=nums[i]
    return max_num
print(max_num_detector(-9,-5,-5,-2,-5,-7,-8,-4,-7,-44,-55,-4,-1))  
        
            
    
        
    



    