from xlrd import open_workbook
msEv = float(input("Mac sonu ev sahibi oranı :"))
msBeraberlik = float(input("Mac sonu beraberlik oranı :"))
msDep = float(input("Mac sonu konuk takım oranı :"))
ilkEv = float(input("İlk yarı ev sahibi oranı :"))
ilkBeraberlik = float(input("İlk yarı beraberlik oranı :"))
ilkDep = float(input("İlk yarı konuk takım oranı :"))
var = float(input("Karşılıklı gol var :"))
yok = float(input("Karşılıklı gol yok :"))
alt = float(input("2,5 altı oranı :"))
ust = float(input("2,5 ust oranı :"))
print("------------------------------------------------------------------------")

re = open_workbook("excel-2017.xlsx")
sheet = re.sheet_by_index(0)
row = 3
toplam = 0
msE = 0
msB = 0
msD = 0
ilksE = 0
ilksB = 0
ilksD = 0
sVar = 0
sYok = 0
alt15 = 0
ust15 = 0
alt25 = 0
ust25 = 0
alt35 = 0
ust35 = 0
tg01 = 0
tg23 = 0
tg46 = 0
tg7 = 0
for row in range(sheet.nrows):
    if(sheet.row_values(row)[9] == msEv):
        if(sheet.row_values(row)[10] == msBeraberlik):
            if(sheet.row_values(row)[11] == msDep):
                if(sheet.row_values(row)[12] == ilkEv):
                    if(sheet.row_values(row)[13] == ilkBeraberlik):
                        if(sheet.row_values(row)[14] == ilkDep):
                            if(sheet.row_values(row)[18] == var):
                                if(sheet.row_values(row)[19] == yok):
                                    if(sheet.row_values(row)[27] == alt):
                                        if(sheet.row_values(row)[28] == ust):
                                            print(sheet.row_values(row)[5]+" - "+sheet.row_values(row)[6]+"   "+sheet.row_values(row)[7]+"   "+sheet.row_values(row)[8])
                                            igE = int(sheet.row_values(row)[7][0])
                                            igD = int(sheet.row_values(row)[7][4])
                                            mgE = int(sheet.row_values(row)[8][0])
                                            mgD = int(sheet.row_values(row)[8][4])
                                            toplam += 1
                                            if(mgE > mgD):
                                                msE += 1
                                            if(mgE == mgD):
                                                msB += 1
                                            if(mgE < mgD):
                                                msD += 1
                                            if(igE > igD):
                                                ilksE += 1
                                            if(igE == igD):
                                                ilksB += 1
                                            if(igE < igD):
                                                ilksD += 1
                                            if(mgE > 0 and mgD > 0):
                                                sVar += 1
                                            else:
                                                sYok += 1
                                            if((mgE+mgD) <= 1):
                                                alt15 += 1
                                            else:
                                                ust15 += 1
                                            if((mgE+mgD) <=2):
                                                alt25 += 1
                                            else:
                                                ust25 += 1
                                            if((mgE+mgD) <= 3):
                                                alt35 += 1
                                            else:
                                                ust35 += 1
                                            if((mgE+mgD) == 0 or (mgE+mgD) == 1):
                                                tg01 += 1
                                            if((mgE+mgD) == 2 or (mgE+mgD) == 3):
                                                tg23 += 1
                                            if((mgE+mgD) == 4 or (mgE+mgD) == 5 or (mgE+mgD) == 6):
                                                tg46 += 1
                                            if((mgE+mgD) >= 7):
                                                tg7 += 1

print("------------------------------------------------------------------------")
print("Toplam : "+str(toplam))
print("\nEv Sahibi : %"+str(int((msE*100)/toplam)))
print("Beraberlik : %"+str(int((msB*100)/toplam)))
print("Deplasman : %"+str(int((msD*100)/toplam)))
print("\nİlkyarı Ev Sahibi : %"+str(int((ilksE*100)/toplam)))
print("İlkyarı Beraberlik : %"+str(int((ilksB*100)/toplam)))
print("İlkyarı Deplasman : %"+str(int((ilksD*100)/toplam)))
print("\nKG Var : %"+str(int((sVar*100)/toplam)))
print("KG Yok : %"+str(int((sYok*100)/toplam)))
print("\n1.5 Altı : %"+str(int((alt15*100)/toplam)))
print("1.5 Üstü : %"+str(int((ust15*100)/toplam)))
print("\n2.5 Altı : %"+str(int((alt25*100)/toplam)))
print("2.5 Üstü : %"+str(int((ust25*100)/toplam)))
print("\n3.5 Altı : %"+str(int((alt35*100)/toplam)))
print("3.5 Üstü : %"+str(int((ust35*100)/toplam)))
print("\nToplam Gol 0-1 : %"+str(int((tg01*100)/toplam)))
print("Toplam Gol 2-3 : %"+str(int((tg23*100)/toplam)))
print("Toplam Gol 4-6 : %"+str(int((tg46*100)/toplam)))
print("Toplam Gol +7 : %"+str(int((tg7*100)/toplam)))