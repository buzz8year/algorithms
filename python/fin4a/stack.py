class Stack:
    def __init__(self):
        self.st = []

    def push(self, n):
        self.st.append(n)

    def pop(self):
        if len(self.st) == 0:
            return None
        return self.st.pop

    def __repr__(self):
        return str(self.st)


class TaskManager:
    def __init__(self):
        self.task = {}

    def new_stack(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

    def __repr__(self):
        return str(sorted(self.task.items(), key=lambda x: x[0]))


s = TaskManager()
s.new_stack("помыть посуду", 4)
s.new_stack("постирать белье", 4)
s.new_stack("побухать с мужиками", 1)
s.new_stack("сдать лабу по питошке", 2)
s.new_stack("покормить кота", 2)
print(s)
