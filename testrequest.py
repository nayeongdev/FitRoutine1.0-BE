import requests

HOST = "http://127.0.0.1:8000"

print("\n===== 로그인 =====")
LOGIN_URL = HOST + "/accounts/login/"
LOGIN_INFO = {
    "email": "user@email.com",
    "password": "useruser",
}

res = requests.post(LOGIN_URL, data=LOGIN_INFO)
print(res.status_code)
print(res.json())
print("\n===== 로그인 끝 =====")

print("토큰 정보")
token = res.json()["tokens"]["access"]
print(token)

# JWT 헤더가 필요한 경우
headers = {
    "Authorization": "Bearer " + token,
}

print("\n***********************\n")

print("\n===== maker 리스트 =====")
res = requests.get(HOST + "/maker/", headers=headers)
print(res.status_code)
print(res.json())

print("\n===== maker 생성 =====")
data = {
    "goal": "운동목표",
    "level": "초급",
    "exercise_place": "운동장소",
    "preferred_exercise": "운동종목",
    "exercise_duration": 1,
    "author": "472a579b-b0a3-4567-bc6d-f61d053bfd1b",
}
res = requests.post(HOST + "/maker/", headers=headers, data=data)
print(res.status_code)
print(res.json())

print("\n===== maker 생성 확인 =====")
post_id = res.json()["id"]
res = requests.get(HOST + f"/maker/{post_id}", headers=headers)
print(res.status_code)
print(res.json())

print("\n***********************\n")

print("\n===== 루틴 리스트 =====")
res = requests.get(HOST + "/routines/", headers=headers)
print(res.status_code)
print(res.json())

print("\n===== 루틴 생성 =====")
data = {
    "title": "루틴 제목",
    "content": "루틴내용루틴내용\r\n 루틴내용루틴내용",
    "author": "1380beb2-a789-4f87-afca-4f3d6362905d",
    "exerciser_info": 5,
}

res = requests.post(HOST + "/routines/", headers=headers, data=data)
print(res.status_code)
print(res.json())

print("\n===== 루틴 생성 확인 =====")
routine_id = res.json()["id"]
res = requests.get(HOST + f"/routines/{routine_id}", headers=headers)
print(res.status_code)
print(res.json())
