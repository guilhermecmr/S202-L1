class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class LivrosCLI(SimpleCLI):
    def __init__(self, livros_model):
        super().__init__()
        self.livros_model = livros_model
        self.add_command("create", self.create_livros)
        self.add_command("read", self.read_livros)
        self.add_command("update", self.update_livros)
        self.add_command("delete", self.delete_livros)

    def create_livros(self):
        id = input("Entre com o id: ")
        titulo = input("Entre com o titulo: ")
        autor = input("Entre com o autor: ")
        ano = int(input("Entre com o ano: "))
        preco = float(input("Entre com o preco: "))
        self.livros_model.create_livro(id, titulo, autor, ano, preco)

    def read_livros(self):
        id = input("Entre com o id: ")
        livro = self.livros_model.read_livro_by_id(id)
        if livro:
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Preco: {livro['preco']}")

    def update_livros(self):
        id = input("Entre com o id: ")
        titulo = input("Entre com o titulo: ")
        autor = input("Entre com o autor: ")
        ano = int(input("Entre com o ano: "))
        preco = float(input("Entre com o preco: "))
        self.livros_model.update_livro(id, titulo, autor, ano, preco)

    def delete_livros(self):
        id = input("Entre com o id: ")
        self.livros_model.delete_livro(id)
        
    def run(self):
        print("Welcome to the livro CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        