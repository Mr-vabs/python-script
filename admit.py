import wget

def download(url, filename):

    print("\n\ndownloading.....\n\n")
    response = wget.download(url, filename)
    print("\n\ncopy paste this link in browser if not downloaded\n\n")
    print(url)

'''
from requests import get
def downloadasfile(url, filename):
    with open(filename, "wb") as file :
        print("\n\ndownloading.....\n\n")
        response = get(url, stream = True)
        file.write(response.content)
        print("\n\ncopy paste this link in browser if not downloaded\n\n")
        print(url)
'''



choice = 1
print("Not supported in Android for now\n")
while choice :
    print("Download single or multiple results?")
    print("1. Single Admit Card\n2. Multiple Admit Card")
    choice = int(input("3. Exit\n"))
    
    if choice == 1 :
        ccode = input("\n\nEnter college code :: ")
        enum = input("\n\nEnter enrollment number:: ")
        url = "https://bteup.ac.in/AdmitCardVerificationCard/AdmitCard/"+ccode+"/"+enum+".pdf"
        filename = enum+".pdf"
        download(url,filename)
    
    if choice == 2 :
        ccode = input("\n\nEnter college code :: ")
        print("Enter range :: ")
        lowenum = input("From this :: ")
        upenum = input("To this :: ")
        low = int(lowenum[1::])
        up = int(upenum[1::])
        up = up + 1
        
        for i in range(low, up) :
            enum = upenum[:1:]
            i = f'{i}'
            enum = enum + i
            url = "https://bteup.ac.in/AdmitCardVerificationCard/AdmitCard/"+ccode+"/"+enum+".pdf"
            filename = enum+".pdf"
            download(url,filename)
    
    else :
        choice = 0
        print("bye bye...:D")
