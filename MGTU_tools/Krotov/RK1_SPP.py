class Criteria:
    """
    Информация о критерии. Не содержит значений.
    """
    def __init__(self, rate: int = None, is_down: bool = False, name: str = "Unknown"):
        self.is_down = is_down
        self.name = name
        self.rate = rate

    def read(self):
        print("Запиши через пробел: ВАЖНОСТЬ, НАЗВАНИЕ, Чем_меньше_тем_лучше(0 или 1)")
        arr = [self.rate, self.name, self.is_down]
        data = input().split()
        if len(data) > 1:
            arr[0] = int(data[0])
        elif len(data) > 2:
            arr[1] = data[1]
        elif len(data) > 3:
            arr[2] = bool(data[2])
        return self

    def __str__(self):
        text = f"Кр. {self.name} чем {'<' if self.is_down else '>'} тем лучше." \
               f"{f'Важ. {self.rate}' if self.rate else ''}"
        return text


class CriteriaMatrix:
    def __init__(self, n_criteria: int = None, n_vars: int = None):
        self.n_criteria = n_criteria
        self.n_vars = n_vars
        self.data = []
        self.criteria = []

    def read(self):
        try:
            n_criteria, n_vars = map(int, input("Кол-во вариантов и критериев: ").split())
        except TypeError:
            print("Неверный ввод")
            return
        self.n_criteria = n_criteria
        self.n_vars = n_vars

        self.criteria.clear()
        for i in n_criteria:
            self.criteria.append(Criteria().read())

        for i in range(n_vars):
            print(f"Ввод варианта В{i+1}")
            var_vals = []
            for j in range(len(self.criteria)):
                x = input(f"{self.criteria[j].name} - ")
                var_vals.append(x)

        print("Ввод завершен.")
        print(self)

    def __str__(self):
        text = "Матрица:\n"
        for c in self.criteria:
            text += str(c) + "\n"
        for i, d in enumerate(self.data):
            text += f"В{i+1}" + str(*d) + "\n"
        return text





class Solution:
    def __init__(self, matrix: CriteriaMatrix):
        self.mat = matrix

    def