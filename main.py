from XLPtB2 import *

def my_app():
    print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
    a = float(input("Nhập a : "))
    b = float(input("Nhập b : "))
    c = float(input("Nhập c : "))
    XL_PTBHai = XuLyPtB2(a, b, c)
    Nghiem = XL_PTBHai.TimNghiem()
    if input("Type y <return> to restart the app! ").lower() == "y":
        return True

if __name__ == "__main__":
    restart_on_exit = True
    while restart_on_exit:
        restart_on_exit = my_app()

