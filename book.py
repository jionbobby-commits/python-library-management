
class Book:
    # 类属性：所有图书对象共享的类别信息
    category = "普通图书"

    def __init__(self, name, author, price, stock):
        # 实例属性：每本图书各自拥有的数据
        self.name = name
        self.author = author
        self.price = price
        self.stock = stock

    def show_info(self):
        print(
            f"书名：{self.name}，"
            f"作者：{self.author}，"
            f"价格：{self.price}，"
            f"库存：{self.stock}"
        )