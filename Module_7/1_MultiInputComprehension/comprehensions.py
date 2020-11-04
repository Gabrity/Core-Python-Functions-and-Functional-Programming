# single version
s = [i*2 for i in range(10)]

#multi
m = [(x,y) for x in range(5) for y in range(5)]
print(m)

f = [x/ (x-y) for x in range(100) if x > 50 for y in range(100) if x - y != 0]
print(f)

e = [(x, y) for x in range(5) for y in range(x)]
print(e)