def calculate_cgpa():
    num_semesters = int(input("Enter number of semesters: "))
    sgpas = []

    for i in range(num_semesters):
        sgpa = float(input(f"Enter SGPA for Semester {i + 1}: "))
        sgpas.append(sgpa)

    cgpa = sum(sgpas) / len(sgpas)

    return cgpa
