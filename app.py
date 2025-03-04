from habit_controller import HabitController
from habit_view import CLIView

if __name__ == "__main__":
    habit_controller = HabitController()
    cli_view = CLIView(habit_controller)

    cli_view.show_all_habits() 

