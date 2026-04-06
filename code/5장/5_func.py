# 5_func.py

def return_info(name, phone, address, email):
    contact_info = f"연락처: {phone}\n{email}\n이메일: {eamil}"
    return f"이름: {naem}\n{contact_info}\주소:{address}"

def print_info(name, phone, address, email):
    contact_info = f"연락처: {phone}\n{email}\n이메일:\t{eamil}"
    print(f"이름:\t{naem}\n{contact_info}\n주소: {address}")
    
    print_info("aaron", "010-5555-5555", "전주")
    person = return_info(email = "hi@ut.ac.kr", phone="010-1111-1111",
                         address="교통대학교", name="Aaron"
                        )