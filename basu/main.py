# main.py
# インスタンスメソッド化（初期化）
class BusTime:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def bus(self):
    # 登校するか下校するかの確認
    print("登校しますか？下校しますか？")
    self.x = int(input("1.登校 2.下校"))
    # 市バスを利用するかプリンセスバスを利用するかの確認
    print("市バスを利用しますか？プリンセスバスを利用しますか？")
    self.y = int(input("1.市バス 2.プリンセスバス"))

    # 市バスで登校
    if self.x == 1 and self.y == 1:
      import sity_bus1
      sb1 = sity_bus1.sity_bus1(self.z)
      return sb1
    # 市バスで下校
    elif self.x == 2 and self.y == 1:
      import sity_bus2
      sb2 = sity_bus2.sity_bus2()
      return sb2
    # プリンセスバスで登校
    elif self.x == 1 and self.y == 2:
      import princess_bus1
      pb1 = princess_bus1.princess_bus1(self.z)
      return pb1
    # プリンセスバスで下校
    elif self.x == 2 and self.y == 2:
      import princess_bus2
      pb2 = princess_bus2.princess_bus2()
      return pb2
    else:
      print("----------ERROR----------")
      return "----------ERROR----------"

      
bustime = BusTime(0,0,5)
bustime.bus()
