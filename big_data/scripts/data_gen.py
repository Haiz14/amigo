from faker import Faker

class NumericalData:
    def __init__(self):
        self.fake = Faker()
        self.barcode_list = self.add_barcode_list()

    def add_barcode_list(self):
        barcode_list = [5]
        return barcode_list


if __name__ == "__main__":
    obj = NumericalData()
    print (obj.barcode_list)
