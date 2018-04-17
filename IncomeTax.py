__author__ = 'Razvan'
#single tax

#FirstDisk = 50000
#Seconddisk = 75000
#ThirdDisk = 100000
#FourthDisk = 250000
#FifthDisk = 500000
taxes = float

Income = int(input("Give in your income :"))
#Schijf 0-50000
if Income < 50000:
    taxes = Income * 0.01

    print("%.2f"%taxes)
#Schijf 50000-75000
elif Income >50000 and Income <75000:
    taxes = 50000*0.01
    rest = Income - 50000
    rest = rest * 0.02
    print("Your will have to pay: ""%.2f"%taxes," in taxes.")
#Schijf 75000-100000
elif Income >75000 and Income <100000:
    taxes = 50000 *0.01 +25000*0.02
    rest = Income - 75000

    taxes = taxes + Income *0.03
    print("Your will have to pay: ""%.2f"%taxes," in taxes.")

#Schijf 100000-250000
elif  Income >100000 and Income <250000:
    taxes = 50000 *0.01+ 25000 *0.02+ 25000*0.03
    rest = Income - 100000
    taxes = taxes + rest * 0.04
    print("Your will have to pay: ""%.2f"%taxes," in taxes.")

#Schijf 250000-500000#

elif Income > 250000 and Income <500000:
    taxes = 50000 *0.01+ 25000 *0.02+ 25000*0.03+ 150000*0.04
    rest = Income - 250000
    taxes = taxes + (rest * 0.05)
    print("Your will have to pay: ""%.2f"%taxes," in taxes.")

#Schijf >500000
elif Income >500000:
    taxes = 50000 *0.01+ 25000 *0.02+ 25000*0.03+ 150000*0.04 +250000*0.05
    rest = Income - 250000
    taxes = taxes + (rest * 0.05)
    print("Your will have to pay: ""%.2f"%taxes," in taxes.")