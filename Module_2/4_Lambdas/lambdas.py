scientists = ['Marie Curie', 'Albert Einstein', 'Isaac Newton']
print(sorted(scientists, key = lambda name: name.split()[-1]))

last_name = lambda name: name.split()[-1]
print(last_name('Nikola Tesla'))