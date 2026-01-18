class Brainfu:
    def __init__(self, cell_num):
        self.cells = {}
        for i in range(1, cell_num  + 1):
            self.cells[i] = 0
        self.current_cell = 1
        self.output = ""
        self.running = True


    def run(self):
        print("Brainfu")

        while self.running:
            user_input = input("> ")

            if user_input == "exit":
                print("Программа завершена.")
                self.running = False
                break

            elif user_input == "clear":
                self.current_cell = 1
                for key in self.cells:
                    self.cells[key] = 0
                self.output = ""
                print("Программа очищена.")
                continue

            elif user_input == "info":
                print("Информация")
                continue
            

            for symbol in user_input:
                self.execute_symbol(symbol)

            print(f'Ячейки: {self.cells}')
            print(f'Вывод: {self.output}')
            print(f'Номер текущей ячейки: {self.current_cell}')

    def execute_symbol(self, symbol):
        if symbol == "+":
            self.cells[self.current_cell] = (self.cells[self.current_cell] + 1) % 256
        elif symbol == "-":
            self.cells[self.current_cell] = (self.cells[self.current_cell] - 1 ) % 256
        elif symbol == ">":
            if self.current_cell < len(self.cells):
                self.current_cell += 1
            else:
                print("Ошибка: Ячейка упирается в лимит.")
        elif symbol == "<":
            if self.current_cell > 1:
                self.current_cell -= 1
            else:
                print("Ошибка: Ячейка упирается в лимит.")
        elif symbol == "[":
            pass
        elif symbol == "]":
            pass
        elif symbol == ".":
            value = chr(self.cells[self.current_cell] % 256)
            self.output += value + " "
            print(f'{value}')
        elif symbol == ",":
            user_char = input("Введите один символ: ")
            if user_char:
                self.cells[self.current_cell] = ord(user_char[0]) % 256
        else:
            print(f'Ошибка: Команда "{symbol}" не найдена.')

    def read_file(self, file_name):
        try:
           with open(file_name, "r", encoding="utf-8") as file:
               self.content = file.read()
        except Exception as e:
            print(f'Ошибка: {e}')
            
    def run_file(self):
        pass

brainfu = Brainfu(4)
brainfu.run()
print(brainfu.cells)