import pyqrcode

# content = "this is my content"
# url = pyqrcode.create(content)
# url.png("myqr.png",scale=9)



def GenerateQrWithData(rollno,name,clas):
    content = rollno+","+name+","+clas
    url = pyqrcode.create(content)
    url.png(rollno+".png",scale=10)

# GenerateQrWithData('Bablu','B.tech','Cse')


def GeneareQrWithFile(filename,path):
    with open(filename, 'r') as f:
        lines = [l[:-1] for l in f.readlines() if len(l) > 2]
        for line in lines:
            print(line)
            url = pyqrcode.create(line)
            url.png(path+"/"+line.split(",")[0]+".png",scale=10)


GeneareQrWithFile("students.csv","data")
# with open('whitelist.txt', 'r') as f:
#     authorized_users = [l[:-1] for l in f.readlines() if len(l) > 2]
#     print(authorized_users)
#     f.close()

