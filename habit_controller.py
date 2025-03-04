from habit_model import Habit

class HabitController:
    def get_all_habits(self):
        """Fetch all habits from the Model"""
        return Habit.get_all_habits()

