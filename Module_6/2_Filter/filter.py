# lazily evaluated!
#filter(function, sequence) => function applied to sequence, only gives the ones where function evaluate to true

positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
print(list(positives))

trues = filter(None, [0,1,False,True,[],[1,2,3],'','hello'])
print(list(trues))