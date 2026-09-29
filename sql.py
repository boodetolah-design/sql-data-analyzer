import csv
counts = {}
with open("fav.csv","r") as file:
    reader =csv.DictReader(file)
    for row in  reader:
        lang = row['problem'].lower().strip()

        if lang not in counts:
            counts[lang] = 0

        counts[lang] += 1



for i in sorted(counts,key=lambda lang:counts[lang] , reverse= False):
    print(f"{i} : {counts[i]}")



