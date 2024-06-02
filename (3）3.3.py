def main():
    grades = []
    print("請輸入每個學生的成績，輸入 -1 表示結束輸入。")
    
    while True:
        grade = float(input("請輸入成績: "))
        if grade == -1:
            break
        grades.append(grade)
    
    if grades:
        total_students = len(grades)
        passing_students = sum(1 for grade in grades if grade >= 60)
        failing_students = total_students - passing_students
        average_grade = sum(grades) / total_students
        
        print(f"全班人數: {total_students}")
        print(f"及格人數: {passing_students}")
        print(f"不及格人數: {failing_students}")
        print(f"全班平均成績: {average_grade:.2f}")
    else:
        print("沒有輸入任何成績。")

if __name__ == "__main__":
    main()