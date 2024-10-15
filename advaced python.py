#1
[10, 501, 22, 100, 999, 87, 351]
#2
data = [10, "hello", 3.14, "world", 100, "Python"]

result = list(map(lambda x: "string" if isinstance(x, str) else "integer" if isinstance(x, int) else "other", data))

print(result)
#3
fibonacci = lambda x: x if x <= 1 else fibonacci(x-1) + fibonacci(x-2)

fib_series = list(map(fibonacci, range(50)))

print(fib_series)
#4
import re

def validate_input(input_type, input_value):
    patterns = {
        "email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        "bd_mobile": r"^\+8801[3-9]\d{8}$",
        "usa_telephone": r"^\+1[2-9]\d{2}[2-9](?!11)\d{6}$",
        "password": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$"
    }

    if input_type not in patterns:
        return False

    return re.match(patterns[input_type], input_value) is not None

email = "example@example.com"
bd_mobile = "+8801712345678"
usa_telephone = "+11234567890"
password = "Passw0rd@2024Test"

print("Email valid:", validate_input("email", email))
print("Bangladesh mobile valid:", validate_input("bd_mobile", bd_mobile))
print("USA telephone valid:", validate_input("usa_telephone", usa_telephone))
print("Password valid:", validate_input("password", password))
