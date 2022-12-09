# This program is designed by Saroj Kumar tharu to shorthen the url or hide a real url 

from msvcrt import getch
from os import system
from cuttpy import Cuttpy
import webbrowser  

class LinkShorthen:
    url=""
    api="" # api ---> api number 
    with open ("api.txt",'r') as file:
        api=file.read()
        
    shortener = Cuttpy(api)

    def GenerateNewLink():  
        ''' Generated New link '''
        system("cls")
        print("\n\t\t <------ New Generate Link Section -----> ")
        url=input("\n\t\t Enter the your URL ----> ")
        # shorten URL
        try:
            response = LinkShorthen.shortener.shorten(url)
            LinkShorthen.url=response.shortened_url
            # print shortened url
            result="\t\t Your Shorthen Link -----> "+response.shortened_url
            print(result)
            
        except:
            print("\n\t\t <---- May be Internet Is Not Working -----> ")

        # getch()

    def OpenGeneratedLink():
        ''' Open Generated Link '''
        system("cls")
        if LinkShorthen.url =="":
            print("\n\t\tRecently Generated link ----> Empty")
        else:
            print(f"\n\t\t Recently Generated link ----> {LinkShorthen.url}")

        print("\t Note ----> Press Enter to Generated url Recently ")
        
        url=input("\n\t\t Please Enter New Url ----> ")

        print("\t\t Opening link in Brower ")
        if url=="":
            if LinkShorthen.url =="":
                print("\n\t\t Link is not Generated ")
                getch()
                return 0
            webbrowser.open(LinkShorthen.url, new=1, autoraise=True)
        else:
            webbrowser.open(url, new=1, autoraise=True)
    

    def AboutUs():
        ''' About Developer  '''
        system("cls")
        
        art="\n\t\t Tʜɪs Pʀᴏɢʀᴀᴍ ɪs Dᴇsɪɢɴᴇᴅ Bʏ  Sᴀʀᴏᴊ Kʀ. Tʜᴀʀᴜ."
        print("\n\t\t <--- Welcome to About us Section -----> ")
        print(art)
        getch()


    def menu():
        # while(True):
            system("cls")
            print("\n\t\t <---- Welcome to Main Menu -----> ")
            print("\t\t\t 1 . Generate New Link ")
            print("\t\t\t 2 . Open Generate Link  ")
            print("\t\t\t 10. About Us ")
            print("\t\t\t 99. Exit ")
            choice=int( input("\t\t  Your Choice ----> ") )
            
            if choice ==1:
                LinkShorthen.GenerateNewLink()
                LinkShorthen.banner(1)
            elif choice ==2:
                LinkShorthen.OpenGeneratedLink()
                LinkShorthen.banner(2)
            elif choice ==10:
                LinkShorthen.AboutUs()
                LinkShorthen.banner(3)
                
            elif choice ==99:
                LinkShorthen.ExitProgram()
                
            else:
                print("\n\t\t <---- Invalid Options -----> ")

    def ExitProgram():
        print("\n\t\t <---- Thanks for Using Our Program -----> ")
        print("\t\t <---- Exiting -----> ")
        exit()

    def banner(no):
        ''' Banner near the bottom'''

        # system("cls")
        if LinkShorthen.url =="":
            print("\n\t\tRecently Generated link ----> Empty")
        else:
            print(f"\n\t\t Recently Generated link ----> {LinkShorthen.url}")


        if no==1:
            ''' 1 ---> open  2----> about 3 ----> exit'''
            
            cho=int( input("\t\t  1. Open Link \t\t 10. About Us \t\t 99. Exit") )
            if cho ==1:
                LinkShorthen.OpenGeneratedLink()
                LinkShorthen.banner(2)
            elif cho ==10:
                LinkShorthen.AboutUs()
                LinkShorthen.banner(3)
            elif cho ==99:
                LinkShorthen.ExitProgram()
                
            else:
                print("\n\t\t Invalid options ")
                getch()
                system("cls")
                LinkShorthen.banner(1)
                
                

        elif no==2:
            ''' 1 ---> generate  2----> about 3 ----> exit'''
            cho=int( input("\t\t  1. Generated New Link \t\t 10. About Us \t\t 99. Exit") )
            if cho ==1:
                LinkShorthen.GenerateNewLink()
                LinkShorthen.banner(1)
            elif cho ==10:
                LinkShorthen.AboutUs()
                LinkShorthen.banner(3)
            elif cho ==99:
                LinkShorthen.ExitProgram()
                
            else:
                print("\n\t\t Invalid options ")
                getch()
                system("cls")
                LinkShorthen.banner(2)
            

        elif no==3:
            ''' 1 ---> generate  2----> open  3 ----> exit '''
            cho=int( input("\t\t  1. Generated New Link \t\t 10. Open Link \t\t 99. Exit") )
            if cho ==1:
                LinkShorthen.GenerateNewLink()
                LinkShorthen.banner(1)
            elif cho ==10:
                LinkShorthen.OpenGeneratedLink()
                LinkShorthen.banner(2)
            elif cho ==99:
                LinkShorthen.ExitProgram()
                
            else:
                print("\n\t\t Invalid options ")
                getch()
                system("cls")
                LinkShorthen.banner(3)
        
            

def main():
    link=LinkShorthen
    link.menu()



if __name__=='__main__':
    main()

