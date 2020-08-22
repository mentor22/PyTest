f = open('Mydata','r')
#print(f.readline())
#print(f.readline(4))
#print(f.readlines())
f1=open("abc",'w')
f1.write(f.read()) #works fine
f1.close()
#f1=open('abc','a')
#f1.write("\nFile is appended")
f.close()
#this was all about how we can read ,write and append
#let's copy and move data from a .jpg file image
f=open('river-safari_giant-panda-forest.jpg','rb')
f1=open('panda_pic.jpg','wb')
f1.write(f.read()) 
#copies binary data from image and pastes into new jpg file in binary from