from config import redis_client

class Habit:
    def __init__(self, habit_id, name, category, status="Not Started"):
        self.habit_id = habit_id
        self.name = name
        self.category = category
        self.status = status

    def save_to_db(self):
        """Save habit to Redis"""
        redis_client.hset(f"habit:{self.habit_id}", mapping={
            "name": self.name,
            "category": self.category,
            "status": self.status
        })

    @staticmethod
    def get_all_habits():
        """Fetch all habits stored in Redis"""
        habit_keys = redis_client.keys("habit:*")  # Get all habit keys
        habits = []
        for key in habit_keys:
            habit_data = redis_client.hgetall(key)
            habit_data["id"] = key.split(":")[1]  # Extract habit ID from key
            habits.append(habit_data)
        return habits

    def update_status(self, new_status):
        """Update habit status"""
        redis_client.hset(f"habit:{self.habit_id}", "status", new_status)
