
from library import Library


def main():
    library = Library()
    try:
    while True:
        print("\n===== 图书借阅管理系统 =====")
        print("1. 添加图书")
        print("2. 修改图书")
        print("3. 删除图书")
        print("4. 查询图书")
        print("5. 展示全部图书")
        print("6. 退出系统")

        choice = input("请输入选项：")

        if choice == "1":
            name = input("请输入书名：")
            author = input("请输入作者：")
            price = float(input("请输入价格："))
            stock = int(input("请输入库存："))
            library.add_book(name, author, price, stock)

        elif choice == "2":
            name = input("请输入要修改的书名：")
            author = input("请输入新作者：")
            price = float(input("请输入新价格："))
            stock = int(input("请输入新库存："))
            library.update_book(name, author, price, stock)

        elif choice == "3":
            name = input("请输入要删除的书名：")
            library.delete_book(name)

        elif choice == "4":
            name = input("请输入要查询的书名：")
            library.show_book(name)

        elif choice == "5":
            library.show_all()

        elif choice == "6":
            print("系统已退出！")
            break

        else:
            print("输入有误，请重新选择！")
    except ValueError:
        print("输入值错误，请输入1~6以内的选项")
    except Exception:
        print("输入值错误，请检查后重试")

if __name__ == "__main__":
    main()