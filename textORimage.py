import requests
input1=input("Enter the choice : ")
if input1=="text":
    response=requests.get(input("Enter the url of text : "))
    print(response.text)

elif input1=="image":
    img=requests.get(input("Enter the url of image : "))
    with open((input("Enter the file name with extension(eg: jpg,png,etc...) : ")),"wb") as f:
        f.write(img.content)

else :
    print("Wrong choice")