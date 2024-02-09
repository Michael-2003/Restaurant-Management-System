from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from PIL import Image,ImageTk
root= Tk()
root.geometry("1520x780+0+0")

f1=Frame(root,height=780,width=190,bg="#3381bf")
f1.place(x=0,y=0)
f2=Frame(root,height=60,width=1520-190,bg="#3381bf")
f2.place(x=190,y=0)
ff=Frame(root,height=780-60,width=1520-190)
ff.place(x=190,y=60)
logoimg=ImageTk.PhotoImage(Image.open("logo.png"))
logolabel=Label(root,image=logoimg,height=70,width=170)
logolabel.place(x=8,y=-5)
img1=ImageTk.PhotoImage(Image.open("kood1.png"))
img2=ImageTk.PhotoImage(Image.open("kood2.png"))
img3=ImageTk.PhotoImage(Image.open("drinks1.png"))
img4=ImageTk.PhotoImage(Image.open("drinks2.png"))
img5=ImageTk.PhotoImage(Image.open("salad1.png"))
img6=ImageTk.PhotoImage(Image.open("salad2.png"))
img7=ImageTk.PhotoImage(Image.open("dessert1.png"))
img8=ImageTk.PhotoImage(Image.open("dessert2.png"))
img9=ImageTk.PhotoImage(Image.open("exit1.png"))
img10=ImageTk.PhotoImage(Image.open("exit2.png"))
img11=ImageTk.PhotoImage(Image.open("hback1.png"))
img12=ImageTk.PhotoImage(Image.open("hback2.png"))
homeimg1=ImageTk.PhotoImage(Image.open("home1.png"))
homeimg2=ImageTk.PhotoImage(Image.open("home2.png"))
profileimg1=ImageTk.PhotoImage(Image.open("profilewww.png"))
profileimg2=ImageTk.PhotoImage(Image.open("profilebbb.png"))
cartimg1=ImageTk.PhotoImage(Image.open("cart1.png"))
cartimg2=ImageTk.PhotoImage(Image.open("cart.png"))

cocacolaimg=ImageTk.PhotoImage(Image.open("cocacola.png"))
spriteimg=ImageTk.PhotoImage(Image.open("sprite.png"))
mirindaimg=ImageTk.PhotoImage(Image.open("mirinda.png"))
cocacola_zeroimg=ImageTk.PhotoImage(Image.open("cocacola_zero.png"))
fantaimg=ImageTk.PhotoImage(Image.open("hfanta.png"))
redbullimg=ImageTk.PhotoImage(Image.open("hredbull.png"))


addimg=ImageTk.PhotoImage(Image.open("add.png"))
bbq_pizza=ImageTk.PhotoImage(Image.open("hbq pizza 1.png"))
ransh_pizza=ImageTk.PhotoImage(Image.open("kransh pizza.png"))
vegetable_pizza=ImageTk.PhotoImage(Image.open("Roasted Vegetable Pizza.png"))
margretiaa_pizza=ImageTk.PhotoImage(Image.open("margretiaa.png"))
pep_pizza=ImageTk.PhotoImage(Image.open("pep2.png"))
maetlover_pizza=ImageTk.PhotoImage(Image.open("meatloverpizza.png"))




coleslaw_img=ImageTk.PhotoImage(Image.open("coleslaw.png"))
greensalad_img=ImageTk.PhotoImage(Image.open("greensalad.png"))
fattoush_img=ImageTk.PhotoImage(Image.open("fattoush.png"))
thousandIslandDressing_img=ImageTk.PhotoImage(Image.open("thousandIslandDressing.png"))
garlicdip_img=ImageTk.PhotoImage(Image.open("garlicdip.png"))
mixedbeans_img=ImageTk.PhotoImage(Image.open("mixedbeans.png"))





cheesecake_img=ImageTk.PhotoImage(Image.open("cheesecake.png"))
cinnabon_img=ImageTk.PhotoImage(Image.open("cinnabon.png"))
cupcake_img=ImageTk.PhotoImage(Image.open("cupcake.png"))
donat_img=ImageTk.PhotoImage(Image.open("donat.png"))
icecream_img=ImageTk.PhotoImage(Image.open("icecream.png"))
moltencake_img=ImageTk.PhotoImage(Image.open("moltencake.png"))

def home_home():
    homeframe=Frame(root,height=780-60,width=1520-190,bg="#ffffff")
    homeframe.place(x=190,y=60)
    # x=username.get()
    # homelabel=Label(homeframe,text=f"Welcome {x} to NU restuarant",font=("Bro",50),fg="#3381bf",bg="#ffffff")
    # homelabel.place(x=250,y=(780-60)/2-200)

    homelabel2=Label(homeframe,text=f",Wish You Like The Food",font=("Bro",50),fg="#3381bf",bg="#ffffff")
    homelabel2.place(x=250-2,y=(780-60)/2+150-100)


def food_food():
    
    foodframe=Frame(root,height=780-60,width=1520-190,bg="#ffffff")
    foodframe.place(x=190,y=60)
    

    pizza_bbq=Label(foodframe,image=bbq_pizza,height=200,width=350,bg="#ffffff")
    pizza_bbq.place(x=220.5+5-190,y=90.5-60)


    pizza_bbq_name=Label(foodframe,text="Chicken BBQ Pizza",width=50,bg="#ffffff")##name
    pizza_bbq_name.place(x=220.5+5-190,y=90.5-60+200+20)    
    
    bbq_price=Label(foodframe,text="70 LE",width=50,bg="#ffffff")##price
    bbq_price.place(x=220.5+5-190,y=90.5-60+200+20+20)

    pizza_vegetable=Label(foodframe,image=vegetable_pizza,height=200,width=350,bg="#ffffff")
    pizza_vegetable.place(x=678+5-190,y=90.5-60)

    pizza_vegetable_name=Label(foodframe,text="Vegetable Pizza",width=50,bg="#ffffff")##name
    pizza_vegetable_name.place(x=678+5-190,y=90.5-60+200+20)    
    
    pizza_vegetable_price=Label(foodframe,text="60 LE",width=50,bg="#ffffff")##price
    pizza_vegetable_price.place(x=678+5-190,y=90.5-60+200+20+20)

    pizza_margretiaa=Label(foodframe,image=margretiaa_pizza,height=200,width=350,bg="#ffffff")
    pizza_margretiaa.place(x=1135.5+5-190,y=90.5-60)

    pizza_margretiaa_name=Label(foodframe,text="Margherita Pizza",width=50,bg="#ffffff")##name
    pizza_margretiaa_name.place(x=1135.5+5-190,y=90.5-60+200+20)    
    
    pizza_margretiaa_price=Label(foodframe,text="60 LE",width=50,bg="#ffffff")##price
    pizza_margretiaa_price.place(x=1135.5+5-190,y=90.5-60+200+20+20)

    pizza_ransh=Label(foodframe,image=ransh_pizza,height=200,width=350,bg="#ffffff")
    pizza_ransh.place(x=220.5+5-190,y=418-60)

    pizza_ransh_name=Label(foodframe,text="Chicken Ransh Pizza",width=50,bg="#ffffff")##name
    pizza_ransh_name.place(x=220.5+5-190,y=575)    
    
    pizza_ransh_price=Label(foodframe,text="80 LE",width=50,bg="#ffffff")##price
    pizza_ransh_price.place(x=220.5+5-190,y=575+20)

    pizza_pep=Label(foodframe,image=pep_pizza,height=200,width=350,bg="#ffffff")
    pizza_pep.place(x=1135.5+5-190,y=418-60)

    pizza_pep_name=Label(foodframe,text="Pepperoni Pizza",width=50,bg="#ffffff")##name
    pizza_pep_name.place(x=1135.5+5-190,y=575)

    pizza_pep_price=Label(foodframe,text="75 LE",width=50,bg="#ffffff")##price
    pizza_pep_price.place(x=1135.5+5-190,y=575+20)

    pizza_meatlover=Label(foodframe,image=maetlover_pizza,height=200,width=350,bg="#ffffff")
    pizza_meatlover.place(x=678+5-190,y=418-60)

    pizza_meatlover_name=Label(foodframe,text="Meat Lover Pizza",width=50,bg="#ffffff")##name
    pizza_meatlover_name.place(x=678+5-190,y=575)

    pizza_meatlover_price=Label(foodframe,text="80 LE",width=50,bg="#ffffff")##price
    pizza_meatlover_price.place(x=678+5-190,y=575+20)

    def p_70_bbq():
        l.append(70)
        s.append("Chicken BBQ Pizza")
    
    def p_60_vege():
        l.append(60)
        s.append("Vegetable Pizza")

    def p_60_margretiaa():
        l.append(60)
        s.append("Margherita Pizza")
    
    def p_80_ransh():
        l.append(80)
        s.append("Chicken Ransh Pizza")
    
    def p_80_meatlover():
        l.append(80)
        s.append("Meat Lover Pizza") 
    
    def p_75_pep():
        l.append(75)
        s.append("Pepperoni Pizza")


    pizza_bbq_btn=Button(foodframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_70_bbq)
    pizza_bbq_btn.place(x=220.5+5-190+75,y=90.5+220)
    
    pizza_vegetable_btn=Button(foodframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_60_vege)
    pizza_vegetable_btn.place(x=678+5-190+75,y=90.5+220)
    
    pizza_margretiaa_btn=Button(foodframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_60_margretiaa)
    pizza_margretiaa_btn.place(x=1135.5+5-190+75,y=90.5+220)
    
    pizza_ransh_btn=Button(foodframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_80_ransh)
    pizza_ransh_btn.place(x=220.5+5-190+75,y=650.5-15)
    
    pizza_pep_btn=Button(foodframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_80_meatlover)
    pizza_pep_btn.place(x=678+5-190+75,y=650.5-15)
    
    pizza_meatlover_btn=Button(foodframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_75_pep)
    pizza_meatlover_btn.place(x=1135.5+5-190+75,y=650.5-15)




def drinks_drinks():
    drinksframe=Frame(root,height=780-60,width=1520-190,bg="#ffffff")
    drinksframe.place(x=190,y=60)

    cocacola=Label(drinksframe,image=cocacolaimg,height=200,width=350,bg="#ffffff")
    cocacola.place(x=220.5+5-190,y=90.5-60)

    cocacola_name=Label(drinksframe,text="CocaCola",width=50,bg="#ffffff")##name
    cocacola_name.place(x=220.5+5-190,y=90.5-60+200+20)
    
    cocacola_price=Label(drinksframe,text="10 LE",width=50,bg="#ffffff")##price
    cocacola_price.place(x=220.5+5-190,y=90.5-60+200+20+20)

    sprite=Label(drinksframe,image=spriteimg,height=200,width=350,bg="#ffffff")
    sprite.place(x=678+5-190,y=90.5-60)

    sprite_name=Label(drinksframe,text="Sprite",width=50,bg="#ffffff")##name
    sprite_name.place(x=678+5-190,y=90.5-60+200+20)    
    
    sprite_price=Label(drinksframe,text="10 LE",width=50,bg="#ffffff")##price
    sprite_price.place(x=678+5-190,y=90.5-60+200+20+20)

    mirinda=Label(drinksframe,image=mirindaimg,height=200,width=350,bg="#ffffff")
    mirinda.place(x=1135.5+5-190,y=90.5-60)

    mirinda_name=Label(drinksframe,text="Mirinda",width=50,bg="#ffffff")##name
    mirinda_name.place(x=1135.5+5-190,y=90.5-60+220)

    mirinda_price=Label(drinksframe,text="10 LE",width=50,bg="#ffffff")##price
    mirinda_price.place(x=1135.5+5-190,y=90.5-60+220+20)

    cocacola_zero=Label(drinksframe,image=cocacola_zeroimg,height=200,width=350,bg="#ffffff")
    cocacola_zero.place(x=220.5+5-190,y=418-60)

    cocacola_zero_name=Label(drinksframe,text="CocaCola Zero",width=50,bg="#ffffff")##name
    cocacola_zero_name.place(x=220.5+5-190,y=418-60+200+20)    
    
    cocacola_zero_price=Label(drinksframe,text="10 LE",width=50,bg="#ffffff")##price
    cocacola_zero_price.place(x=220.5+5-190,y=418-60+200+20+20)

    fanta=Label(drinksframe,image=fantaimg,height=200,width=350,bg="#ffffff")
    fanta.place(x=1135.5+5-190,y=418-60)

    fanta_name=Label(drinksframe,text="Fanta",width=50,bg="#ffffff")##name
    fanta_name.place(x=1135.5+5-190,y=575)

    fanta_price=Label(drinksframe,text="10 LE",width=50,bg="#ffffff")##price
    fanta_price.place(x=1135.5+5-190,y=575+20)

    redbull=Label(drinksframe,image=redbullimg,height=200,width=350,bg="#ffffff")
    redbull.place(x=678+5-190,y=418-60)

    redbull_name=Label(drinksframe,text="Redbull",width=50,bg="#ffffff")##name
    redbull_name.place(x=678+5-190,y=575)

    redbull_price=Label(drinksframe,text="30 LE",width=50,bg="#ffffff")##price
    redbull_price.place(x=678+5-190,y=575+20)

    def p_10_CocaCola():
        l.append(10)
        s.append("CocaCola")
    
    def p_10_Sprite():
        l.append(10)
        s.append("Sprite")

    def p_10_Mirinda():
        l.append(10)
        s.append("Mirinda")
    
    def p_10_CocaCola_Zero():
        l.append(10)
        s.append("CocaCola Zero")
    
    def p_30_Redbull():
        l.append(30)
        s.append("Redbull") 
    
    def p_10_Fanta():
        l.append(10)
        s.append("Fanta")


    cocacola_btn=Button(drinksframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_10_CocaCola)
    cocacola_btn.place(x=220.5+5-190+75,y=90.5+220)
    
    sprite_btn=Button(drinksframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_10_Sprite)
    sprite_btn.place(x=678+5-190+75,y=90.5+220)
    
    mirinda_btn=Button(drinksframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_10_Mirinda)
    mirinda_btn.place(x=1135.5+5-190+75,y=90.5+220)
    
    cocacola_zero_btn=Button(drinksframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_10_CocaCola_Zero)
    cocacola_zero_btn.place(x=220.5+5-190+75,y=650.5-15)
    
    fanta_btn=Button(drinksframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_10_Fanta)
    fanta_btn.place(x=678+5-190+75,y=650.5-15)
    
    redbull_btn=Button(drinksframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_30_Redbull)
    redbull_btn.place(x=1135.5+5-190+75,y=650.5-15)




def salad_salad():
    saladframe=Frame(root,height=780-60,width=1520-190,bg="#ffffff")
    saladframe.place(x=190,y=60)

    coleslaw=Label(saladframe,image=coleslaw_img,height=200,width=350,bg="#ffffff")
    coleslaw.place(x=220.5+5-190,y=90.5-60)

    coleslaw_name=Label(saladframe,text="Coleslaw",width=50,bg="#ffffff")##name
    coleslaw_name.place(x=220.5+5-190,y=90.5-60+200+20)    
    
    coleslaw_price=Label(saladframe,text="20 LE",width=50,bg="#ffffff")##price
    coleslaw_price.place(x=220.5+5-190,y=90.5-60+200+20+20)

    greensalad=Label(saladframe,image=greensalad_img,height=200,width=350,bg="#ffffff")
    greensalad.place(x=678+5-190,y=90.5-60)

    greensalad_name=Label(saladframe,text="Green Salad",width=50,bg="#ffffff")##name
    greensalad_name.place(x=678+5-190,y=90.5-60+200+20)    
    
    greensalad_price=Label(saladframe,text="15 LE",width=50,bg="#ffffff")##price
    greensalad_price.place(x=678+5-190,y=90.5-60+200+20+20)

    fattoush=Label(saladframe,image=fattoush_img,height=200,width=350,bg="#ffffff")
    fattoush.place(x=1135.5+5-190,y=90.5-60)
    
    fattoush_name=Label(saladframe,text="Fattoush",width=50,bg="#ffffff")##name
    fattoush_name.place(x=1135.5+5-190,y=90.5-60+200+20)  

    fattoush_price=Label(saladframe,text="25 LE",width=50,bg="#ffffff")##price
    fattoush_price.place(x=1135.5+5-190,y=90.5-60+200+20+20)

    thousandIslandDressing=Label(saladframe,image=thousandIslandDressing_img,height=200,width=350,bg="#ffffff")
    thousandIslandDressing.place(x=220.5+5-190,y=418-60)

    thousandIslandDressing_name=Label(saladframe,text="Thousand Island Dressing",width=50,bg="#ffffff")##name
    thousandIslandDressing_name.place(x=220.5+5-190,y=575)    
    
    thousandIslandDressing_price=Label(saladframe,text="15 LE",width=50,bg="#ffffff")##price
    thousandIslandDressing_price.place(x=220.5+5-190,y=575+20)
    
    garlicdip=Label(saladframe,image=garlicdip_img,height=200,width=350,bg="#ffffff")
    garlicdip.place(x=1135.5+5-190,y=418-60)
    
    garlicdip_name=Label(saladframe,text="Garlic Dip",width=50,bg="#ffffff")##name
    garlicdip_name.place(x=1135.5+5-190,y=575)    
    
    garlicdip_price=Label(saladframe,text="10 LE",width=50,bg="#ffffff")##price
    garlicdip_price.place(x=1135.5+5-190,y=575+20)


    mixedbeans=Label(saladframe,image=mixedbeans_img,height=200,width=350,bg="#ffffff")
    mixedbeans.place(x=678+5-190,y=418-60)

    mixedbeans_name=Label(saladframe,text="Mixed Beans",width=50,bg="#ffffff")##name
    mixedbeans_name.place(x=678+5-190,y=575)    
    
    mixedbeans_price=Label(saladframe,text="30 LE",width=50,bg="#ffffff")##price
    mixedbeans_price.place(x=678+5-190,y=575+20)

    def p_20_Coleslaw():
        l.append(20)
        s.append("Coleslaw")
    
    def p_15_GreenSalad():
        l.append(15)
        s.append("Green Salad")

    def p_25_Fattoush():
        l.append(25)
        s.append("Fattoush")
    
    def p_15_Thousand_Island_Dressing():
        l.append(15)
        s.append("Thousand Island Dressing")
    
    def p_30_Mixed_Beans():
        l.append(30)
        s.append("Mixed Beans") 
    
    def p_10_Garlic_Dip():
        l.append(10)
        s.append("Garlic Dip")
    

    coleslaw_btn=Button(saladframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_20_Coleslaw())
    coleslaw_btn.place(x=220.5+5-190+75,y=90.5+220)
    
    greensalad_btn=Button(saladframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_15_GreenSalad)
    greensalad_btn.place(x=678+5-190+75,y=90.5+220)
    
    fattoush_btn=Button(saladframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_25_Fattoush)
    fattoush_btn.place(x=1135.5+5-190+75,y=90.5+220)
    
    thousandIslandDressing_btn=Button(saladframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_15_Thousand_Island_Dressing)
    thousandIslandDressing_btn.place(x=220.5+5-190+75,y=650.5-15)
    
    mixedbeans_btn=Button(saladframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_30_Mixed_Beans)
    mixedbeans_btn.place(x=678+5-190+75,y=650.5-15)
    
    garlicdip_btn=Button(saladframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_10_Garlic_Dip)
    garlicdip_btn.place(x=1135.5+5-190+75,y=650.5-15)




def dessert_dessert():
    dessertframe=Frame(root,height=780-60,width=1520-190,bg="#ffffff")
    dessertframe.place(x=190,y=60)

    cheesecake=Label(dessertframe,image=cheesecake_img,height=200,width=350,bg="#ffffff")
    cheesecake.place(x=220.5+5-190,y=90.5-60)

    cheesecake_name=Label(dessertframe,text="CheeseCake",width=50,bg="#ffffff")##name
    cheesecake_name.place(x=220.5+5-190,y=90.5-60+200+20)

    cheesecake_price=Label(dessertframe,text="25 LE",width=50,bg="#ffffff")##price
    cheesecake_price.place(x=220.5+5-190,y=90.5-60+200+20+20)

    cinnabon=Label(dessertframe,image=cinnabon_img,height=200,width=350,bg="#ffffff")
    cinnabon.place(x=678+5-190,y=90.5-60)

    cinnabon_name=Label(dessertframe,text="Cinnabon",width=50,bg="#ffffff")##name
    cinnabon_name.place(x=678+5-190,y=90.5-60+200+20)

    cinnabon_price=Label(dessertframe,text="30 LE",width=50,bg="#ffffff")##price
    cinnabon_price.place(x=678+5-190,y=90.5-60+200+20+20)

    cupcake=Label(dessertframe,image=cupcake_img,height=200,width=350,bg="#ffffff")
    cupcake.place(x=1135.5+5-190,y=90.5-60)

    cupcake_name=Label(dessertframe,text="CupCake",width=50,bg="#ffffff")##name
    cupcake_name.place(x=1135.5+5-190,y=90.5-60+200+20)    
    
    cupcake_price=Label(dessertframe,text="25 LE",width=50,bg="#ffffff")##price
    cupcake_price.place(x=1135.5+5-190,y=90.5-60+200+20+20)

    donat=Label(dessertframe,image=donat_img,height=200,width=350,bg="#ffffff")
    donat.place(x=220.5+5-190,y=418-60)

    donat_name=Label(dessertframe,text="Donat",width=50,bg="#ffffff")##name
    donat_name.place(x=220.5+5-190,y=575)    
    
    donat_price=Label(dessertframe,text="20 LE",width=50,bg="#ffffff")##price
    donat_price.place(x=220.5+5-190,y=575+20)

    icecream=Label(dessertframe,image=icecream_img,height=200,width=350,bg="#ffffff")
    icecream.place(x=1135.5+5-190,y=418-60)

    icecream_name=Label(dessertframe,text="Ice Cream",width=50,bg="#ffffff")##name
    icecream_name.place(x=1135.5+5-190,y=575) 

    icecream_price=Label(dessertframe,text="15 LE",width=50,bg="#ffffff")##price
    icecream_price.place(x=1135.5+5-190,y=575+20)

    moltencake=Label(dessertframe,image=moltencake_img,height=200,width=350,bg="#ffffff")
    moltencake.place(x=678+5-190,y=418-60)

    moltencake_name=Label(dessertframe,text="Molten Cake",width=50,bg="#ffffff")##name
    moltencake_name.place(x=678+5-190,y=575)  

    moltencake_price=Label(dessertframe,text="30 LE",width=50,bg="#ffffff")##price
    moltencake_price.place(x=678+5-190,y=575+20)

    def p_25_CheeseCake():
        l.append(25)
        s.append("CheeseCake")
    
    def p_30_Cinnabon():
        l.append(30)
        s.append("Cinnabon")

    def p_25_CupCake():
        l.append(25)
        s.append("CupCake")
    
    def p_20_Donat():
        l.append(20)
        s.append("Donat")
    
    def p_30_Molten_Cake():
        l.append(30)
        s.append("Molten Cake") 
    
    def p_15_IceCream():
        l.append(15)
        s.append("IceCream")

    cheesecake_btn=Button(dessertframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_25_CheeseCake)
    cheesecake_btn.place(x=220.5+5-190+75,y=90.5+220)
    
    cinnabon_btn=Button(dessertframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_30_Cinnabon)
    cinnabon_btn.place(x=678+5-190+75,y=90.5+220)
    
    cupcake_btn=Button(dessertframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_25_CupCake)
    cupcake_btn.place(x=1135.5+5-190+75,y=90.5+220)
    
    donat_btn=Button(dessertframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_20_Donat)
    donat_btn.place(x=220.5+5-190+75,y=650.5-15)
    
    icecream_btn=Button(dessertframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_15_IceCream)
    icecream_btn.place(x=1135.5+5-190+75,y=650.5-15)
    
    moltencake_btn=Button(dessertframe,image=addimg,height=35,width=200,bd=0,relief=SUNKEN,cursor="hand2",bg="#ffffff",command=p_30_Molten_Cake)
    moltencake_btn.place(x=678+5-190+75,y=650.5-15)


l=[]
s=[]

def cart_cart():
    cartframe=Frame(root,height=780-60,width=1520-190,bg="#ffffff")
    cartframe.place(x=190,y=60)
    x=sum(l)
    label_total=Label(cartframe,text=f"Total Price = {x}",font=("Bro",30),width=20,bg="#ffffff")
    label_total.place(x=900,y=660)
    c=0
    u=0
    label1=Label(cartframe,text="Your Order :",font=("Bro",30),bg="#ffffff")
    label1.place(x=0,y=0+c) 
    
    for i in l:
        label_label=Label(cartframe,text=i,font=("Bro",30),bg="#ffffff")
        label_label.place(x=0,y=160+u)
        u=u+100
    
    for g in s:
        label11=Label(cartframe,text=g,font=("Bro",30),bg="#ffffff")
        label11.place(x=100,y=160+c)         
        c=c+100





def back1(enter):
        back_btn.config(image=img11)
        
def back2(event):
        back_btn.config(image=img12)

back_btn=Button(root,image=img12,height=40,width=40,bd=0,bg="#3381bf",activebackground="#3381bf",relief=SUNKEN,cursor="hand2")
back_btn.place(x=73,y=230+100+100+100+100)

back_btn.bind("<Enter>",back1)
back_btn.bind("<Leave>",back2)


def exitapp():
    root.destroy()

def exit1(enter):
        exit_btn.config(image=img9)
        
def exit2(event):
        exit_btn.config(image=img10)
    
exit_btn=Button(root,image=img10,height=40,width=40,bd=0,bg="#3381bf",relief=SUNKEN,cursor="hand2",command=exitapp)
exit_btn.place(x=73,y=230+100+100+100+100+50)

exit_btn.bind("<Enter>",exit1)
exit_btn.bind("<Leave>",exit2)



def f_profile():
    def profile1(enter):
        profile_btn.config(image=profileimg1)

    def profile2(event):
        profile_btn.config(image=profileimg2)

    profile_btn=Button(root,image=profileimg2,height=60,width=60,bd=0,bg="#3381bf",relief=SUNKEN,cursor="hand2",activebackground="#3381bf",command=c_profile)
    profile_btn.place(x=1450,y=-2)

    profile_btn.bind("<Enter>",profile1)
    profile_btn.bind("<Leave>",profile2)


def f_home():
    def home1(enter):
        home_btn.config(image=homeimg1)
            
    def home2(event):
        home_btn.config(image=homeimg2)

    home_btn=Button(root,image=homeimg2,height=50,width=155,bd=0,bg="#3381bf",relief=SUNKEN,cursor="hand2",command=c_home)
    home_btn.place(x=(190-155-4)/2,y=130)

    home_btn.bind("<Enter>",home1)
    home_btn.bind("<Leave>",home2)


def f_food():
    def food1(enter):
        food_btn1.config(image=img1)
        
    def food2(event):
        food_btn1.config(image=img2)
    
    food_btn1=Button(root,image=img2,height=70,width=150,bd=0,bg="#3381bf",relief=SUNKEN,cursor="hand2",command=c_food)
    food_btn1.place(x=18,y=230)
    
    food_btn1.bind("<Enter>",food1)
    food_btn1.bind("<Leave>",food2)


def f_drinks():
    def drinks1(enter):
        drinks_btn1.config(image=img3)
    
    def drinks2(event):
        drinks_btn1.config(image=img4)

    drinks_btn1=Button(root,image=img4,height=70,width=150,bd=0,relief="sunken",bg="#3381bf",cursor="hand2",command=c_drinks)
    drinks_btn1.place(x=18,y=230+100)

    drinks_btn1.bind("<Enter>",drinks1)
    drinks_btn1.bind("<Leave>",drinks2)


def f_salad():
    def salad1(enter):
        salad_btn1.config(image=img5)
    
    def salad2(event):
        salad_btn1.config(image=img6)

    salad_btn1=Button(root,image=img6,height=70,width=150,bd=0,relief="sunken",bg="#3381bf",cursor="hand2",command=c_salad)
    salad_btn1.place(x=18,y=230+100+100)

    salad_btn1.bind("<Enter>",salad1)
    salad_btn1.bind("<Leave>",salad2)


def f_dessert():
    
    def dessert1(enter):
        dessert_btn1.config(image=img7)
        
    def dessert2(event):
        dessert_btn1.config(image=img8)

    dessert_btn1=Button(root,image=img8,height=70,width=150,bd=0,relief="sunken",bg="#3381bf",cursor="hand2",command=c_dessert)
    dessert_btn1.place(x=18,y=230+100+100+100)

    dessert_btn1.bind("<Enter>",dessert1)
    dessert_btn1.bind("<Leave>",dessert2)

labelhome=Label(root,image=homeimg1,height=50,width=155)
labelfood=Label(root,image=img1,height=70,width=150)
labeldrinks=Label(root,image=img3,height=70,width=150)
labeldessert=Label(root,image=img7,height=70,width=150)
labelsalad=Label(root,image=img5,height=70,width=150)
labelprofile=Label(root,image=profileimg1,height=70,width=150)
labelcart=Label(root,image=cartimg1,height=70,width=150)


def c_home():
    global labelhome
    labelhome=Label(root,image=homeimg1,height=50,width=155)
    labelhome.place(x=(190-155-4)/2,y=130)
    home_home()
    labeldessert.place_forget()
    labelsalad.place_forget()
    labeldrinks.place_forget()
    labelfood.place_forget()
    labelprofile.place_forget()
    labelcart.place_forget()

def c_food():
    global labelfood
    labelfood=Label(root,image=img1,height=70,width=150)
    labelfood.place(x=18,y=230)
    food_food()
    labeldessert.place_forget()
    labelsalad.place_forget()
    labeldrinks.place_forget()
    labelhome.place_forget()
    labelprofile.place_forget()
    labelcart.place_forget()



  


def c_drinks():
    global labeldrinks
    ff=Frame(root,height=780-60,width=1520-190)
    ff.place(x=190,y=60)
    labeldrinks=Label(root,image=img3,height=70,width=150)
    labeldrinks.place(x=18,y=230+100)
    drinks_drinks()
    labeldessert.place_forget()
    labelsalad.place_forget()
    labelfood.place_forget()
    labelhome.place_forget()
    labelprofile.place_forget()
    labelcart.place_forget()
    



def c_salad():
    global labelsalad
    labelsalad=Label(root,image=img5,height=70,width=150)
    labelsalad.place(x=18,y=230+100+100)
    salad_salad()
    labeldessert.place_forget()
    labeldrinks.place_forget()
    labelfood.place_forget()
    labelhome.place_forget()    
    labelprofile.place_forget()
    labelcart.place_forget()
    



def c_dessert():
    global labeldessert
    labeldessert=Label(root,image=img7,height=70,width=150)
    labeldessert.place(x=18,y=230+100+100+100)
    dessert_dessert()
    labelsalad.place_forget()
    labeldrinks.place_forget()
    labelfood.place_forget()
    labelhome.place_forget()
    labelprofile.place_forget()
    labelcart.place_forget()

def c_profile():
    global labelprofile
    labelprofile=Label(root,image=profileimg1,height=60,width=60)
    labelprofile.place(x=1450,y=-3.5)

    labelsalad.place_forget()
    labeldrinks.place_forget()
    labelfood.place_forget()
    labelhome.place_forget()
    labelcart.place_forget()
    labeldessert.place_forget()

def c_cart():
    global labelcart
    labelcart=Label(root,image=cartimg1,height=60,width=60)
    labelcart.place(x=1380,y=-3.5)
    cart_cart()
    labelsalad.place_forget()
    labeldessert.place_forget()
    labeldrinks.place_forget()
    labelfood.place_forget()
    labelhome.place_forget()
    labelprofile.place_forget()


def cart1(enter):
        cart_btn.config(image=cartimg1)
    
def cart2(event):
        cart_btn.config(image=cartimg2)

cart_btn=Button(root,image=cartimg2,height=60,width=60,bd=0,relief="sunken",bg="#3381bf",cursor="hand2",command=c_cart)
cart_btn.place(x=1380,y=-2)

cart_btn.bind("<Enter>",cart1)
cart_btn.bind("<Leave>",cart2)


f_home()
f_profile()
f_food()
f_drinks()
f_salad()
f_dessert()


root.mainloop()
