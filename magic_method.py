class page:
    def __init__(self,total,index=1):
        self.total=total
        self.index=index
        self.per_page=10
    def main_page(self):
        print("这是主页")


main = page(1)
print(dir(main))
