import random
i = 0
o = 0
encrypted_list =[]
encrypt_decrypt = input(" Type '1' to encrypt, type '2' to decrpyt")
if encrypt_decrypt =='1':
    prompt = input("What would you like me to encrypt.")#.lower

    encryption_key = random.randint(1,9)

    encryption_key_2 = random.randint(0,9)

    for i in range(len(prompt)):  
        encrypted_list.append(ord(prompt[i])*encryption_key +encryption_key_2)
        i+=1
    print (f"{encrypted_list} \nyour keys are {encryption_key},{encryption_key_2}")

if encrypt_decrypt == '2':
    decryption_key_1 = int(input("what is your first encryption key? "))
    decryption_key_2 = int(input("what is your second encryption key? "))

    decryption_list=[]
    decrypted_letter = []
    decrypt_code = [int(x) for x in input("what do you want me to decrypt? please separate by commas").split(',')]
    for o in range(len(decrypt_code)):
        decryption_list.append((decrypt_code[o]-decryption_key_2)/decryption_key_1)
        decrypted_letter.append(chr(int(decryption_list[o])))
        o +=1
    print ("your message is")
    print(*(decrypted_letter), sep='')
            
