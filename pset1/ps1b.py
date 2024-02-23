savings = 0
r = 0.04
total_cost = float(input("How much your dream house costs?"))
annual_salary = float(input("How much you earn per year?"))
half_year_increment = float(input("How much your salary increases every 6 months?"))
monthly = annual_salary / 12
portion_saved = float(input("How much you can save per month?"))
down_payment = 0.25 * total_cost
monthly_savings = monthly * portion_saved

time_to_goal = 0

while savings < down_payment:
    if time_to_goal % 6 == 0 and time_to_goal != 0:
        increase = annual_salary * half_year_increment
        annual_salary += increase
        monthly = annual_salary  / 12
        monthly_savings = monthly * portion_saved
    investment = savings * r / 12
    new_savings = investment + monthly_savings
    savings += new_savings
    time_to_goal += 1
print("months to goal: " + str(time_to_goal))



#Enter your starting annual salary: 120000
#Enter the percent of your salary to save, as a decimal: .05
#Enter the cost of your dream home: 500000
#Enter the semi­annual raise, as a decimal: .03
#Number of months: 142 
#>>>
#Test Case 2 
#>>>  
#Enter your starting annual salary: 80000
#Enter the percent of your salary to save, as a decimal: .1
#Enter the cost of your dream home: 800000
#Enter the semi­annual raise, as a decimal: .03
#Number of months: 159 
#>>>
#Test Case 3 
#>>>  
#Enter your starting annual salary: 75000
#Enter the percent of your salary to save, as a decimal: .05
#Enter the cost of your dream home: 1500000
#Enter the semi­annual raise, as a decimal: .05
# Number of months: 261 