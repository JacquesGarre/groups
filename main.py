from classes.classe import Classe
                
def main():
    classe = Classe(csv = "liste_apprenants.csv", max_persons_by_group = 4)
    classe.printTables()

if __name__=='__main__':
    main() 