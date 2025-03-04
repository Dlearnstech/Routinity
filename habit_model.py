from config import redis_client  

class Habit:
    @staticmethod
    def get_all_habits():
        """Fetch all habits from Redis"""
        habit_keys = redis_client.keys("habit:*")  # Get all habit keys

        if not habit_keys:
            return []  # Return empty list if no habits found

        habits = []
        for key in habit_keys:
            habit_data = redis_client.hgetall(key)
            habit_id = key.split(":")[1]  # Extract habit ID from key
            habit_data["id"] = habit_id
            habits.append(habit_data)

        return habits
