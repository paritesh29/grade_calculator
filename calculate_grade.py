# Function to calculate grade and return grade + message
def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent! Outstanding performance! "
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! "
    elif 70 <= marks <= 79:
        return "C", "Good job! You can aim even higher! "
    elif 60 <= marks <= 69:
        return "D", "Keep trying! You're improving! "
    else:
        return "F", "Don't give up! Work harder and you'll succeed! "


# Function to get valid marks (0-100 only)
def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


# Main function
def main():
    name = input("Enter student name: ")
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", name.upper() + ":")
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


# Run the program
main()