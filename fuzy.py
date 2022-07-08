
class BentukAlbum():
    kotak = 30
    bulat = 20
    persegipanjang = 60

    def turun(self, x):
        if x <= self.kotak:
            return 0
        elif x >= self.bulat:
            return 1
        else:
            return bawah(x, self.bulat, self.kotak)

    def pas(self, x):
        if self.kotak < x < self.bulat:
            return atas(x, self.kotak, self.bulat)
        elif self.bulat < x < self.persegipanjang:
            return bawah(x, self.bulat, self.persegipanjang)
        elif x == self.bulat:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.bulat:
            return 1
        elif x <= self.persegipanjang:
            return 0
        else:
            return up(x, self.persegipanjang, self.bulat)

class teksturAlbum():
    halus = 40
    kasar = 20
    jelas = 30

    def sedikit(self, x):
        if x >= self.halus:
            return 0
        elif x <= self.kasar:
            return 1
        else:
            return down(x, self.kasar, self.halus)
    
    def cukup(self, x):
        if self.halus < x < self.kasar:
            return up(x, self.halus, self.kasar)
        elif self.kasar < x < self.jelas:
            return down(x, self.kasar, self.jelas)
        elif x == self.kasar:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.jelas:
            return 1
        elif x <= self.kasar:
            return 0
        else:
            return up(x, self.kasar, self.jelas)

class WarnaAlbum():
    putih = 50
    hitam = 40
    pink = 80

    def sedikit(self, x):
        if x >= self.hitam:
            return 0
        elif x <= self.putih:
            return 1
        else:
            return down(x, self.putih, self.hitam)
    
    def cukup(self, x):
        if self.putih < x < self.hitam:
            return up(x, self.hitam, self.putih)
        elif self.putih < x < self.pink:
            return down(x, self.putih, self.pink)
        elif x == self.putih:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.pink:
            return 1
        elif x <= self.putih:
            return 0
        else:
            return up(x, self.putih, self.pink)

class versiAlbum():
    repackage = 30
    lunatic = 50
    holiday1 = 70
   
    def sedikit(self, x):
        if x >= self.lunatic:
            return 0
        elif x <= self.repackage:
            return 1
        else:
            return down(x, self.repackage, self.lunatic)
    
    def cukup(self, x):
        if self.repackage < x < self.lunatic:
            return up(x, self.repackage, self.lunatic)
        elif self.repackage < x < self.holiday1:
            return down(x, self.lunatic, self.holiday1)
        elif x == self.lunatic:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.holiday1:
            return 1
        elif x <= self.lunatic:
            return 0
        else:
            return up(x, self.lunatic, self.holiday1)
