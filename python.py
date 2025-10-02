
nums=[n for n in range(987)]
print(nums)
print(sum(nums))

def count():
    return sum([num <0 for num in nums])

print(count())