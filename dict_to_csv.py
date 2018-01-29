import csv

def write_csv(dicts,filename):
    with open(filename, 'a') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, ['label', 'from', 'subject', 'body', 'attachment'])
        # w.writeheader()
        w.writerow(dicts)
