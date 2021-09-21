from tkinter import Label, Tk, Text, Entry, Button, END
import kutuphaneDFversion as kd

root = Tk()
root.geometry("1200x400")
root.title("Sancak Kutuphane")

def kitapa():
    kd.Uye(UyeiE.get(), UyesE.get()).kitapal(KitapAlE2.get(), KitapAlE.get())
    KitapAlE.delete(0, 'end')
    KitapAlE2.delete(0, 'end')
def kitapt():
    kd.Uye(UyeiE.get(), UyesE.get()).kitapteslim(KitapTE2.get(), KitapTE.get())

    KitapTE.delete(0, 'end')
    KitapTE2.delete(0, 'end')


def kitapg():
    kitaptext = kd.Uye(UyeiE.get(), UyesE.get()).kitapgoster()

    KitapGLdf.delete(1.0, END)
    KitapGLdf.insert(END, str(kitaptext))
    KitapGLdf.place(y=80, x= 400)

#    kitaps = kd.Uye(UyeiE.get(), UyesE.get()).name1
#    tarihs = kd.Uye(UyeiE.get(), UyesE.get()).date1
#
#    KitapGLBn.delete(first= 0, last= 10)
#    KitapGLBd.delete(first= 0, last= 10)
#
#    for a,b in zip(kitaps, range(len(kitaps))):
#        KitapGLBn.insert(b, a)
#
#    for a,b in zip(tarihs, range(len(tarihs))):
#        KitapGLBd.insert(b, a)
#
#    KitapGLBn.place(x = 200, y = 110)
#    KitapGLBd.place(x = 70, y = 110)
        


#Uye kısmı
Uyei = Label(root, text= "İsim")
Uyei.place(x=400, y= 10)

Uyes = Label(root, text = "Soyisim")
Uyes.place(x=550, y=10)

UyeiE = Entry(root, bd = 2)
UyeiE.place(x=400, y= 50)

UyesE = Entry(root, bd = 2)
UyesE.place(x=550, y= 50)

#KitapAlma kısmı
KitapAlL2 = Label(root, text = "Kitap No: ")
KitapAlL2.place(x=10, y=60)

KitapAlE2 = Entry(root, bd = 3)
KitapAlE2.place(x=100, y=60)

KitapAlL = Label(root, text = "Kitap Adı: ")
KitapAlL.place(x=10, y=10)

KitapAlE = Entry(root, bd = 3)
KitapAlE.place(x= 100, y=10)

KitapAlB = Button(root, text = "Kitap AL", command = kitapa)
KitapAlB.place(x=230, y=58)

#KitapTeslim kısmı
KitapTL2 = Label(root, text = "Teslim Kitap No")
KitapTL2.place(x=10, y=200)

KitapTE2 = Entry(root, bd = 3)
KitapTE2.place(x=100, y=200)

KitapTL = Label(root, text = "Teslim kitap Adı ")
KitapTL.place(x=10, y=150)

KitapTE = Entry(root, bd = 3)
KitapTE.place(x= 100, y=150)

KitapTB = Button(root, text = "Kitap Teslim", command = kitapt)
KitapTB.place(x=230, y=198)


#KitapGoster kısmı
KitapGB = Button(root, text = "Kitap Göster", command = kitapg)
KitapGB.place(x=100, y=250)
# 
# KitapGLBd = Listbox(root)
# KitapGLBn = Listbox(root)
# KitapGLBno= Listbox(root)
KitapGLdf = Text(root)

root.mainloop()