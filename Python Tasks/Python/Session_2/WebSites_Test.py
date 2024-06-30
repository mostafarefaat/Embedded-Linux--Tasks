import Python.Session_2.Firelink as Firelink
print("List Of Available WebSites : ")
for link in Firelink.WebSites.keys():
    print(link, end="  ")
print("")

while True:
    url = input("Please Choose one of the Above Links : \n")
    Firelink.FireFox(Firelink.WebSites[url])
