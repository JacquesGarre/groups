from classes.classroom import Classroom
                
def main():
    classroom = Classroom(csv = "liste_apprenants.csv", max_persons_by_group = 4)
    classroom.printTables()

if __name__=='__main__':
    main() 