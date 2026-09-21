employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()
gross_salary = base_salary + (overtime_hours * 35)
if tax_status == "Single" and gross_salary >= 5000:
    tax_rate = 0.22
    elif



print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
