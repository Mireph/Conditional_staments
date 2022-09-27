budget = float(input())
n_video = int(input())
m_cpu = int(input())
p_ram = int(input())
pr_video = 250 * n_video
pr_cpu = pr_video * 0.35 * m_cpu
pr_ram = pr_video * 0.1 * p_ram
price_sub_total = pr_video + pr_cpu + pr_ram
if n_video > m_cpu:
    total_price = price_sub_total -(price_sub_total * 0.15)
else:
    total_price = price_sub_total
if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")