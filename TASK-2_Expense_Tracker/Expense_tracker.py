expenses = []
total = 0

while True:

    user_input = input("Enter expense amount (or 'Done'): ")

    if user_input.lower() == "done":
        break

    try:
        expense = int(user_input)

        expenses.append(expense)

        total += expense

        print(f"Current Total: ₹{total}")

    except ValueError:
        print("Invalid input! Enter numbers only.")

print("\n===== EXPENSE REPORT =====")

for index, expense in enumerate(expenses, start=1):
    print(f"{index}. ₹{expense}")

print(f"\nTotal Expense: ₹{total}")

if len(expenses) > 0:
    print(f"Average Expense: ₹{total/len(expenses):.2f}")
    print(f"Highest Expense: ₹{max(expenses)}")
    print(f"Lowest Expense: ₹{min(expenses)}")