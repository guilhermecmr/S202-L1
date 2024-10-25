from database.database import Database
from teacher_crud.teacher_crud import TeacherCRUD

db = Database("bolt://98.80.167.84", "neo4j", "occurrences-incentive-kites")

# Questão 3
# a)
teacher_crud = TeacherCRUD(db)

# b)
teacher_create = teacher_crud.create("Chris Lima", "1956", "189.052.396-66")

# c)
teacher_read = teacher_crud.read("Chris Lima")
print("Retorno de Chris Lima:")
print(teacher_read)

# d)
teacher_update = teacher_crud.update("Chris Lima", "162.052.777-77")

# e)
class TeacherCLI:
    def __init__(self, teacher_crud: TeacherCRUD):
        self.teacher_crud = teacher_crud
    
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Criar Professor")
            print("2. Ler Professor")
            print("3. Atualizar Professor")
            print("4. Remover Professor")
            print("5. Sair")
            
            option = input("Opcao: ")
            
            if option == "1":
                self.create_teacher()
            elif option == "2":
                print(self.read_teacher())
            elif option == "3":
                self.update_teacher() 
            elif option == "4":
                self.delete_teacher()
            elif option == "5":
                print("\nEncerrando o programa...")
                break
            else:
                print("Opcao invalida!")

    def create_teacher(self):
        name = input("\nNome: ")
        ano_nasc = input("Ano de nascimento: ")
        cpf = input("CPF: ")
        teacher = self.teacher_crud.create(name, ano_nasc, cpf)
        print("Professor criado com sucesso!")
        return teacher

    def read_teacher(self):
        name = input("\nNome do professor: ")
        print(f"Retorno de {name}:")
        teacher = self.teacher_crud.read(name)
        return teacher
    
    def update_teacher(self):
        name = input("\nNome do professor: ")
        newCpf = input("CPF: ")
        teacher = self.teacher_crud.update(name, newCpf)
        print("Professor atualizado com sucesso!")
        return teacher
    
    def delete_teacher(self):
        name = input("\nNome do professor: ")
        teacher = self.teacher_crud.delete(name)
        print("Professor removido com sucesso!")
        return teacher
    
teacher_cli = TeacherCLI(teacher_crud)

if __name__ == "__main__":
    teacher_cli.menu()