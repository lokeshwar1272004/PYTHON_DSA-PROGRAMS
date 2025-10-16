d ={}
class cgpa:
    credit_list = []
    calculated_cgpa = []
    total = 0
    dictionary = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5}

    def __init__(self):
        index = int(input("enter how many sub: "))
        for i in range(index):
            grade = input("enter your grade: ").upper()
            if grade in cgpa.dictionary:
                self.value_grade = cgpa.dictionary[grade]

            else:
                print("not valid")
            self.credit = int(input("enter your credit: "))
            cgpa.credit_list.append(self.credit)
            cgpa.total += self.value_grade * self.credit

            print("sub", i + 1, "added")
            print("......")
        print("sum of total_cgpa", cgpa.total)
        r = cgpa.total / sum(cgpa.credit_list)
        cgpa.calculated_cgpa.append(r)
        self.data_cgp=round(r,4)
        print("your cgpa is:>>>", round(r, 4), "<<<<")
a=cgpa()
print(a)