from functools import reduce
import operator

print(reduce(operator.add, [1,2,3,4,5])) 


# what happens in reality:
numbers = [1,2,3,4,5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator, item)
print(accumulator)


reduce(operator.add, [1]) # reduce is never called


print(reduce(operator.add, numbers, 6)) # starting from initial value 6