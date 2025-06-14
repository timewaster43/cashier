import tkinter as tk
from tkinter import messagebox
import datetime

class CashRegister:
    def __init__(self, root):

        self.log_route = "cash.txt"

        self.time = str(datetime.date.today())
        file_handle=open(self.log_route,mode='a')
        file_handle.writelines("----------------\n")
        file_handle.writelines(self.time+"\n")
        file_handle.writelines("----------------\n")
        file_handle.close()

        self.count = 1

        self.root = root
        self.root.title("收银台程序")

        self.cart = {}
        self.total_amount = 0.0

        self.cart_label = tk.Label(root, text="当\n前\n购\n物\n车", font=(2))
        self.cart_label.pack(side = "left")

        self.cart_listbox = tk.Listbox(root, height = 80, width = 24, font=(0.1))
        self.cart_listbox.pack(side = "left")

        self.product_label = tk.Label(root, text="可\n选\n商\n品", font=(2))
        self.product_label.pack(side = "right")

        self.product_listbox = tk.Listbox(root, height = 80, width = 24, font=(0.1))
        self.product_listbox.pack(side = "right")

        self.checkout_button = tk.Button(root, text="结算", command=self.checkout, height = 3, width = 10, font=(3))
        self.checkout_button.pack(side = "bottom")

        self.clear_cart_button = tk.Button(root, text="清除购物车", command=self.clear, height = 3, width = 10, font=(3))
        self.clear_cart_button.pack(side = "bottom")

        self.add_to_cart_button = tk.Button(root, text="加入购物车", command=self.add_to_cart, height = 3, width = 10, font=(3))
        self.add_to_cart_button.pack(side = "bottom")

        self.current_cart_amount_label = tk.Label(root, text="当前购物车总金额: 0.00", font=(1))
        self.current_cart_amount_label.pack(side = "top")

        self.total_amount_label = tk.Label(root, text="总金额: 0.00", font=(1))
        self.total_amount_label.pack(side = "top")

        self.current_count_label = tk.Label(root, text="\n接下来的号码：1", font=(1))
        self.current_count_label.pack(side = "top")

        self.products = {
            "生椰拿铁": 16.0,
            "鸳鸯拿铁": 15.0,
            "芒着开心": 15.0,
            "莓有烦恼": 15.0,
            "轻尘冰粉": 15.0,
            "抹茶冰沙": 18.0,
            "巧克力冰沙": 18.0,
            "暗黑森林": 19.0,
            "意式浓缩": 8.0,
            "美式": 9.0,
            "拿铁": 10.0,
            "摩卡": 15.0,
            "香草拿铁": 15.0,
            "焦糖玛奇朵": 15.0,
            "抹茶拿铁": 12.0,
            "奶茶拿铁": 12.0,
            "可可": 10.0,
            "柚子茶": 8.0,
            "黑糖牛奶冰粉": 8.0,
            "玫瑰牛奶冰粉": 12.0,
            "芒果思慕雪": 20.0,
            "草莓思慕雪": 20.0,
            "生酪拿铁": 17.0,
            "暴打柠檬茶": 15.0,
            "蓝海星辰": 20.0,
            "乌云盖雪": 20.0,
        }


        for product_name in self.products.keys():
            self.product_listbox.insert(tk.END, f"{product_name}: ￥{self.products[product_name]:.2f}")

    def add_to_cart(self):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if selected_product:
            price = float(selected_product.split(": ￥")[1])
            self.cart[selected_product] = price
            self.cart_listbox.insert(tk.END, selected_product)
            self.update_amount_labels()

    def checkout(self):
        if self.cart:
            cart_contents = "\n".join(self.cart.keys())
            messagebox.showinfo("结算信息", f"结算购物车内容:\n{cart_contents}\n\n总金额: {self.update_amount_labels():.2f}\n\n号码牌：{self.count}")
            file_handle=open(self.log_route,mode='a')
            file_handle.writelines(str(self.count)+"号："+cart_contents+"\n")
            file_handle.close()
            self.total_amount += self.update_amount_labels()
            self.cart.clear()
            self.cart_listbox.delete(0, tk.END)
            self.update_amount_labels()
            self.count += 1
        else:
            messagebox.showerror("错误","购物车为空")

    def update_amount_labels(self):
        current_cart_amount = sum(self.cart.values())
        self.current_cart_amount_label.config(text=f"当前购物车总金额: {current_cart_amount:.2f}")
        self.total_amount_label.config(text=f"总金额: {self.total_amount:.2f}")
        self.current_count_label.config(text=f"\n接下来的号码：{self.count}")
        return current_cart_amount

    def clear(self):
        result = messagebox.askokcancel('清空购物车', '是否确认清空购物车?')
        if result == True:
            self.cart.clear()
            self.cart_listbox.delete(0, tk.END)
            self.update_amount_labels()


if __name__ == "__main__":
    root = tk.Tk()
    app = CashRegister(root)
    root.mainloop()
