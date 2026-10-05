"""
==================================================
🎯 GOALTRACK
Personal Goal Management System

Set goals. Track progress. Grow. 🚀
==================================================
"""

from datetime import date


# ==================================================
# 🎯 GOAL CLASS
# ==================================================

class Goal:

    def __init__(
        self,
        goal_id,
        title,
        description,
        category,
        deadline,
        progress
    ):
        self.id = goal_id
        self.title = title
        self.description = description
        self.category = category
        self.deadline = deadline
        self.progress = progress
        self.created_at = date.today()

    # ------------------------------------------------
    # Progress status
    # ------------------------------------------------

    def get_status(self):

        if self.progress == 0:
            return "Not Started"

        elif self.progress < 100:
            return "In Progress"

        else:
            return "Completed"

    # ------------------------------------------------
    # Deadline status
    # ------------------------------------------------

    def get_deadline_status(self):

        today = date.today()

        if self.deadline < today:
            return "⚠️ OVERDUE"

        elif self.deadline == today:
            return "🔥 DUE TODAY"

        else:
            days_left = (self.deadline - today).days
            return f"⏳ {days_left} days left"

    # ------------------------------------------------
    # Display goal
    # ------------------------------------------------

    def display(self):

        print("\n" + "=" * 55)
        print(f"🎯 GOAL #{self.id}")
        print("=" * 55)

        print(f"Title       : {self.title}")
        print(f"Description : {self.description}")
        print(f"Category    : {self.category}")
        print(f"Progress    : {self.progress}%")
        print(f"Status      : {self.get_status()}")
        print(f"Deadline    : {self.deadline}")
        print(f"Due Status  : {self.get_deadline_status()}")
        print(f"Created     : {self.created_at}")

        print("=" * 55)


# ==================================================
# 📦 STORAGE
# ==================================================

goals = []
next_id = 1


# ==================================================
# 🛠️ HELPER FUNCTIONS
# ==================================================

def find_goal(goal_id):

    for goal in goals:

        if goal.id == goal_id:
            return goal

    return None


# ==================================================
# ➕ ADD GOAL
# ==================================================

def add_goal():

    global next_id

    print("\n" + "=" * 55)
    print("➕ ADD NEW GOAL")
    print("=" * 55)

    title = input("Enter goal title: ").strip()

    if not title:
        print("❌ Title cannot be empty.")
        return

    description = input("Enter description: ").strip()

    category = input("Enter category: ").strip()

    if not category:
        category = "General"

    # ------------------------------------------------
    # Deadline validation
    # ------------------------------------------------

    while True:

        deadline_input = input(
            "Enter deadline (YYYY-MM-DD): "
        ).strip()

        try:

            deadline = date.fromisoformat(deadline_input)

            if deadline < date.today():
                print("❌ Deadline cannot be in the past.")
                continue

            break

        except ValueError:

            print(
                "❌ Invalid date format. "
                "Please use YYYY-MM-DD."
            )

    # ------------------------------------------------
    # Progress validation
    # ------------------------------------------------

    while True:

        try:

            progress = int(
                input("Enter progress (0-100): ")
            )

            if 0 <= progress <= 100:
                break

            print("❌ Progress must be between 0 and 100.")

        except ValueError:

            print("❌ Please enter a number.")

    # ------------------------------------------------
    # Create goal
    # ------------------------------------------------

    goal = Goal(
        next_id,
        title,
        description,
        category,
        deadline,
        progress
    )

    goals.append(goal)

    next_id += 1

    print("\n✅ Goal added successfully!")
    print(f"🎯 Goal ID: {goal.id}")


# ==================================================
# 📋 SHOW ALL GOALS
# ==================================================

def show_goals():

    if not goals:

        print("\n📭 No goals found.")
        return

    print("\n" + "=" * 55)
    print("📋 YOUR GOALS")
    print("=" * 55)

    for goal in goals:
        goal.display()


# ==================================================
# 🔎 SEARCH GOAL
# ==================================================

def search_goal():

    if not goals:

        print("\n📭 No goals available.")
        return

    keyword = input(
        "\n🔎 Search by title, description or category: "
    ).strip().lower()

    if not keyword:

        print("❌ Search cannot be empty.")
        return

    found = []

    for goal in goals:

        if (
            keyword in goal.title.lower()
            or keyword in goal.description.lower()
            or keyword in goal.category.lower()
        ):
            found.append(goal)

    if not found:

        print("\n❌ No matching goals found.")
        return

    print(f"\n🔎 Found {len(found)} goal(s):")

    for goal in found:
        goal.display()


# ==================================================
# 🗂️ FILTER BY CATEGORY
# ==================================================

def filter_by_category():

    if not goals:

        print("\n📭 No goals available.")
        return

    category = input(
        "\n🗂️ Enter category: "
    ).strip().lower()

    found = []

    for goal in goals:

        if goal.category.lower() == category:
            found.append(goal)

    if not found:

        print("\n❌ No goals found in this category.")
        return

    print(f"\n🗂️ Goals in '{category}':")

    for goal in found:
        goal.display()


# ==================================================
# 📈 UPDATE PROGRESS
# ==================================================

def update_progress():

    if not goals:

        print("\n📭 No goals available.")
        return

    try:

        goal_id = int(
            input("\nEnter goal ID: ")
        )

    except ValueError:

        print("❌ Invalid ID.")
        return

    goal = find_goal(goal_id)

    if goal is None:

        print("❌ Goal not found.")
        return

    print("\n" + "-" * 55)
    print(f"🎯 Goal: {goal.title}")
    print(f"📈 Current progress: {goal.progress}%")
    print("-" * 55)

    while True:

        try:

            new_progress = int(
                input("Enter new progress (0-100): ")
            )

            if 0 <= new_progress <= 100:
                break

            print("❌ Progress must be between 0 and 100.")

        except ValueError:

            print("❌ Please enter a number.")

    goal.progress = new_progress

    print("\n✅ Progress updated!")
    print(f"📈 Progress: {goal.progress}%")
    print(f"📌 Status: {goal.get_status()}")


# ==================================================
# 📅 UPDATE DEADLINE
# ==================================================

def update_deadline():

    if not goals:

        print("\n📭 No goals available.")
        return

    try:

        goal_id = int(
            input("\nEnter goal ID: ")
        )

    except ValueError:

        print("❌ Invalid ID.")
        return

    goal = find_goal(goal_id)

    if goal is None:

        print("❌ Goal not found.")
        return

    print(f"\n🎯 Goal: {goal.title}")
    print(f"📅 Current deadline: {goal.deadline}")

    while True:

        deadline_input = input(
            "Enter new deadline (YYYY-MM-DD): "
        ).strip()

        try:

            new_deadline = date.fromisoformat(
                deadline_input
            )

            if new_deadline < date.today():

                print("❌ Deadline cannot be in the past.")
                continue

            break

        except ValueError:

            print(
                "❌ Invalid date format. "
                "Use YYYY-MM-DD."
            )

    goal.deadline = new_deadline

    print("\n✅ Deadline updated!")
    print(f"📅 New deadline: {goal.deadline}")
    print(f"⏳ {goal.get_deadline_status()}")


# ==================================================
# 🗑️ DELETE GOAL
# ==================================================

def delete_goal():

    if not goals:

        print("\n📭 No goals available.")
        return

    try:

        goal_id = int(
            input("\nEnter goal ID: ")
        )

    except ValueError:

        print("❌ Invalid ID.")
        return

    goal = find_goal(goal_id)

    if goal is None:

        print("❌ Goal not found.")
        return

    print(f"\n🎯 Goal: {goal.title}")

    confirmation = input(
        "Are you sure you want to delete it? (y/n): "
    ).strip().lower()

    if confirmation == "y":

        goals.remove(goal)

        print("\n🗑️ Goal deleted successfully!")

    else:

        print("\n↩️ Deletion cancelled.")


# ==================================================
# 📊 STATISTICS
# ==================================================

def show_statistics():

    if not goals:

        print("\n📭 No goals available.")
        return

    total = len(goals)

    completed = 0
    in_progress = 0
    not_started = 0
    overdue = 0
    due_today = 0

    total_progress = 0

    for goal in goals:

        total_progress += goal.progress

        # Progress status

        if goal.progress == 0:

            not_started += 1

        elif goal.progress < 100:

            in_progress += 1

        else:

            completed += 1

        # Deadline status

        today = date.today()

        if goal.deadline < today:

            overdue += 1

        elif goal.deadline == today:

            due_today += 1

    average_progress = total_progress / total

    print("\n" + "=" * 55)
    print("📊 GOAL STATISTICS")
    print("=" * 55)

    print(f"🎯 Total Goals       : {total}")
    print(f"✅ Completed         : {completed}")
    print(f"🔄 In Progress       : {in_progress}")
    print(f"⏳ Not Started       : {not_started}")
    print(f"⚠️ Overdue           : {overdue}")
    print(f"🔥 Due Today         : {due_today}")
    print(f"📈 Average Progress  : {average_progress:.1f}%")

    print("=" * 55)


# ==================================================
# ⚠️ SHOW DEADLINES
# ==================================================

def show_deadlines():

    if not goals:

        print("\n📭 No goals available.")
        return

    print("\n" + "=" * 55)
    print("📅 DEADLINE OVERVIEW")
    print("=" * 55)

    today = date.today()

    overdue_goals = []
    today_goals = []
    upcoming_goals = []

    for goal in goals:

        if goal.deadline < today:

            overdue_goals.append(goal)

        elif goal.deadline == today:

            today_goals.append(goal)

        else:

            upcoming_goals.append(goal)

    # ------------------------------------------------
    # Overdue
    # ------------------------------------------------

    if overdue_goals:

        print("\n⚠️ OVERDUE")

        for goal in overdue_goals:

            print(
                f"  #{goal.id} - "
                f"{goal.title} "
                f"({goal.deadline})"
            )

    # ------------------------------------------------
    # Due today
    # ------------------------------------------------

    if today_goals:

        print("\n🔥 DUE TODAY")

        for goal in today_goals:

            print(
                f"  #{goal.id} - "
                f"{goal.title}"
            )

    # ------------------------------------------------
    # Upcoming
    # ------------------------------------------------

    if upcoming_goals:

        print("\n⏳ UPCOMING")

        upcoming_goals.sort(
            key=lambda goal: goal.deadline
        )

        for goal in upcoming_goals:

            days_left = (
                goal.deadline - today
            ).days

            print(
                f"  #{goal.id} - "
                f"{goal.title} | "
                f"{goal.deadline} | "
                f"{days_left} days left"
            )

    print("\n" + "=" * 55)


# ==================================================
# 🏠 DASHBOARD
# ==================================================

def dashboard():

    print("\n" + "=" * 55)
    print("🏠 GOALTRACK DASHBOARD")
    print("=" * 55)

    if not goals:

        print("\n📭 You don't have any goals yet.")
        print("💡 Start by adding your first goal!")

        print("=" * 55)
        return

    total = len(goals)

    completed = 0
    overdue = 0
    total_progress = 0

    today = date.today()

    for goal in goals:

        total_progress += goal.progress

        if goal.progress == 100:
            completed += 1

        if goal.deadline < today:
            overdue += 1

    average_progress = total_progress / total

    print(f"\n🎯 Total Goals      : {total}")
    print(f"✅ Completed        : {completed}")
    print(f"⚠️ Overdue          : {overdue}")
    print(f"📈 Average Progress : {average_progress:.1f}%")

    print("\n📌 Recent Goals:")

    for goal in goals[-3:]:
        print(
            f"  #{goal.id} "
            f"{goal.title} "
            f"— {goal.progress}%"
        )

    print("=" * 55)


# ==================================================
# 🧭 MENU
# ==================================================

def show_menu():

    print("\n")

    print("╔══════════════════════════════════════╗")
    print("║            🎯 GOALTRACK              ║")
    print("║      Set goals. Track progress.      ║")
    print("║               Grow. 🚀               ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. 🏠 Dashboard                    ║")
    print("║  2. ➕ Add Goal                      ║")
    print("║  3. 📋 Show Goals                    ║")
    print("║  4. 🔎 Search Goal                   ║")
    print("║  5. 🗂️ Filter by Category            ║")
    print("║  6. 📈 Update Progress               ║")
    print("║  7. 📅 Update Deadline               ║")
    print("║  8. 📅 Deadline Overview              ║")
    print("║  9. 🗑️ Delete Goal                   ║")
    print("║ 10. 📊 Statistics                    ║")
    print("║  0. 🚪 Exit                          ║")
    print("╚══════════════════════════════════════╝")


# ==================================================
# 🚀 MAIN PROGRAM
# ==================================================

def main():

    while True:

        show_menu()

        choice = input(
            "\n👉 Choose an option: "
        ).strip()

        if choice == "1":

            dashboard()

        elif choice == "2":

            add_goal()

        elif choice == "3":

            show_goals()

        elif choice == "4":

            search_goal()

        elif choice == "5":

            filter_by_category()

        elif choice == "6":

            update_progress()

        elif choice == "7":

            update_deadline()

        elif choice == "8":

            show_deadlines()

        elif choice == "9":

            delete_goal()

        elif choice == "10":

            show_statistics()

        elif choice == "0":

            print("\n" + "=" * 55)
            print("👋 Thank you for using GoalTrack!")
            print("🎯 Keep setting goals.")
            print("📈 Keep tracking progress.")
            print("🚀 Keep growing!")
            print("=" * 55)

            break

        else:

            print(
                "\n❌ Invalid option. "
                "Please choose from 0 to 10."
            )


# ==================================================
# ▶️ PROGRAM START
# ==================================================

if __name__ == "__main__":
    main()