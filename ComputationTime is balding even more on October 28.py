# daytime = int(input())
# evening = int(input())
# weekend = int(input())
# plan_a_cost = ((daytime - 100) if daytime > 100 else 0) * 0.25 + evening * 0.15 + weekend * 0.2
# plan_b_cost = ((daytime - 250) if daytime > 250 else 0) * 0.45 + evening * 0.35 + weekend * 0.25
# print(f"Plan A costs {plan_a_cost:.2f}")
# print(f"Plan B costs {plan_b_cost:.2f}")
# if plan_a_cost > plan_b_cost:
#     print("Plan B is cheapest.")
# elif plan_a_cost < plan_b_cost:
#     print("Plan A is cheapest.")
# else: 
#     print("Plan A and B are the same price.")

typed = input().split()
first_date = int(typed[0])
number_of_days = int(typed[1])
print("Sun Mon Tue Wed Thr Fri Sat")
print(" " * 4 * (first_date - 1), end="")
a = 7 - first_date
print(f"{1:3.0f}", end="")
for i in range (a):
    print(f" {2 + i:3.0f}", end="")
days_left = number_of_days - a - 1

for i in range (days_left):
    if (i) % 7 == 0:
        print()
    else:
        print(" ", end='')

    print(f"{a + 2 + i:3.0f}", end="")
print()

