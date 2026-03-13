class MultipleFunctions():
    def Subfields():
            print("Sub-fields in AI are:")
            lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
            for fields in lists:
                print(fields)
                
    def OddEven():
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                print(f"{num} is Even number")
            else:
                print(f"{num} is Odd number")
                
    def Eligible():
            gender = input("Your Gender:")
            if not gender.isalpha():
                print("This field accepts only Male or Female")
                print("Try Again")
                return
            age = int(input("Your Age:"))
            if gender == "Male" and age >= 21:
                print("ELIGIBLE")
            elif gender == "Female" and age >= 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
                
    def percentage():
        sub1 = int(input("Subject1= "))
        sub2 = int(input("Subject2= "))
        sub3 = int(input("Subject3= "))
        sub4 = int(input("Subject4= "))
        sub5 = int(input("Subject5= "))
        Total = sub1 + sub2 + sub3 + sub4 + sub5
        Percentage = Total / 5
        print("Total : ", Total)
        print("Percentage : ", Percentage)
        
    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", (height * breadth) / 2)
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", height1 + height2 + breadth)