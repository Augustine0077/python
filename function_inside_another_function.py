#punction inside another function

def process_student():
    def calculate_grade(mark):
        if mark >= 90:
            return "A"
        elif mark >= 75:
            return "B"
        else:
            return "C"
    
    return calculate_grade(82)

print(process_student())  
