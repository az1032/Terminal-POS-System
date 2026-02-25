import cv2 
import time
import os
from pyzbar.pyzbar import decode


def addbarcode():
    n=0
    while n==0:
        print('\n=========================================================')
        print('                [ BARCODE SCANNER MENU ]                 ')
        print('=========================================================')
        print("Camera is turning on,Press the 'esc' key to exit. ")
        webcam = cv2.VideoCapture(0)
        while True:
            
            kontrol,resim = webcam.read()
            if cv2.waitKey(20) == 27:
                break
            if not kontrol:
                print("an error came through while opening camera please try again.")
                break
            resim = cv2.flip(resim,1)
            cv2.imshow("window",resim)
            
            Barcode = decode(resim)
            x = '0'
            for i in Barcode:
                x = i.data.decode('utf-8')
            if x != '0':
                
                break 
            
            else:
                continue
        cv2.destroyAllWindows()
        webcam.release()

        file = open('barkodlar.txt','r')
        info = file.read()
        if x in info:
            print('This product is already registered.')
            file.close()
            return 1
        file.close()

        print('\n=========================================================')
        print('              [ NEW PRODUCT REGISTRATION ]               ')
        print('=========================================================')
        print(' Scanned Barcode: ' + x)
        print('=========================================================')

        nameOfproduct=input('Please enter the name of the product>>')
        print('---------------------------------------------------------')
        prize=input('cost per product>>')
        print('---------------------------------------------------------')
        prize2=input('the price at which the product will be sold is>>')
        print('---------------------------------------------------------')
        print('---------------------------------------------------------')
        
        
        file = open('barkodlar.txt','a')
        file.write(nameOfproduct+'-'+prize+'-'+prize2+'-'+x+'\n')
        file.close() 
        choise2=input('do you want to continue yes=1/no=2?>>')
        if choise2=='1':
            os.system('cls')
            continue
        elif choise2=='2':
            os.system('cls')
            break
        else:
            print(" [!] Not a viable option!")
            time.sleep(1.5)
            os.system('cls')
            continue 
    mainmenu()
            

    
def scanbarcode():
    import os
    os.system('mode con: cols=65 lines=25')
    print('\n=========================================================')
    print('                 [ CASHIER / SCANNER ]                   ')
    print('=========================================================')
    print(" Camera is turning on. Press the 'ENTER' key to exit.    ")
    print('=========================================================\n')

    webcam=cv2.VideoCapture(0)
    top =0
    
    quit = False
    while True:
        while True:
            file = open("barkodlar.txt","r")
            while True:
                
                kontrol,resim = webcam.read()
                if cv2.waitKey(20) == 13:
                    quit = True
                    break
                if not kontrol:
                    print("an error came through while opening camera please try again.")
                    break

                resim = cv2.flip(resim,1)
                cv2.imshow("window",resim)
                barcode = decode(resim)
                
                x = '0'
                barcode3="000000000009"
                for i in barcode:
                    x = i.data.decode('utf-8')
                    if x != '0':
                        for info2 in file:
                                name,cost,sold,barcode3=info2.strip().split("-")
                                if x == barcode3:
                                    print("---------------------------------------------------------")
                                    print(" " + name + " .............................. " + sold + " TL")
                                    
                                    top += int(sold)
                                    print(" CURRENT TOTAL ........................ " + str(top) + " TL")
                                    print("---------------------------------------------------------")
                                    time.sleep(1.5)
                                    file.seek(0)
                                    x = "0"
                                    break 
                    if x=="0":
                        continue
                    else:
                        print(" [!] WARNING: This barcode is not registered.")          
                    file.seek(0) 
                
            if quit == True:
                break
                
    
        file.close()
        cv2.destroyAllWindows()
        webcam.release()
        
        print('\n=========================================================')
        print('                 [ OVER ]                     ')
        print('=========================================================')
        print(' TOP: ' + str(top) + ' TL')
        print('=========================================================\n')
        print("press 1 for new customer/press 2 for main menu")
        choise3 =input(">>")
        if choise3 == "1":
            os.system("cls")
            scanbarcode()
        elif choise3 == "2":
           os.system("cls")
           mainmenu()
        else:
            print("not a viable option")
            return 1

        
    


def manageinventory():
    print("sa")
    
         
       
       

        
def mainmenu():
    print("--MAİN MENU--")
    print('---------------------------------------------------------')
    print("[1]-Add New Barcode")
    print("[2]-Scan Barcode")
    print("[3]-Manage Inventory")
    print("[4]-End Of Day Report")
    print('---------------------------------------------------------')
mainmenu()
choise = input("select >>   ")

match choise:
    case "1":
        os.system("cls")
        addbarcode()
    case "2":
        os.system("cls")
        scanbarcode()
    case "3":
        os.system("cls")
        manageinventory()
