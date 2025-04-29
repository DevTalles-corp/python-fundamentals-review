
# and
age = 18
licensed = False

if age >= 18 and licensed:
    print("Puedes manejar")

# or
is_student = False
membership = False

if is_student or membership:
    print("Obtiene precio especial")

# not
is_admin = True
if not is_admin:
    print("Acceso denegado")

# Short Circuiting
name = "Ricardo"
print(name and name.upper())
