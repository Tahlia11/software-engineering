student_profile={
    "name":
    "age:"
    "grade:"
    "enrolled:"
    
}

student_profile["name"] = input("Enter the students name: ")
student_profile["age"] = int(input("Enter the students age: "))
student_profile["enrolled"] = input("Is the student enrolled: ").lower() == "yes"

print("\Student Profile")
print(f"Name: {student_profile['name']}")
print(f"Age: {student_profile['age']}")
print(f"Enrolled: {student_profile['enrolled']}")