import random
import numpy as np

class Classe(object):

    MAX_PERSONS_BY_GROUP = 4

    def __init__(self, effectif):
        self.effectif = effectif
        self.groups = self.createGroups()

    def createGroups(self):
        groups_count = self.effectif // self.MAX_PERSONS_BY_GROUP + 1
        idsList = [i for i in range(self.effectif+1)]
        random.shuffle(idsList)
        groups = np.array_split(idsList, groups_count)
        return groups

classe = Classe(24)

for id_table, group in enumerate(classe.groups):
    print(
        "La table {} sera composée du groupe: {}".format(id_table, ",".join(map(str, group))) 
    )
