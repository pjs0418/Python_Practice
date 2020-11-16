# -*- coding: utf-8 -*-

class Contact:
    def __init__(self, name, phone_num, email, address):
        self.name = name
        self.phone_num = phone_num
        self.email = email
        self.address = address
        
    def print_info(self):
        print("이름:", self.name)
        print("휴대폰 번호:", self.phone_num)
        print("이메일:", self.email)
        print("주소:", self.address)
        
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    num = int(input("번호 입력: "))
    return num

def set_contact():
    name = input("이름 입력: ")
    phone_num = input("휴대폰 번호 입력: ")
    email = input("이메일 입력: ")
    address = input("주소 입력: ")
    contact = Contact(name, phone_num, email, address)
    return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]
        
def run():
    contact_list = []
    
    while(True):
        sel_num = print_menu()
        if sel_num == 1:
            print("연락처 입력 실행")
            c = set_contact()
            contact_list.append(c)
        elif sel_num == 2:
            if contact_list == []:
                print("연락처 정보가 없습니다")
                continue
            
            print("연락처 출력 실행")
            print_contact(contact_list)
        elif sel_num == 3:
            if contact_list == []:
                print("연락처 정보가 없습니다")
                continue
            
            print("연락처 삭제 실행")
            name = input("삭제할 연락처의 이름 입력: ")
            delete_contact(contact_list, name)
        else:
            print("실행 종료")
            break
        
if __name__ == "__main__":
    run()