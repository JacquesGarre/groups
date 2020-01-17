import random
import numpy as np
import csv
import os, sys
import datetime

class Classe(object):

    def __init__(self, csv, max_persons_by_group):
        self.liste_apprenants = self.parseCsv(csv)
        self.max_persons_by_group = max_persons_by_group
        self.groups = self.createGroups()

    def createGroups(self):
        groups_count = len(self.liste_apprenants) // self.max_persons_by_group + 1
        random.shuffle(self.liste_apprenants)
        groups = np.array_split(self.liste_apprenants, groups_count)
        return groups

    def parseCsv(self, csv_filename):
        liste_apprenants = []
        file_path = os.path.join(os.path.dirname(__file__), csv_filename)
        with open(file_path, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in enumerate(csv_reader):
                liste_apprenants.append(row[1][0] + ' ' + row[1][1])
        return liste_apprenants

    def printTables(self):
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        print("\nAujourd'hui, {} :\n".format(date))
        for i, group in enumerate(self.groups):
            print(
                "La table {} sera composée de : {}".format(i, ", ".join(map(str, group)))
            )
        print("\n")

                
classe = Classe(csv = "liste_apprenants.csv", max_persons_by_group = 4)
classe.printTables()


