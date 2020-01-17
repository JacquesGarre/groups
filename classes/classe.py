import random
import numpy as np
import csv
from os.path import dirname, abspath, join
import datetime

class Classe(object):

    def __init__(self, csv, max_persons_by_group):
        self.liste_apprenants = self.__parseCsv(csv)
        self.__max_persons_by_group = max_persons_by_group
        self.__groups = self.__createGroups()

    def __createGroups(self):
        groups_count = len(self.liste_apprenants) // self.__max_persons_by_group + 1
        random.shuffle(self.liste_apprenants)
        groups = np.array_split(self.liste_apprenants, groups_count)
        return groups

    def __parseCsv(self, csv_filename):
        liste_apprenants = []
        file_path = join(
            dirname(dirname(abspath(__file__))),
            csv_filename
        )        
        with open(file_path, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                liste_apprenants.append(row[0] + ' ' + row[1])
        return liste_apprenants

    def printTables(self):
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        print("\nAujourd'hui, {} :\n".format(date))
        for i, group in enumerate(self.__groups):
            persons = ", ".join(map(str, group[:-1])) + " et " + str(group[-1])
            print("La table {} sera composée de : {}".format(i, persons))
        print("\n")
