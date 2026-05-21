""" 
    Trong code hiện tại:
    Vòng lặp ngoài duyệt theo tháng
    Vòng lặp trong duyệt theo chi nhánh

    Nên kết quả sẽ hiển thị:

    Tháng 1 -> CN1, CN2, CN3
    Tháng 2 -> CN1, CN2, CN3
    Tháng 3 -> CN1, CN2, CN3

    Tức là dữ liệu đang được gom theo tháng.
    => Phải gom dữ liệu theo từng chi nhánh.
 """

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

all_students = 0  

for branch in range(1, branch_count + 1):

    print(f"\nChi nhánh {branch}")

    total_students = 0

    for classroom in range(1, class_count + 1):

        student_count = int(
            input(f"Nhập số học viên lớp {classroom}: ")
        )

        total_students += student_count

    print(f"Chi nhánh {branch}: "
          f"{total_students} học viên")

    all_students += total_students   

print(f"Tổng số học viên của tất cả chi nhánh: {all_students}")
