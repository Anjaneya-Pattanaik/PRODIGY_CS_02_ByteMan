print("Welcome to Image Cryptor!!!\nOptions:\n1. Encrypt\t2. Exit")
print("\n**Encryption of an image twice causes decryption producing the original image**")

def crypt():
    path= input('Enter path of Image: ').strip('"')
    key=int(input('Enter (Non-zero Integer) Key for encryption of Image: '))
    img=open(path, 'rb')
    image=img.read()
    img.close()
    image=bytearray(image)
    for index,values in enumerate(image):
    	image[index]=values^key
    img=open(path, 'wb')
    img.write(image)
    img.close()
    print('Crypted...')

        
while (True):
    opt=int(input("Enter option: "))
    if opt==1:
        crypt()
    elif opt==2:
        print("Thankyou!!")
        break
    else:
        print("Invalid Option!")
