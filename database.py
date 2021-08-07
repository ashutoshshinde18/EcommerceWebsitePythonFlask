from model import Mobiles
from model import Fashion
from model import Electronics
import pymysql

con = pymysql.connect(host='localhost',user='root',passwd=' ',db='pythonproject')

cursor = con.cursor()

# def showProduct():
#     prolist = []
#     try:
#         sqlquery = 'select * from products'
#         cursor.execute(sqlquery)
#         rows = cursor.fetchall()
#         con.commit()
#         for row in rows:
#             pro = Ecommerce(row[0],row[1],row[2],row[3],row[4],row[5])
#             prolist.append(pro)
#         return prolist
#     except Exception as e:
#         print(e)

def showMobilesProduct():
    moblist = []
    try:
        sqlquery = 'select * from mobiles'
        cursor.execute(sqlquery)
        rows = cursor.fetchall()
        con.commit()
        for row in rows:
            mob = Mobiles(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
            moblist.append(mob)
        return moblist
    except Exception as e:
        print(e)

def showFashionProduct():
    fashlist = []
    try:
        sqlquery = 'select * from fashion'
        cursor.execute(sqlquery)
        rows = cursor.fetchall()
        con.commit()
        for row in rows:
            fash = Fashion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
            fashlist.append(fash)
        return fashlist
    except Exception as e:
        print(e)
    

def showElectronicsProduct():
    elelist = []
    try:
        sqlquery = 'select * from electronics'
        cursor.execute(sqlquery)
        rows = cursor.fetchall()
        con.commit()
        for row in rows:
            ele = Electronics(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
            elelist.append(ele)
        return elelist
    except Exception as e:
        print(e)

def saveMobilesProduct(mob):
    try:
        sqlquery = 'insert into mobiles(mobName,mobBrand,mobPrice,mobRAM,mobInternalStorage,mobSIMType,mobCustomerRatings,mobImage,mobCategory) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sqlquery,(mob.mobName,mob.mobBrand,mob.mobPrice,mob.mobRAM,mob.mobInternalStorage,mob.mobSIMType,mob.mobCustomerRatings,mob.mobImage,mob.mobCategory))
        con.commit()
    except Exception as e:
        print(e)

def saveFashionProduct(fash):
    try:
        sqlquery = 'insert into fashion(fashName,fashBrand,fashPrice,fashGender,fashSize,fashColor,fashCustomerRatings,fashImage,fashCategory) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sqlquery,(fash.fashName,fash.fashBrand,fash.fashPrice,fash.fashGender,fash.fashSize,fash.fashColor,fash.fashCustomerRatings,fash.fashImage,fash.fashCategory))
        con.commit()
    except Exception as e:
        print(e)


def saveElectronicsProduct(ele):
    try:
        sqlquery = 'insert into electronics(eleName,eleBrand,elePrice,eleWiredWireless,eleSize,eleColor,eleCustomerRatings,eleImage,eleCategory) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sqlquery,(ele.eleName,ele.eleBrand,ele.elePrice,ele.eleWiredWireless,ele.eleSize,ele.eleColor,ele.eleCustomerRatings,ele.eleImage,ele.eleCategory))
        con.commit()
    except Exception as e:
        print(e)

def deleteMobilesProduct(id):
    try:
        sqlquery = 'delete from mobiles where mobId=%s'
        cursor.execute(sqlquery,(id))
        con.commit()
    except Exception as e:
        print(e)

def deleteFashionProduct(id):
    try:
        sqlquery = 'delete from fashion where fashId=%s'
        cursor.execute(sqlquery,(id))
        con.commit()
    except Exception as e:
        print(e)

def deleteElectronicsProduct(id):
    try:
        sqlquery = 'delete from electronics where eleId=%s'
        cursor.execute(sqlquery,(id))
        con.commit()
    except Exception as e:
        print(e)

def getMobilesProductById(id):
    try:
        sqlquery = 'select * from mobiles where mobId=%s'
        cursor.execute(sqlquery,(id))
        row = cursor.fetchone()
        con.commit()
        mob = Mobiles(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        return mob
    except Exception as e:
        print(e)
     
def updateMobilesProduct(id,mob):
    try:
        sqlquery = 'update mobiles set mobName=%s,mobBrand=%s,mobPrice=%s,mobRAM=%s,mobInternalStorage=%s,mobSIMType=%s,mobCustomerRatings=%s,mobImage=%s,mobCategory=%s where mobId=%s'
        cursor.execute(sqlquery,(mob.mobName,mob.mobBrand,mob.mobPrice,mob.mobRAM,mob.mobInternalStorage,mob.mobSIMType,mob.mobCustomerRatings,mob.mobImage,mob.mobCategory,id))
        con.commit()
    except Exception as e:
        print(e)
        

def getFashionProductById(id):
    try:
        sqlquery = 'select * from fashion where fashId=%s'
        cursor.execute(sqlquery,(id))
        row = cursor.fetchone()
        con.commit()
        fash = Fashion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        return fash
    except Exception as e:
        print(e)
     
def updateFashionProduct(id,fash):
    try:
        sqlquery = 'update Fashion set fashName=%s,fashBrand=%s,fashPrice=%s,fashGender=%s,fashSize=%s,fashColor=%s,fashCustomerRatings=%s,fashImage=%s,fashCategory=%s where fashId=%s'
        cursor.execute(sqlquery,(fash.fashName,fash.fashBrand,fash.fashPrice,fash.fashGender,fash.fashSize,fash.fashColor,fash.fashCustomerRatings,fash.fashImage,fash.fashCategory,id))
        con.commit()
    except Exception as e:
        print(e)
        

def getElectronicsProductById(id):
    try:
        sqlquery = 'select * from electronics where eleId=%s'
        cursor.execute(sqlquery,(id))
        row = cursor.fetchone()
        con.commit()
        ele = Electronics(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        return ele
    except Exception as e:
        print(e)
     
def updateElectronicsProduct(id,ele):
    try:
        sqlquery = 'update electronics set eleName=%s,eleBrand=%s,elePrice=%s,eleWiredWireless=%s,eleSize=%s,eleColor=%s,eleCustomerRatings=%s,eleImage=%s,eleCategory=%s where eleId=%s'
        cursor.execute(sqlquery,(ele.eleName,ele.eleBrand,ele.elePrice,ele.eleWiredWireless,ele.eleSize,ele.eleColor,ele.eleCustomerRatings,ele.eleImage,ele.eleCategory,id))
        con.commit()
    except Exception as e:
        print(e)



def closeConnection():                                                               
    con.close()