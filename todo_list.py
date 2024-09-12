class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        estado = "Completado" if self.completed else "Pendiente"
        return f"{self.description} - {estado}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)


def main():
    pass


if __name__ == "__main__":
    main()
