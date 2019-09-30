students = {"chem2": 0, "chem8": 0, "chem10": 0}
students["chem2"] = 373
students["chem8"] = 273
students["chem10"] = 301
students["chem2"] += 5
students["chem10"] -= 14
for i in students:
    print("%6s: %5d" %(i, students[i]))
