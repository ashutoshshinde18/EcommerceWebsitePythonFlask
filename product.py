from flask import Flask,render_template,redirect,request,url_for
import database as db
from model import Mobiles
from model import Fashion
from model import Electronics
app = Flask(__name__)
import os


# home.html page
@app.route("/")
def home():
    return render_template('index.html')

#show mobiles product
@app.route("/showmobilesproduct")
def showmobilesproduct():
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproduct.html',moblist=moblist)

@app.route("/showfashionproduct")
def showfashionproduct():
    fashlist = db.showFashionProduct()
    return render_template('showfashionproduct.html',fashlist=fashlist)

@app.route("/showelectronicsproduct")
def showelectronicsproduct():
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproduct.html',elelist=elelist)


@app.route('/addmobilesproduct')
def addmobilesproduct():
    mob = Mobiles()
    return render_template('addmobilesproduct.html',mob=mob,action='Add')

@app.route('/addfashionproduct')
def addfashionproduct():
    fash = Fashion()
    return render_template('addfashionproduct.html',fash=fash,action='Add')

@app.route('/addelectronicsproduct')
def addelectronicsproduct():
    ele = Electronics()
    return render_template('addelectronicsproduct.html',ele=ele,action='Add')


@app.route('/savemobilesproduct',methods=['POST'])
def savemobilesproduct():
    name = request.form['mobName']
    brand = request.form['mobBrand']
    price = request.form['mobPrice']
    ram = request.form['mobRAM']
    internalstorage = request.form['mobInternalStorage']
    simtype = request.form['mobSIMType']
    customerratings =request.form['mobCustomerRatings']
    imagefile = request.files['mobImage']
    imagename = imagefile.filename
    path = os.path.join('static\\img',imagename)
    imagefile.save(path)
    category = request.form['mobCategory']
    mob = Mobiles(name=name,brand=brand,price=price,ram=ram,internalstorage=internalstorage,simtype=simtype,customerratings=customerratings,image=imagename,category=category)
    db.saveMobilesProduct(mob)
    return redirect('/showmobilesproduct')

@app.route('/savefashionproduct',methods=['POST'])
def savefashionproduct():
    name = request.form['fashName']
    brand = request.form['fashBrand']
    price = request.form['fashPrice']
    gender = request.form['fashGender']
    size = request.form['fashSize']
    color = request.form['fashColor']
    customerratings =request.form['fashCustomerRatings']
    imagefile = request.files['fashImage']
    imagename = imagefile.filename
    path = os.path.join('static\\img',imagename)
    imagefile.save(path)
    category = request.form['fashCategory']
    fash = Fashion(name=name,brand=brand,price=price,gender=gender,size=size,color=color,customerratings=customerratings,image=imagename,category=category)
    db.saveFashionProduct(fash)
    return redirect('/showfashionproduct')

@app.route('/saveelectronicsproduct',methods=['POST'])
def saveelectronicsproduct():
    name = request.form['eleName']
    brand = request.form['eleBrand']
    price = request.form['elePrice']
    wiredwireless = request.form['eleWiredWireless']
    size = request.form['eleSize']
    color = request.form['eleColor']
    customerratings = request.form['eleCustomerRatings']
    imagefile = request.files['eleImage']
    imagename = imagefile.filename
    path = os.path.join('static\\img',imagename)
    imagefile.save(path)
    category = request.form['eleCategory']
    ele = Electronics(name=name,brand=brand,price=price,wiredwireless=wiredwireless,size=size,color=color,customerratings=customerratings,image=imagename,category=category)
    db.saveElectronicsProduct(ele)
    return redirect('/showelectronicsproduct')

@app.route('/deletemobilesproduct/<int:mobId>')
def deletemobilesproduct(mobId):
    db.deleteMobilesProduct(mobId)
    return redirect('/showmobilesproduct')

@app.route('/deletefashionproduct/<int:fashId>')
def deletefashionproduct(fashId):
    db.deleteFashionProduct(fashId)
    return redirect('/showfashionproduct')

@app.route('/deleteelectronicsproduct/<int:eleId>')
def deleteelectronicsproduct(eleId):
    db.deleteElectronicsProduct(eleId)
    return redirect('/showelectronicsproduct')

@app.route('/editmobilesproduct/<int:mobId>')
def editmobilesproduct(mobId):
    mob = db.getMobilesProductById(mobId)
    return render_template('addmobilesproduct.html',mob=mob,action='Edit')

@app.route('/updatemobilesproduct',methods=['POST'])
def updatemobilesproduct():
    id = request.form['mobId']
    name = request.form['mobName']
    brand = request.form['mobBrand']
    price = request.form['mobPrice']
    ram = request.form['mobRAM']
    internalstorage = request.form['mobInternalStorage']
    simtype = request.form['mobSIMType']
    customerratings = request.form['mobCustomerRatings']
    imagefile = request.files['mobImage']
    imagename = imagefile.filename
    path = os.path.join('static\\img',imagename)
    imagefile.save(path)
    category = request.form['mobCategory']
    mob = Mobiles(id=id,name=name,brand=brand,price=price,ram=ram,internalstorage=internalstorage,simtype=simtype,customerratings=customerratings,image=imagename,category=category)
    db.updateMobilesProduct(id,mob)
    return redirect('/showmobilesproduct')
    
@app.route('/editfashionproduct/<int:fashId>')
def editfashionproduct(fashId):
    fash = db.getFashionProductById(fashId)
    return render_template('addfashionproduct.html',fash=fash,action='Edit')

@app.route('/updatefashionproduct',methods=['POST'])
def updatefashionproduct():
    id = request.form['fashId']
    name = request.form['fashName']
    brand = request.form['fashBrand']
    price = request.form['fashPrice']
    gender = request.form['fashGender']
    size = request.form['fashSize']
    color = request.form['fashColor']
    customerratings = request.form['fashCustomerRatings']
    imagefile = request.files['fashImage']
    imagename = imagefile.filename
    path = os.path.join('static\\img',imagename)
    imagefile.save(path)
    category = request.form['fashCategory']
    fash = Fashion(id=id,name=name,brand=brand,price=price,gender=gender,size=size,color=color,customerratings=customerratings,image=imagename,category=category)
    db.updateFashionProduct(id,fash)
    return redirect('/showfashionproduct')

@app.route('/editelectronicsproduct/<int:eleId>')
def editelectronicsproduct(eleId):
    ele = db.getElectronicsProductById(eleId)
    return render_template('addelectronicsproduct.html',ele=ele,action='Edit')

@app.route('/updateelectronicsproduct',methods=['POST'])
def updateelectronicsproduct():
    id = request.form['eleId']
    name = request.form['eleName']
    brand = request.form['eleBrand']
    price = request.form['elePrice']
    wiredwireless = request.form['eleWiredWireless']
    size = request.form['eleSize']
    color = request.form['eleColor']
    customerratings = request.form['eleCustomerRatings']
    imagefile = request.files['eleImage']
    imagename = imagefile.filename
    path = os.path.join('static\\img',imagename)
    imagefile.save(path)
    category = request.form['eleCategory']
    ele = Electronics(id=id,name=name,brand=brand,price=price,wiredwireless=wiredwireless,size=size,color=color,customerratings=customerratings,image=imagename,category=category)
    db.updateElectronicsProduct(id,ele)
    return redirect('/showelectronicsproduct')


@app.route('/searchmobilesby')
def searchmobilesby():
    return render_template('searchmobilesby.html')

@app.route('/showmobilesproductbyid',methods=['POST'])
def showmobilesproductbyid():
    id = int(request.form['mobId'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbyid.html',moblist=moblist,id=id)
    

@app.route('/showmobilesproductbyname',methods=['POST'])
def showmobilesproductbyname():
    name = str(request.form['mobName'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbyname.html',moblist=moblist,name=name)

@app.route('/showmobilesproductbybrand',methods=['POST'])
def showmobilesproductbybrand():
    brand = str(request.form['mobBrand'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbybrand.html',moblist=moblist,brand=brand)    

@app.route('/showmobilesproductbyprice',methods=['POST'])
def showmobilesproductbyprice():
    price = float(request.form['mobPrice'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbyprice.html',moblist=moblist,price=price)  
   
@app.route('/showmobilesproductbyram',methods=['POST'])
def showmobilesproductbyram():
    ram = str(request.form['mobRAM'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbyram.html',moblist=moblist,ram=ram)  

@app.route('/showmobilesproductbyinternalstorage',methods=['POST'])
def showmobilesproductbyinternalstorage():
    internalstorage = str(request.form['mobInternalStorage'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbyinternalstorage.html',moblist=moblist,internalstorage=internalstorage)  

@app.route('/showmobilesproductbysimtype',methods=['POST'])
def showmobilesproductbysimtype():
    simtype = str(request.form['mobSIMType'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbysimtype.html',moblist=moblist,simtype=simtype)  

@app.route('/showmobilesproductbycustomerratings',methods=['POST'])
def showmobilesproductbycustomerratings():
    customerratings = float(request.form['mobCustomerRatings'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbycustomerratings.html',moblist=moblist,customerratings=customerratings)   

@app.route('/showmobilesproductbycategory',methods=['POST'])
def showmobilesproductbycategory():
    category = str(request.form['mobCategory'])
    moblist = db.showMobilesProduct()
    return render_template('showmobilesproductbycategory.html',moblist=moblist,category=category)  


#search by fashion

@app.route('/searchfashionby')
def searchfashionby():
    return render_template('searchfashionby.html')

@app.route('/showfashionproductbyid',methods=['POST'])
def showfashionproductbyid():
    id = int(request.form['fashId'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbyid.html',fashlist=fashlist,id=id)
    

@app.route('/showfashionproductbyname',methods=['POST'])
def showfashionproductbyname():
    name = str(request.form['fashName'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbyname.html',fashlist=fashlist,name=name)

@app.route('/shofashionproductbybrand',methods=['POST'])
def showfashionproductbybrand():
    brand = str(request.form['fashBrand'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbybrand.html',fashlist=fashlist,brand=brand)    

@app.route('/showfashionproductbyprice',methods=['POST'])
def showfashionproductbyprice():
    price = float(request.form['fashPrice'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbyprice.html',fashlist=fashlist,price=price)  
   
@app.route('/showfashionproductbygender',methods=['POST'])
def showfashionproductbygender():
    gender = str(request.form['fashGender'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbygender.html',fashlist=fashlist,gender=gender)  

@app.route('/showfashionproductbysize',methods=['POST'])
def showfashionproductbysize():
    size = str(request.form['fashSize'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbysize.html',fashlist=fashlist,size=size)  

@app.route('/showfashionproductbycolor',methods=['POST'])
def showfashionproductbycolor():
    color = str(request.form['fashColor'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbycolor.html',fashlist=fashlist,color=color)  

@app.route('/showfashionproductbycustomerratings',methods=['POST'])
def showfashionproductbycustomerratings():
    customerratings = float(request.form['fashCustomerRatings'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbycustomerratings.html',fashlist=fashlist,customerratings=customerratings)   

@app.route('/showfashionproductbycategory',methods=['POST'])
def showfashionproductbycategory():
    category = str(request.form['fashCategory'])
    fashlist = db.showFashionProduct()
    return render_template('showfashionproductbycategory.html',fashlist=fashlist,category=category)  


#electronics search by

@app.route('/searchelectronicsby')
def searchelectronicsby():
    return render_template('searchelectronicsby.html')

@app.route('/showelectronicsproductbyid',methods=['POST'])
def showelectronicsproductbyid():
    id = int(request.form['eleId'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbyid.html',elelist=elelist,id=id)
    

@app.route('/showelectronicsproductbyname',methods=['POST'])
def showelectronicsproductbyname():
    name = str(request.form['eleName'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbyname.html',elelist=elelist,name=name)

@app.route('/showelectronicsproductbybrand',methods=['POST'])
def showelectronicsproductbybrand():
    brand = str(request.form['eleBrand'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbybrand.html',elelist=elelist,brand=brand)    

@app.route('/showelectronicsproductbyprice',methods=['POST'])
def showelectronicsproductbyprice():
    price = float(request.form['fashPrice'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbyprice.html',elelist=elelist,price=price)  
   
@app.route('/showelectronicsproductbywiredwireless',methods=['POST'])
def showelectronicsproductbywiredwireless():
    wiredwireless = str(request.form['eleWiredWireless'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbywiredwireless.html',elelist=elelist,wiredwireless=wiredwireless)  

@app.route('/showelectronicsproductbysize',methods=['POST'])
def showelectronicsproductbysize():
    size = str(request.form['eleSize'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbysize.html',elelist=elelist,size=size)  

@app.route('/showelectronicsproductbycolor',methods=['POST'])
def showelectronicsproductbycolor():
    color = str(request.form['eleColor'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbycolor.html',elelist=elelist,color=color)  

@app.route('/showelectronicsproductbycustomerratings',methods=['POST'])
def showelectronicsproductbycustomerratings():
    customerratings = float(request.form['eleCustomerRatings'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbycustomerratings.html',elelist=elelist,customerratings=customerratings)   

@app.route('/showelectronicsproductbycategory',methods=['POST'])
def showelectronicsproductbycategory():
    category = str(request.form['eleCategory'])
    elelist = db.showElectronicsProduct()
    return render_template('showelectronicsproductbycategory.html',elelist=elelist,category=category)  

#sort product by
@app.route('/sortmobilesbyprice')
def sortmobilesbyprice():
    moblist = db.showMobilesProduct()
    moblist.sort(key = lambda a:a.mobPrice)
    return render_template('showmobilesproduct.html',moblist=moblist)

@app.route('/sortmobilesbycustomerratings')
def sortmobilesbycustomerratings():
    moblist = db.showMobilesProduct()
    moblist.sort(key = lambda a:a.mobCustomerRatings)
    return render_template('showmobilesproduct.html',moblist=moblist)

@app.route('/sortfashionbyprice')
def sortfashionbyprice():
    fashlist = db.showFashionProduct()
    fashlist.sort(key = lambda a:a.fashPrice)
    return render_template('showfashionproduct.html',fashlist=fashlist)

@app.route('/sortfashionbycustomerratings')
def sortfashionbycustomerratings():
    fashlist = db.showFashionProduct()
    fashlist.sort(key = lambda a:a.fashCustomerRatings)
    return render_template('showfashionproduct.html',fashlist=fashlist)

@app.route('/sortelectronicsbyprice')
def sortelectronicsbyprice():
    elelist = db.showElectronicsProduct()
    elelist.sort(key = lambda a:a.elePrice)
    return render_template('showelectronicsproduct.html',elelist=elelist)

@app.route('/sortelectronicsbycustomerratings')
def sortelectronicsbycustomerratings():
    elelist = db.showElectronicsProduct()
    elelist.sort(key = lambda a:a.eleCustomerRatings)
    return render_template('showelectronicsproduct.html',elelist=elelist)
if __name__=='__main__':
    app.run(debug=True)

