#Add an item

#print the current list

#delete an item

#add a check mark

class todo:
    def __init__(self,list = []):
        self.list = list
        self.items = 0

    def add_item(self, add_item):
        self.list.append(add_item)
        with open("todo.txt", "w") as file:
            for i in range(len(self.list)):
                file.write(f"{self.list[i]}\n")

    def remove_item(self, remove_item):
        for i in range(len(self.list)):
            if self.list[i] == remove_item:
                self.list.pop(i)
                break # Assuming you only want to remove the first occurrence
        with open("todo.txt", "w") as file:
            for item in self.list:
                file.write(f"{item}\n")

    def display_new_item():
        pass


todolist = todo()
todolist.add_item('do tthis')
todolist.add_item('do this now')
todolist.add_item('do this last')
todolist.remove_item('do this now')
todolist.add_item('do aa')
todolist.add_item('do this fdf')
todolist.add_item('do this last')
