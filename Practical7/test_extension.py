from staff_app import Department, Developer, Manager

engineering = Department("Engineering")

# Test department summary
print(engineering.summary())

# Test manager
manager = Manager("Rahul", "EMP102", engineering, 5)
print(manager.describe())
print("Team size:", manager.team_size)

# Test invalid team size
try:
    manager.team_size = -2
except ValueError as error:
    print("Validation:", error)

# Test blank name
try:
    Developer("", "EMP103", engineering, "Python")
except ValueError as error:
    print("Validation:", error)

# Test negative salary
dev = Developer("Riya", "EMP101", engineering, "Python")

try:
    dev.salary = -100
except ValueError as error:
    print("Validation:", error)