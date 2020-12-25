import pandas as pd
import  random
class Rw:
    def __init__(self):
        self.save = pd.read_csv("G:\disktop\人员名单.csv",encoding="gbk")
        self.len = self.save.index
        print(self.len.stop)
        print(self.save.columns)
        # print(self.save)
        # self.Readcsv()
        # self.mains(2)
    def mains(self, n):
        self.lockys = self.save.sample(n, replace=False, axis=0)
        print(self.lockys)
        self.save = self.save.drop(self.lockys.index)
        print("*********************")
        print(self.save)

    # def main(self,n):
    #     #     liston  = list(range(1,self.len.stop+1))
    #     #     self.rands = random.sample(liston,n)
    #     #     print(self.rands)
    #     #     for i in self.rands:
    #     #         print(self.save.)
    #     #     # self.rand = random.randrange(1,self.len.stop,1)




mainss = Rw()
mainss.mains(1)
print("&&&&&&&&&&&&&&&&&&&&&&")
mainss.mains(2)
print("&&&&&&&&&&&&&&&&&&&&&&")
mainss.mains(2)
print("&&&&&&&&&&&&&&&&&&&&&&")
mainss.mains(2)
print("&&&&&&&&&&&&&&&&&&&&&&")
mainss.mains(2)

