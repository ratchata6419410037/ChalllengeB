import os


def create_new_file():
    file_name = input("ป้อนชื่อไฟล์ (ภาษาอังกฤษ) สำหรับวิชาใหม่: ")
    if file_name.endswith('.txt'):
        
        with open(file_name, 'w') as file:
            file.write('')
            print(f"ไฟล์ {file_name} ถูกสร้างขึ้นแล้ว")
            
            student_name = input("ป้อนชื่อ-สกุลนักเรียน: ")
            midterm_score = float(input("ป้อนคะแนนสอบกลางภาค: "))
            final_score = float(input("ป้อนคะแนนสอบปลายภาค: "))
            additional_score = float(input("ป้อนคะแนนเก็บ: "))
            total_score = midterm_score + final_score + additional_score
            result = "ผ่าน" if total_score > 50 else "ไม่ผ่าน"
            
            with open(file_name, 'a') as file:
                file.write(f"{student_name},{midterm_score},{final_score},{additional_score},{total_score},{result}\n")
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงในไฟล์เรียบร้อยแล้ว")

    else:
        print("ชื่อ - นามสกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่")



def display_all_files():
    files = [file for file in os.listdir() if file.endswith('.txt')]
    if not files:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
    else:
        print("ไฟล์ที่สร้างไว้:")
        for file in files:
            print(file)



def append_data_to_file():
    display_all_files()
    selected_file = input("เลือกไฟล์ที่ต้องการ: ")
    if selected_file not in os.listdir() or not selected_file.endswith('.txt'):
        print("คุณพิมพ์ชื่อไฟล์ผิด")
    else:
        
        with open(selected_file, 'a') as file:
            student_name = input("ป้อนชื่อ-สกุลนักเรียน: ")
            midterm_score = float(input("ป้อนคะแนนสอบกลางภาค: "))
            final_score = float(input("ป้อนคะแนนสอบปลายภาค: "))
            additional_score = float(input("ป้อนคะแนนเก็บ: "))
            total_score = midterm_score + final_score + additional_score
            result = "ผ่าน" if total_score > 50 else "ไม่ผ่าน"
            file.write(f"{student_name},{midterm_score},{final_score},{additional_score},{total_score},{result}\n")
            print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")



def read_file_data():
    display_all_files()
    selected_file = input("เลือกไฟล์ที่ต้องการ: ")
    if selected_file not in os.listdir() or not selected_file.endswith('.txt'):
        print("คุณพิมพ์ชื่อไฟล์ผิด")
    else:
        
        with open(selected_file, 'r') as file:
            data = file.read()
            print(f"ข้อมูลจากไฟล์ {selected_file}:\n{data}")



def delete_file():
    display_all_files()
    selected_file = input("เลือกไฟล์ที่ต้องการลบ: ")
    if selected_file not in os.listdir() or not selected_file.endswith('.txt'):
        print("คุณพิมพ์ชื่อไฟล์ผิด")
    else:
        
        os.remove(selected_file)
        print("ลบไฟล์เรียบร้อยแล้ว")



def main():
    while True:
        print("\nเมนู:")
        print("1. สร้างไฟล์วิชาใหม่")
        print("2. เพิ่มข้อมูลต่อท้ายไฟล์")
        print("3. อ่านข้อมูลจากไฟล์")
        print("4. ลบไฟล์")
        print("0. จบการทำงาน")
        
        choice = input("โปรดเลือกหมายเลขเมนู: ")

        if choice == '1':
            create_new_file()
        elif choice == '2':
            append_data_to_file()
        elif choice == '3':
            read_file_data()
        elif choice == '4':
            delete_file()
        elif choice == '0':
            print("จบการทำงานของโปรแกรม")
            break
        else:
            print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")


if __name__ == "__main__":
    main()
