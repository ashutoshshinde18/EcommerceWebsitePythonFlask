
class Mobiles():
    def __init__(self,id=0,name=' ',brand=' ',price=0,ram=' ',internalstorage=' ',simtype=' ',customerratings=0,image=None,category=' '):
        self.mobId = id
        self.mobName = name
        self.mobBrand = brand
        self.mobPrice = price
        self.mobRAM = ram
        self.mobInternalStorage = internalstorage
        self.mobSIMType = simtype
        self.mobCustomerRatings= customerratings
        self.mobImage = image
        self.mobCategory = category
    def __repr__(self):
        return f'Mobiles[{self.mobId},{self.mobName},{self.mobBrand},{self.mobPrice},{self.mobRAM},{self.mobInternalStorage},{self.mobSIMType},{self.mobCustomerRatings},{self.mobImage},{self.mobCategory}]'


class Fashion():
    def __init__(self,id=0,name=' ',brand=' ',price=0,gender=' ',size=' ',color=' ',customerratings=0,image=None,category=' '):
        self.fashId = id
        self.fashName = name
        self.fashBrand = brand
        self.fashPrice = price
        self.fashGender = gender
        self.fashSize = size
        self.fashColor = color
        self.fashCustomerRatings= customerratings
        self.fashImage = image
        self.fashCategory = category
    def __repr__(self):
        return f'Fashion[{self.fashId},{self.fashName},{self.fashBrand},{self.fashPrice},{self.fashGender},{self.fashSize},{self.fashColor},{self.fashCustomerRatings},{self.fashImage},{self.fashCategory}]'


class Electronics():
    def __init__(self,id=0,name=' ',brand=' ',price=0,wiredwireless=' ',size=' ',color=' ',customerratings=0,image=None,category=' '):
        self.eleId = id
        self.eleName = name
        self.eleBrand = brand
        self.elePrice = price
        self.eleWiredWireless = wiredwireless
        self.eleSize = size
        self.eleColor = color
        self.eleCustomerRatings= customerratings
        self.eleImage = image
        self.eleCategory = category
    def __repr__(self):
        return f'Electronics[{self.eleId},{self.eleName},{self.eleBrand},{self.elePrice},{self.elewiredwireless},{self.eleSize},{self.eleColor},{self.eleCustomerRatings},{self.eleImage},{self.eleCategory}]'


