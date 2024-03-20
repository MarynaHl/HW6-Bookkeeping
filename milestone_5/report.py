import csv
import sys

def report(database_file, month, verbose=False):
    with open(database_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row['Birthday'].split('-')[1] == month:
                if verbose:
                    print("{} - {} - {} - {}".format(row['Name'], row['Hiring Date'], row['Department'], row['Birthday']))
                else:
                    print("{} - {}".format(row['Name'], row['Birthday']))

if __name__ == '__main__':
    database_file = sys.argv[1]
    month = sys.argv[2]
    verbose = False
    if len(sys.argv) > 3 and sys.argv[3] == '-v':
        verbose = True
    report(database_file, month, verbose)
