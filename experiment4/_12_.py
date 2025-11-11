
'''
password_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
'''
import random
# chr() Unicode
# ord() deUnicode
password_list=[chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]
special_list=['+','-', '*', '/', '?', '!' ,'@' ,'#', '￥','%','&']
def make_password(length):
    password_generated=[random.choice(password_list) for _ in range(0,length)]
    password_generated=insertAtRandom(password_generated,length)
    return password_generated
def insertAtRandom(list_password,length):
    '''special_character=str(special_list[random.randint(0,9)])
    number_character=random.randint(0,10)
    '''
    special_character=random.choice(special_list)
    number_character=random.randint(0,10)

    special_insert = random.randint(0, length-1)
    number_insert=random.randint(0,length-1)
    while special_insert==number_insert:
        number_insert = random.randint(0, length-1)

    list_password[special_insert]=special_character
    list_password[number_insert]=str(number_character)
    return ''.join(list_password)

if __name__=="__main__":
    while True:
        try :
            length=int(input("Input the length of password:\n"))
            break
        except ValueError:
            print("Please input a number!\n")
            continue
        try_flag=1
    password=make_password(length)
    print(password)

