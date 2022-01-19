import csv


def add(url,filename):
    file = open("./assets/audio.csv", "w")

    writer = csv.writer(file)
    writer.writerow([url, filename])
    file.close()

def getdict():
    with open('./assets/audio.csv') as f:
        return dict(filter(None, csv.reader(f)))