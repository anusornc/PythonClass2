# งานที่ 2
# กำหนดให้ชื่อรถคันที่ 1 คือ Toyota , สีแดง , เป็นปิคอัพ , ราคา 600000 บาท
# กำหนดให้ชื่อรถคันที่ 2 คือ Ferrari , สีดำ , เป็นรถเก๋ง , ราคา 1000000 บาท

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# เริ่มเขียนโค้ดด้านล่างนี้ -


# test code
print(car1.description())
print(car2.description())
