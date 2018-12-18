###testing making a dict of functions

import csv

with open('seneca_routes.csv', 'r', encoding='utf-8-sig') as f:     #weird encoding from excel?
    reader = csv.DictReader(f,)
    print("Here is a list of classics and the grade")
    print()
