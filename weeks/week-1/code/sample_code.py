# Assigning values
name = "Abhi"
age = 30
height = 1.78

# Printing values
print(name, age, height)

# Data types
x = 42
y = 3.14
name = "AI Engineer"
is_ready = True
print(type(x), type(y), type(name), type(is_ready))


# Lists
skills = ["Python", "ML", "API", "Agentic AI"]

# Access elements
print(skills[0])   # Python
print(skills[-1])  # Agentic AI

# Modify
skills.append("LangChain")
skills.remove("API")

# Loop through
for skill in skills:
    print(skill)
    
# Dictionaries
developer = {
    "name": "Abhi",
    "role": "Backend Developer",
    "experience": 10
}

# Access values
print(developer["name"])     # Abhi
# Add new key
developer["speciality"] = "AI"
# Loop through keys & values
for key, value in developer.items():
    print(f"{key}: {value}")

#### Loops
# For loop - iterates over sequences (lists, strings, etc.)
for i in range(5):
    print(i)

# While loop - repeats as long as a condition is true
count = 0
while count < 5:
    print(count)
    count += 1