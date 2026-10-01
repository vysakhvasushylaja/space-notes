import math

mu = 398600   # ഭൂമിയുടെ ഗുരുത്വാകർഷണ സംഖ്യ
R = 6378      # ഭൂമിയുടെ ആരം, km

# LEO: ഉയരം അറിയാം -> വേഗവും സമയവും
for alt in [400, 800]:
    r = R + alt
    v = math.sqrt(mu / r)
    T = 2 * math.pi * r**1.5 / math.sqrt(mu)
    print(f"{alt} km: speed {v:.2f} km/s, period {T/60:.1f} min")

# GEO: സമയം അറിയാം -> ഉയരം
T = 86164
r = (mu * T**2 / (4 * math.pi**2)) ** (1/3)
print(f"GEO: height {r - R:.0f} km")
