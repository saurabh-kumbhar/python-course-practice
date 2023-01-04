#!/usr/bin/env python3

from utils.utility_stuff import ListCharShortner, DictionaryShortner
from machines.vehicle_stuff import car

mydict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}
mydshort = DictionaryShortner(mydict)
mydshort.print_original_items()
mydshort.print_shortened_items()

mylist = "MacBook"
mylshort = ListCharShortner(mylist)
mylshort.print_original_items()
mylshort.print_shortened_items()

# Double Under / Dundur __str__ or __len__
nexon = car('Compact SUV', 'Tata', 'Nexon', 'Dark')
print(nexon)
print(len(nexon), 'meters')