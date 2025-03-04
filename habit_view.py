from tabulate import tabulate

class CLIView:
    def __init__(self, controller):
        self.controller = controller

    def show_all_habits(self):
        """Fetch and display all habits in a table format"""
        habits = self.controller.get_all_habits()

        if not habits:
            print("No habits found in Redis!")
            return

        table_data = []
        for habit in habits:
            table_data.append([habit["id"], habit["name"], habit["category"], habit["status"]])

        print("\n--- All Habits ---")
        print(tabulate(table_data, headers=["ID", "Name", "Category", "Status"], tablefmt="grid"))
