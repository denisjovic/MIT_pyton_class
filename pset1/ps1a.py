savings = 0
r = 0.04
total_cost = float(input("How much your dream house costs?"))
annual_salary = float(input("How much you earn per year?"))
monthly = annual_salary / 12
portion_saved = float(input("How much you can save per month?"))
down_payment = 0.25 * total_cost
monthly_savings = monthly * portion_saved

time_to_goal = 0

while savings < down_payment:
    investment = savings * r / 12
    new_savings = investment + monthly_savings
    savings += new_savings
    time_to_goal += 1
print("months to goal: " + str(time_to_goal))