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

ccode = input("\n\nEnter college code :: ")
enum = input("\n\nEnter enrollment number:: ")
url = "https://bteup.ac.in/AdmitCardVerificationCard/AdmitCard/"+ccode+"/"+enum+".pdf"
filename = enum+".pdf"
download(url,filename)
