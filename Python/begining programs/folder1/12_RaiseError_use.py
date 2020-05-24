class Mobile:
    def __init__(self, mobile):
        self.mobile = mobile


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile_name):
        # self.mobile_name = mobile_name
        # self.mobiles.append(self.mobile_name)
        if isinstance(mobile_name, Mobile):
            self.mobiles.append(mobile_name)
        else:
            raise TypeError("Entered phone is not in Mobile class.")


oneplus = Mobile("OnePlus 5")
samsung = Mobile("Samsung Galaxy S9")
samsung1 = Mobile("Samsung Galaxy S10")
apple = Mobile("Apple Iphone 11 Pro")
# print(oneplus.mobile)
# print(samsung.mobile)

krishna_mobiles = MobileStore()
print(krishna_mobiles.mobiles)
krishna_mobiles.add_mobile(samsung)
print(krishna_mobiles.mobiles[0].mobile)
# krishna_mobiles.add_mobile(oneplus)
# print(krishna_mobiles.mobiles)
