# class SmartPhone:
#     def __init__(self,model,sim_cards,battery):
#         self.model = "mers"
#         self.model = model
#         self.sim_cards = sim_cards
#         self.battery = battery
#     def info(self):
#         print(f"Бренд-{self.model},сим карты-{self.sim_cards},бфтарейка-{self.battery}")
#     def gellery(self):
#         print("Фотографии")
#     def password(self):
#         print("1242534457569")    
# mi =SmartPhone("note 10",["megacom","O"],"500 Mach")
# mi.info()

# def private(value):
#     def test():
#         print("Hello")
#         value()
#         print("bay!")
#     return test
# @private
# def hello():
#     print("hi")
# hello()    
import math

a1 = 0.5
a5 = 32

# Находим знаменатель прогрессии
r = math.pow(a5 / a1, 1/4)

# Находим промежуточные члены
a2 = a1 * r
a3 = a1 * r**2
a4 = a1 * r**3

print(f"a2 = {a2}, a3 = {a3}, a4 = {a4}")
print(f"Знаменатель прогрессии r = {r}")


 

print
