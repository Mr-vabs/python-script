# url = http://result.bteupexam.in/Odd_Semester/main/result.aspx?Roll_no=E1......
# url = http://result.bteupexam.in/Even_Semester/main/result.aspx?Roll_no=E1......
# from html2image import Html2Image
# hti = Html2Image()
# link = 'http://result.bteupexam.in/Odd_Semester/main/result.aspx?Roll_no=E1.......'
# hti.screenshot(url=link, save_as='test.png')

from html2image import Html2Image

def download(link, filename):

    try :
        print("\n\nDownloading.....{}\n\n".format(filename))
        hti = Html2Image()
        print(link)
        print("\n\ncopy paste this link in browser if not downloaded\n\n")
        hti.screenshot(url=link, save_as=filename)
        print("{} downloaded successfully.....\n".format(filename))
    except OSError :
        print("\nUnfortunately failed to generate file. \nNot supported for your OS. \n")
        print(link)
        print("Copy paste this link in browser if not downloaded\n")


choice = 1
print("Not supported in Android for now\n")
while choice :
    print("Download single or multiple results?")
    print("1. Single Result\n2. Multiple Results")
    choice = int(input("3. Exit\n"))
    
    if choice == 1 :
        print("\n\nFor Odd Even Semesters\n\n1. Odd semester choose 1\n2. Even Semester choose 2")
        sem = int(input("Enter 1 or 2 :: "))
        enum = input("\n\nEnter enrollment number:: ")
        if sem == 1:
          link = "http://result.bteupexam.in/Odd_Semester/main/result.aspx?Roll_no="+enum
        if sem == 2:
          link = "http://result.bteevaluation.co.in/even_test22testadc/main/oddresult.aspx?Roll_no="+enum
        
        filename = enum+".png"
        download(link,filename)
    
    if choice == 2 :
        print("Enter range :: ")
        lowenum = input("From this :: ")
        upenum = input("To this :: ")
        low = int(lowenum[1::])
        up = int(upenum[1::])
        up = up + 1
        print("\n\nFor Odd Even Semesters\n\n1. Odd semester choose 1\n2. Even Semester choose 2")
        sem = int(input("Enter 1 or 2 :: "))
        
        for i in range(low, up) :
            enum = upenum[:1:]
            i = f'{i}'
            enum = enum + i
            if sem == 1:
              link = "http://result.bteupexam.in/Odd_Semester/main/result.aspx?Roll_no="+enum
            if sem == 2:
              link = "http://result.bteevaluation.co.in/even_test22testadc/main/oddresult.aspx?Roll_no="+enum
        
            filename = enum+".png"
            download(link,filename)
    
    else :
        choice = 0
        print("bye bye...:D")
