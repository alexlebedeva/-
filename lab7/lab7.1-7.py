class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"сотрудник: {self.name} {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self,name, id)
        self.department = department

    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Отдел: {self.department}"

    def manage_project(self):
        return f"проэктом руководит: {self.name},из департамента: {self.department} "

class Technician(Employee):
    def __init__(self, name, id, specialization):
        self.specialization = specialization
        Employee.__init__(self, name, id)

    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Специализация: {self.specialization}"

    def perform_maintainence(self):
        return f"техник:{self.name}, {self.specialization}, выполняет поддержку"

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Отдел: {self.department},Специализация: {self.specialization}"


    def add_employee(self, employee):
            self.team.append(employee)
            return f"{employee.name} добавлен(а) в команду {self.name}"


    def get_team_info(self):
        if not self.team:
            return "Нет команды"
        text = f"Команда из {len(self.team)} человек:\n"
        number = 1
        for person in self.team:
            text += f"{number}. {person.get_info()}\n"
            number += 1
        return text

oira = Technician("Роман Ойра-Ойра","НИИ-201","Материализация предметов")
kristall = Employee("Кристалл Бенедиктовна", "НИИ-002")
yanus = Manager("Янус Полуэктович Невструев","НИИ-ДИР","Дирекция НИИЧАВО")
azazello = TechManager("Вивиан Азазелло","НИИ-666", "Лаборатория нестандартных решений","Прикладная чертовщина и управление хаосом")


print(yanus.get_info())
print(kristall.get_info())
print(azazello.get_info())
print(oira.get_info())

print(azazello.add_employee(yanus))
print(azazello.add_employee(oira))

print(azazello.get_team_info())