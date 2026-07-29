from datetime import date, datetime
from objective import Todo


class Task(Todo):    

    def determine_priority(self):
        priority_score = 0

        high_prio_tasks = ["Work", "University"]
        mid_prio_tasks = ["Personal", "Health"]

        # Task type
        if self.action_type in high_prio_tasks:
            priority_score += 50
        elif self.action_type in mid_prio_tasks:
            priority_score += 25

        # Remaining work
        spent_hours = int(input("How many hours have you spent on this task so far? "))
        remaining_hours = self.allocated_time - spent_hours

        print(f"Remaining work: {remaining_hours} hours")

        if remaining_hours >= 8:
            priority_score += 30
        elif remaining_hours >= 4:
            priority_score += 20
        elif remaining_hours >= 1:
            priority_score += 10

        # Due date
        today = date.today()


        if isinstance(self.action_due_date, str):
            due_date = datetime.strptime(self.action_due_date, "%d/%m/%Y").date()
        else:
            due_date = self.action_due_date

        days_remaining = (due_date - today).days

        if days_remaining < 0:
            priority_score += 100          # Overdue
        elif days_remaining == 0:
            priority_score += 80           # Due today
        elif days_remaining <= 3:
            priority_score += 60
        elif days_remaining <= 5:
            priority_score += 40
        elif days_remaining <= 7:
            priority_score += 20
        else:
            priority_score += 5

        # Current progress
        possible_status = [
            "Just Started",
            "In The Works",
            "Almost Complete",
            "Completed"
        ]

        print(f"Current state of task {self.action_id}:")

        for status in possible_status:
            print(status)

        current_state = input("Please state here: ").title()

        while current_state not in possible_status:
            print("Please select a valid status.")
            current_state = input("Please state here: ").title()

        if current_state == "Just Started":
            priority_score += 20
        elif current_state == "In The Works":
            priority_score += 10
        elif current_state == "Almost Complete":
            priority_score += 5
        elif current_state == "Completed":
            priority_score = 0

        return priority_score