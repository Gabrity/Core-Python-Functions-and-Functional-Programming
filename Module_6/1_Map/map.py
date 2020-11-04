# lazily evaluated!

sizes = ['small', 'medium', 'large']
colors = ['lavander', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']
def combine(size, color, animal):
    return '{} {} {}'.format(size, color, animal)

print(list(map(combine, sizes, colors, animals)))