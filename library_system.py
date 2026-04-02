class Book:
    def __init__(self, name, author, isbn, stock):
        self.name = name
        self.author = author
        self.__isbn = isbn
        self.stock = stock

    def get_isbn(self):
        return self.__isbn
    
    def update_stock(self, new_stock): # 修改库存（num可正 / 负，代表入库 / 出库，库存不能小于 0，需加校验）
        self.stock = new_stock
        if self.stock < 0:
            print("库存不能小于 0")
            self.stock = 0
        else:
            print(f"库存更新为 {self.stock}")
        return self.stock
    


        
        