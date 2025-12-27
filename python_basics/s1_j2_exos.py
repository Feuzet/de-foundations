# S1-J2 — Python types + I/O + 10 mini-exos
# Objectif: pratiquer int/float/str/bool, input(), conversions, f-strings, arrondis

def rectangle_area(w, h):
    return w * h

# 1) Celsius -> Fahrenheit
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

# 2) Fahrenheit -> Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# 3) Aire cercle (float)
def circle_area(r):
    pi = 3.141592653589793
    return pi * r * r

# 4) Pair / impair (bool)
def is_even(n):
    return n % 2 == 0

# 5) Concat prénom + nom (str)
def full_name(first, last):
    return f"{first.strip().title()} {last.strip().upper()}"

# 6) Prix TTC (float) arrondi 2 décimales
def price_ttc(price_ht, tva_rate=0.20):
    return round(price_ht * (1 + tva_rate), 2)

# 7) Minutes -> "XhYY"
def minutes_to_hhmm(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h}h{m:02d}"

# 8) Moyenne de 3 notes (float)
def avg3(a, b, c):
    return (a + b + c) / 3

# 9) Conversion string -> int/float avec gestion simple
def safe_int(s):
    # retourne None si conversion impossible
    try:
        return int(s)
    except ValueError:
        return None

def safe_float(s):
    try:
        return float(s)
    except ValueError:
        return None

# 10) Mini I/O: demander nom + age + afficher phrase
def ask_user_and_print():
    name = input("Ton prénom ? ")
    age_str = input("Ton âge ? ")
    age = safe_int(age_str)
    if age is None:
        print("Âge invalide.")
        return
    print(f"Salut {name}, dans 5 ans tu auras {age + 5} ans.")

if __name__ == "__main__":
    # Tests rapides (doivent afficher quelque chose de cohérent)
    print("rectangle_area(3, 4) =", rectangle_area(3, 4))          # 12
    print("celsius_to_fahrenheit(0) =", celsius_to_fahrenheit(0))  # 32.0
    print("fahrenheit_to_celsius(32) =", fahrenheit_to_celsius(32))# 0.0
    print("circle_area(2) =", round(circle_area(2), 4))
    print("is_even(10) =", is_even(10))
    print("full_name('chris', 'feuzet') =", full_name("chris", "feuzet"))
    print("price_ttc(100) =", price_ttc(100))
    print("minutes_to_hhmm(135) =", minutes_to_hhmm(135))
    print("avg3(10, 12, 14) =", avg3(10, 12, 14))
    # Décommente pour tester I/O:
    # ask_user_and_print()

