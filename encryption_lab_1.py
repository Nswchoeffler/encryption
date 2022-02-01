import random

ABCD = "abcdefghijklmonpqrstuvwyxz"
ABCD_num =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
encrypt_decrypt = input(" Type '1' to encrypt, type '2' to decrpyt")
if encrypt_decrypt =='1':
    prompt = input("What would you like me to encrypt or decrypt.").lower

    encryption_list = [0,1,2,3,4,5,6,7,8,9]

    encryption_key = 1 #random.randint(0,9)
    #remove when works
    print(encryption_key)

    encryption_key_2 = random.randint(0,9)
    #remove when works
    print(encryption_key_2)

    if encryption_key == 1:
        for i in prompt:
            prompt_num =ord(prompt)
            print(prompt_num)
            
