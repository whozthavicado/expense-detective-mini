print("🕵️ Expense Detective")
print("Write your expense:")

expense = input()

expense = expense.lower()

if "comida" in expense or "food" in expense:
    print("✅ Necessary expense")
elif "uber" in expense or "taxi" in expense:
    print("⚠️ Could be avoided")
elif "ropa" in expense or "clothes" in expense:
    print("❌ Impulsive expense")
else:
    print("🤔 Not sure, think twice!")
