from typing import List


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
        data = input().split()
        if len(data) > 1:
            self.rate = int(data[0])
        elif len(data) > 2:
            self.name = data[1]
        elif len(data) > 3:
            self.is_down = bool(data[2])
        return self

    def __str__(self):
        text = f"Кр. '{self.name}' чем {'<' if self.is_down else '>'} тем лучше. " \
               f"{f'Важность: {self.rate}' if self.rate else ''}"
        return text


class CriteriaMatrix:
    def __init__(self, n_criteria: int = None, n_vars: int = None):
        self.n_criteria = n_criteria
        self.n_vars = n_vars
        self.data = []
        self.criteria: List[Criteria] = []

    def read(self, new_criteria=True):
        if new_criteria:
            try:
                n_criteria, n_vars = map(int, input("Кол-во вариантов и критериев: ").split())
            except TypeError:
                print("Неверный ввод")
                return
            self.n_criteria = n_criteria
            self.n_vars = n_vars

            self.criteria.clear()
            for i in range(n_criteria):
                c = Criteria()
                self.criteria.append(c.read())

        for i in range(self.n_vars):
            print(f"Ввод варианта В{i+1}")
            self.data = []
            for j in range(len(self.criteria)):
                x = float(input(f"{self.criteria[j].name} - "))
                self.data.append(x)

        print("Ввод завершен.")
        print(self)

    def __str__(self):
        text = "Матрица:\n"
        for c in self.criteria:
            text += str(c) + "\n"
        for i, d in enumerate(self.data):
            text += f"В{i+1}|"
            for val in d:
                text += f"{val:^8.1f}|"
            text += "\n"
        hr = "-" * 10
        return text





class Solution:
    def __init__(self, matrix: CriteriaMatrix):
        self.mat = matrix

    def get_row_criteria_and_data(self, k: int = 1) -> List[tuple]:
        res = []
        for i in range(len(self.mat.criteria)):
            c = self.mat.criteria[i]
            if c.rate <= k:
                x = self.get_row_data(i)
                res.append((c, x))

        return sorted(res, key=lambda t: t[0].rate)

    def get_row_data(self, n):
        res = []
        for i in range(len(self.mat.data)):
            res.append(self.mat.data[i][n])
        return res

    def method_1(self):
        """
        Метод главного локального критерия
        """
        text = "-Метод главного локального критерия-\n"
        c, data = self.get_row_criteria_and_data(1)[0]
        text += str(c) + "\n" + str(data)
        k = -1 if c.is_down else 1
        max_val, max_index = data[0], 0
        for i in range(1, len(self.mat.data)):
            if max_val * k < data[i] * k:
                max_val = data[i]
                max_index = i
        text += f"\nЛучший вариант В{max_index + 1}\n"
        print(text)
        return text

    def method_2(self, i1, i2):
        text = "-Метод двух осн. локальных критериев-\n"
        c1, c2 = self.mat.criteria[i1], self.mat.criteria[i2]
        text = str(c1) + " (делимое >)\n" + str(c2) + " (делитель <)\nОтношение критериев\n"
        data1, data2 = self.get_row_data(i1), self.get_row_data(i2)
        max_val = data1[0] / data2[0]
        max_index = 0
        i = 0
        for item_big, item_small in zip(data1, data2):
            text += f"|{item_big / item_small:^10.2f}|"
            if item_big / item_small > max_val:
                max_val = item_big / item_small
                max_index = i
            i += 1
        text += f"\nЛучший вариант В{max_index + 1}\n"
        print(text)
        return text

    def method_3(self, procentage: float):
        text = "-Метод предпочтения локальных критериев-\n"
        left_variants = [1 for i in range(self.mat.n_vars)]
        curr_rate = 1
        all_rows = self.get_row_criteria_and_data(100)
        while left_variants.count(-1) < len(left_variants) - 1 and curr_rate < len(all_rows):
            c, data = all_rows[curr_rate-1]
            text += str(c) + "\n" + str(data) + "\n"
            k = -1 if c.is_down else 1
            max_val, max_index = data[0], 0
            for i in range(1, len(self.mat.data)):
                if max_val * k < data[i] * k:
                    max_val = data[i]
                    max_index = i
            text += f"В{max_index+1} лучший. Считаем дельты:\n"
            deltas = []
            for i in range(len(data)):
                delta = abs(max_val - data[i]) / max_val
                text += f"|{delta:^8.2f}|"
                deltas.append(delta)
            text += "\n"
            for i in range(len(deltas)):
                if deltas[i] > procentage / 100 and left_variants[i] != -1:
                    left_variants[i] = -1
                    text += f"Выкидываем В{i+1}\n"
            curr_rate += 1
        best_num = left_variants.index(1) + 1
        text += f"Лучший вариант В{best_num}\n"
        if curr_rate == len(all_rows):
            text += " (неоптимально по Паретто)\n"
        print(text)
        return text





def main():
    mat = CriteriaMatrix(4, 4)
    criteria = [
        Criteria(2, False, "Мощность"),
        Criteria(2, True, "Стоимость"),
        Criteria(2, True, "Расход"),
        Criteria(1, True, "Разгон"),
    ]
    data = [
        [100, 20, 8.3, 10.3],
        [110, 30, 8.4, 11.7],
        [200, 41, 7.8, 9.8],
        [85, 70, 12, 12.1],
    ]
    mat.criteria = criteria
    mat.data = data
    # mat.read(False)
    sol = Solution(mat)
    sol.method_1()
    sol.method_2(0, 1)
    sol.method_3(10)

if __name__ == '__main__':
    main()