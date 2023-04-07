'''class Bill():
    def __init__(self, prev_read, cur_read):
        # YOUR CODE GOESS HERE
        self.prev_read = prev_read
        self.cur_read = cur_read

        self.units_consumed = self.cur_read - self.prev_read

    def total_bill(self):
        total = 0.0
        meter_charges = 150
        # YOUR CODE GOESS HERE
        if (self.units_consumed >= 200):
            total = float((100 * 3.5 + 100 * 5 + (self.units_consumed - 200) * 8 + meter_charges))
        if (self.units_consumed < 200 and self.units_consumed > 100):
            total = float((100 * 3.5 + (self.units_consumed - 100) * 5 + meter_charges))
        if (self.units_consumed < 100):
            total = float((self.units_consumed * 3.5 + meter_charges))
        print(total)
obj= Bill(200,650)
obj.total_bill()

'''
from datetime import date

a=2
b=3
c=2023
d=date(a,b,c)
print(d)