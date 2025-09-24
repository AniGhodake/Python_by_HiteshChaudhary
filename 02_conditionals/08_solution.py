password = "Secure3P@ss"

if len(password) < 6:
    strenght = "Weak"
elif len(password) < 10:
    strenght = "Medium"
else:
    strenght = "Strong"

print("Password Strength is :",strenght)