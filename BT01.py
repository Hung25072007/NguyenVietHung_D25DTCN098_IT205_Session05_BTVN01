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
month_count = 3


for branch in range(1, branch_count + 1):

    for month in range(1, month_count + 1):

        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: ")
        )
    print("\n-------------- Kết quả --------------")
    
    for month in range(1, month_count + 1):

        print(f"Chi nhánh {branch}, tháng {month}: "
              f"{revenue} triệu đồng")