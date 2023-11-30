# FitRoutine1.0
사용자에게 맞춤형 운동 루틴을 제공하는 OpenAI 기반 플랫폼

## 1. 목표와 기능

### 1.1 목표
- OpenAI(ChatGPT)의 운동 루틴 추천
- 사용자에게 맞춤형 운동 루틴을 제공하는 플랫폼

### 1.2 기능
#### 사용자 정보 및 목표 설정
>  '사용자 입력 양식'을 미리 제공함으로써, 챗지피티와 사용자가 원활하게 상호작용할 수 있습니다.

1. 미리 정의된 양식을 제공하여, 사용자가 제공해야 하는 정보 유형에 대한 명확한 이해를 돕습니다.
2. 데이터의 일관성과 정확성을 높이기 위해, 양식을 통해 입력을 요청하도록 유도합니다.
3. 사용자가 텍스트로 모든 정보를 텍스트로 입력하는 대신, 미리 선택할 수 있는 옵션을 제공하여 사용자 경험을 개선합니다.
드롭다운 메뉴, 라디오 버튼 등을 활용하여 더 편리한 방법을 제공합니다.

#### 운동 루틴 추천
> OpenAI API를 활용하여 사용자의 상황에 맞는 운동 루틴을 제안합니다.

1. ChatGPT API를 활용하여 개인화된 운동 루틴 추천이 가능합니다.
2. 사용자의 운동 선호도에 따라 운동 계획을 제안합니다.

#### 운동 루틴 관리
> OpenAI가 제안한 운동 루틴을 관리합니다.

1. 사용자는 OpenAI가 제안한 운동 루틴이 마음에 들면 저장할 수 있습니다.
2. 저장된 운동 루틴은 수정하거나 삭제가 가능합니다.

## 2. 개발 환경과 프로젝트 일정
### 2.1 개발 환경
- Web Framework
  - Django 4.0 (Python 3.11)
  - Django Rest framework 3.13

### 2.2 프로젝트 개발 일정(WBS)
<img src="" width="100%">

![Alt text](_assets/WBS.png)

## 3. 요구사항 명세와 기능 명세
### 3.1 UML
![Alt text](_assets/%ED%95%8F%EB%A3%A8%ED%8B%B4_UML.png)

#### FitRoutine 웹사이트 Use Case Diagram 시나리오

**액터(Actor):**
- 사용자(User)
- Open AI(AI)

**FitRoutine Website 영역:**
- 사용자는 다음과 같은 기능을 수행할 수 있습니다.
    - (회원가입)
    - (로그인)
    - (운동 루틴 생성)
    - (저장한 루틴 목록 조회)
- (운동 루틴 생성)은 Open AI와 관련이 있습니다.
- (사용자 정보 입력)을 하여 (운동 루틴을 생성)합니다.
- (운동 루틴 생성)에서 (운동 루틴 저장하기)를 할 수 있습니다.
- (저장한 루틴 상세 조회)에서 (삭제), (수정)이 가능합니다.
- (운동 루틴 저장)을 하면 (저장한 루틴 목록 조회)에서 확인 가능합니다.

#### 유스케이스 상세 시나리오
<details>
  <summary>회원가입 유스케이스 시나리오</summary>
  <div markdown="1">
  
  - **유스케이스:** 회원가입

  - **시나리오:**
    1. **설명:** 사용자가 FitRoutine 웹사이트에 회원으로 가입하는 시나리오입니다. 사용자는 FitRoutine 웹사이트의 서비스를 이용하기 위해 회원으로 가입합니다.
    2. **Relationships:**
    - Initiator: 사용자
    - Pre-condition: 사용자(비회원)가 회원가입 기능을 실행합니다.
    - Post-condition: 고객의 정보가 시스템에 저장되고, FitRoutine 웹사이트의 회원이 됩니다.
    3. **기본 시나리오:**
        - 사용자는 웹사이트 회원가입 페이지로 이동합니다.
        - 사용자는 필수 정보(이메일, 유저네임, 비밀번호, 비밀번호 재확인)을 입력합니다.
        - 입력된 정보들 중에 이메일과 유저네임이 기존에 가입된 회원의 정보와 중복 여부를 확인하고, 비밀번호와 비밀번호 재확인이 일치하는지 확인합니다.
        - 정보가 유효하고 완료된 경우, 시스템은 사용자를 회원으로 등록하고, 회원가입 성공 메시지를 표시합니다.
    4. **예외 시나리오:**
        - 이미 등록된 이메일, 유저네임: 시스템은 사용자에게 중복된 이메일 또는 유저네임임을 알리고 다른 이메일이나 유저네임을 사용하도록 안내합니다.
        - 필수 정보 미입력: 사용자가 필수 정보를 입력하지 않은 경우, 시스템은 사용자에게 입력을 완료하도록 안내합니다.
  </div>
</details>
<details>
  <summary>로그인 유스케이스 시나리오</summary>
  <div markdown="1">
  
  - **유스케이스:** 로그인

  - **시나리오:**

  1. **설명:** 사용자는 FitRoutine 웹사이트에 접속하고 로그인합니다.
  2. **Relationships:**
  - Initiator: 사용자
  - Pre-condition: 
    - 사용자는 로그인을 하지 않은 상태입니다.
    - 사용자는 회원가입을 완료하여 계정을 가지고 있어야 합니다.
  - Post-condition: 사용자는 로그인하여 웹사이트의 기능 및 서비스를 이용할 수 있습니다.
  3. **주요 시나리오:**
      - 사용자는 웹사이트 로그인 페이지로 이동합니다.
      - 사용자는 등록한 이메일 주소와 비밀번호를 입력하여 로그인을 시도합니다.
      - 시스템은 사용자의 입력 정보를 확인하고, 유효한 경우 사용자를 인증하여 로그인 세션을 생성합니다.
      - 사용자는 성공적으로 로그인되어 웹사이트에 접근합니다.
  4. **예외 시나리오:**
      - 잘못된 이메일 주소 또는 비밀번호 입력: 시스템은 사용자에게 오류 메시지를 제공하고 다시 입력하도록 안내합니다.
      - 로그인 실패: 시스템 문제로 로그인에 실패할 경우, 사용자에게 에러 메시지를 제공하고 나중에 다시 시도하도록 안내합니다.

  </div>
</details>
<details>
  <summary>운동 루틴 생성 유스케이스 시나리오</summary>
  <div markdown="1">
  
  - **유스케이스:** 운동 루틴 생성

  - **시나리오:**
    1. **설명:** 사용자가 운동 루틴을 생성하는 시나리오입니다. 사용자는 요구사항을 입력하여 맞춤화된 운동 루틴을 생성할 수 있습니다.
    2. **Relationships:**
    - Initiator: 사용자
    - Supporters: Open AI
    - Pre-condition: 사용자는 이미 웹사이트에 로그인되어 있어야 합니다.
    - Post-condition: 사용자는 맞춤 생성된 운동 루틴을 확인하고, 그 결과를 저장할 수 있습니다.
    3. **주요 시나리오:**
        - 사용자는 "운동 루틴 생성"을 선택합니다.
        - 사용자의 사전정보(운동 목표, 운동 장소, 운동 시간, 운동 레벨, 선호 운동)를 받기 위한 화면이 나타납니다.
        - 사용자는 사전정보를 입력하고 '생성' 기능을 실행합니다.
        - 시스템은 사전정보를 기반으로 사용자의 요청에 따라 Open AI기반의 맞춤 운동 루틴을 보여줍니다.
        - 사용자가 운동 루틴을 저장하기를 원할 때 "저장" 버튼을 누르면 사용자의 루틴모델(제목, 내용)에 저장됩니다.
    4. **예외 시나리오:**
      - **사용자 정보 미입력:** 사용자가 필수 정보를 입력하지 않은 경우, 시스템은 정보를 입력하도록 안내합니다.
      - **루틴 생성 실패:** 시스템이 사용자의 입력을 기반으로 운동 루틴을 생성하는 도중에 문제가 발생한 경우, 사용자에게 실패 메시지를 제공하고 다시 시도하도록 안내합니다.

  </div>
</details>
<details>
  <summary>루틴 목록 조회 유스케이스 시나리오</summary>
  <div markdown="1">
  
  - **유스케이스:** 루틴 목록 조회

  - **시나리오:**
    1. **설명:** 사용자는 FitRoutine 웹사이트에 접속하고 로그인합니다.
    2. **Relationships:**
    - Initiator: 사용자
    - Pre-condition: 사용자는 이미 웹사이트에 로그인되어 있어야 합니다.
    - Post-condition: 사용자는 저장한 루틴 목록을 확인하고 상세 정보를 조회할 수 있습니다.
    - **사전조건:** 사용자는 이미 웹사이트에 로그인되어 있어야 합니다.
    - **주요 시나리오:**
        - 사용자는 "저장한 루틴 보기"를 선택합니다.
        - 시스템은 사용자가 저장한 운동 루틴의 목록을 조회하는 페이지를 제공합니다.
        - 시스템은 사용자가 선택한 운동 루틴에 대한 상세 정보를 제공합니다.

    4. **예외 시나리오:**
      - **조회 실패:** 시스템이 저장한 루틴 목록을 조회하는 도중에 문제가 발생한 경우, 사용자에게 실패 메시지를 제공하고 다시 시도하도록 안내합니다.
      - **후행조건:** 사용자는 저장한 루틴 목록을 확인하고 상세 정보를 조회할 수 있습니다. 상세 정보 페이지에서 사용자는 수정이나 삭제를 할 수 있습니다.

  </div>
</details>


### 3.2 데이터베이스 모델링(ERD)
[ERDCloud](https://www.erdcloud.com/d/kjB3ccAdGPgDxF4ay)

![Alt text](_assets/%ED%95%8F%EB%A3%A8%ED%8B%B4ERD.png)

### 3.3 RESTful API 설계
![Alt text](_assets/API1.png)
![Alt text](_assets/API2.png)


## 3. 와이어프레임 / UI

### 3.1 와이어프레임
![화면설계](_assets/%ED%99%94%EB%A9%B4%EC%84%A4%EA%B3%84.png)

![화면1](_assets/%ED%99%94%EB%A9%B41.png)
- 메뉴를 통해 로그인과 회원가입을 할 수 있습니다.

![화면2](_assets/%ED%99%94%EB%A9%B42.png)
- 메인 화면이나 메뉴에서 운동 루틴 생성하기 버튼을 누르면, 사용자 정보 입력 폼을 제공하고, 그것에 맞춤화된 운동 루틴을 생성해 줍니다.
- 운동 루틴 결과 페이지에서 운동 루틴 저장하기 버튼을 누르면 운동 루틴 보관함에 저장하게 됩니다.

![화면3](_assets/%ED%99%94%EB%A9%B43.png)
- 운동 루틴 보관함에서 저장된 글을 상세히 볼 수 있습니다.
- 상세 페이지에서 글 수정과 글 삭제가 가능합니다.

### 3.2 화면 설계
<table>
    <tbody>
        <tr>
            <td>로그인</td>
            <td>로그아웃</td>
        </tr>
        <tr>
            <td>
		          <img src="_assets/loginPage.gif" width="100%">
            </td>
            <td>
		          <img src="_assets/logoutPage.gif" width="100%">
            </td>
        </tr>
        <tr>
            <td>회원 가입</td>
            <td>루틴 생성</td>
        </tr>
        <tr>
          <td>
            <img src="_assets/signupPage.gif" width="100%">
          </td>
          <td>
            <img src="_assets/maker.gif" width="100%">
          </td>
        </tr>
        <tr>
            <td>루틴 저장 및 상세보기</td>
        </tr>
        <tr>
          <td>
            <img src="_assets/makerSave.gif" width="100%">
          </td>
        </tr>
    </tbody>
</table>

## 4. 프로젝트 구조
```
📦FitRoutine1.0-BE
 ┣ 📂___           => startproject
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜exceptions.py
 ┃ ┣ 📜managers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂routines
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜testrequest.py
```

## 5. 메인 기능
### 5.1 사용자 인증
**로그인**  
<img src="_assets/ThunderClient_2.png" width="100%">

- **POST** Request  
  `/accounts/login/`
  - Header
    - content-type : application/json
  - Body
    ```json
    {
      "email": "user1@email.com",
      "password": "1234!@#$"
    }
    ```
  - Response
    - Status: 200 OK
      ```json
      {
        "email": "user1@email.com",
        "tokens": {
          "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMTQ0MjY3MSwiaWF0IjoxNzAxMzU2MjcxLCJqdGkiOiIxNzIxZDljNjc1ZTk0ZGQ1YWE4MTg1Zjg2YTcxZDAyNyIsInVzZXJfaWQiOiIxMzgwYmViMi1hNzg5LTRmODctYWZjYS00ZjNkNjM2MjkwNWQifQ.5kH6f1khnQ0-DO2eRo1b_rXOg2nbks8W_2ifG93qUhE",
          "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxMzYxMDcxLCJpYXQiOjE3MDEzNTYyNzEsImp0aSI6IjVmNjdkY2NkZDFlMjQyZDQ4YjA2YjFhNzg4YzQwYjgyIiwidXNlcl9pZCI6IjEzODBiZWIyLWE3ODktNGY4Ny1hZmNhLTRmM2Q2MzYyOTA1ZCJ9.I0XpNZ7ls8P0rHMtOqaUzysf38IYmXXHmTm7JaSzP0Q"
        }
      }
      ```
    - Status: 400 Bad Request
      ```json
      {
        "non_field_errors": [
          "이 이메일과 비밀번호를 가진 사용자를 찾을 수 없습니다."
        ]
      }
      ```

<details>
  <summary>회원 가입</summary>
  <div markdown="1">
  <img src="_assets/ThunderClient_1.png" width="100%">
    
  - **POST** Request  
    `/accounts/join/`
    - Header
      - content-type : application/json
    - Body
      ```json
      {
        "email": "user1@email.com",
        "username": "user1",
        "password": "1234!@#$",
        "password2": "1234!@#$",
        "date_of_birth": null,  // "YYYY-MM-DD"
        "height": null,         // integer
        "weight": null,         // integer
        "gender": null          // "","남자","여자"
      }
      ```
    - Response
      - Status: 201 Created
        ```json
        {
          "email": "user1@email.com",
          "username": "user1",
          "date_of_birth": null,
          "height": null,
          "weight": null,
          "gender": null
        }
        ```
      - Status: 400 Bad Request
        ```json
        {
          "email": [
            "이 필드는 반드시 고유(unique)해야 합니다."
          ],
          "username": [
            "이 필드는 반드시 고유(unique)해야 합니다."
          ],
          "password": [
            "비밀번호가 일치하지 않습니다."
          ],
          "password": [
            "비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.",
            "비밀번호가 너무 일상적인 단어입니다."
          ],
          "date_of_birth": [
            "Date의 포멧이 잘못되었습니다. 이 형식들 중 한가지를 사용하세요: YYYY-MM-DD."
          ],
          "height": [
            "유효한 숫자를 넣어주세요."
          ],
          "weight": [
            "유효한 숫자를 넣어주세요."
          ],
          "gender": [
            "\"잘못된데이터\"이 유효하지 않은 선택(choice)입니다."
          ]
        }
        ```
  </div>
</details>

### 5.2 루틴 생성
<img src="_assets/ThunderClient_9.png" width="100%">

- **POST** Request  
  `/maker/`
  - Header
    - content-type : application/json
    - Authorization : Bearer {access_token}
  - Body
    ```json
    {
      "goal": "체중 감량",
      "level": "초급",
      "exercise_place": "운동장",
      "preferred_exercise": "축구",
      "exercise_duration": 20
    }
    ```
  - Response
    - Status: 201 Created
      ```json
      {
        "chat_gpt_response": "운동 목표가 '체중 감량'이고 운동 수준이 '초급'인 사용자를 위한 운동 루틴을 계획합니다. 운동은 '운동장'에서 진행하며, '축구'를 선호하는 사용자입니다. 운동 시간은 20분으로 설정합니다.\n\n1. 워밍업: 5분간 경량한 스트레칭과 조깅으로 근육을 준비합니다.\n2. 운동 메인: 15분간 축구를 플레이합니다. 축구는 전신 운동으로 체중 감량에 효과적입니다.\n3. 쿨다운: 5분간 경량한 스트레칭과 걷기로 심장을 천천히 가라앉히고 근육을 이완시킵니다."
      }
      ```
    - Status: 400 Bad Request
      ```json
      {
        "goal": [
          "이 필드는 blank일 수 없습니다."
        ],
        "level": [
          "\"\"이 유효하지 않은 선택(choice)입니다."
        ],
        "exercise_place": [
          "이 필드는 blank일 수 없습니다."
        ],
        "preferred_exercise": [
          "이 필드는 blank일 수 없습니다."
        ],
        "exercise_duration": [
          "이 필드는 null일 수 없습니다."
        ]
      }
      ```

<details>
  <summary>입력한 정보 조회</summary>
  <div markdown="1">
  <ol>
    <li>
      <p>입력한 정보 리스트</p>
      <strong>GET</strong> /maker/
      <img src="_assets/ThunderClient_10.png" width="100%">
    </li>
    <li>
      <p>입력한 정보 상세</p>
      <strong>GET</strong> /maker/{exerciserId}
      <img src="_assets/ThunderClient_11.png" width="100%">
    </li>
  </ol>
  </div>
</details>

<details>
  <summary>루틴 CRUD</summary>
  <div markdown="1">
  <ol>
    <li>
      <p>루틴 저장</p>
      <strong>POST</strong> /routine/?exerciser_id={exerciserId}/
      <img src="_assets/ThunderClient_5.png" width="100%">
    </li>
    <li>
      <p>루틴 리스트</p>
      <strong>GET</strong> /routines/
      <img src="_assets/ThunderClient_3.png" width="100%">
    </li>
    <li>
      <p>루틴 상세</p>
      <strong>GET</strong> /routines/{routineId}/
      <img src="_assets/ThunderClient_6.png" width="100%">
    </li>
    <li>
      <p>루틴 수정</p>
      <strong>PUT</strong> /routines/{routineId}/
      <img src="_assets/ThunderClient_7.png" width="100%">
    </li>
    <li>
      <p>루틴 삭제</p>
      <strong>DELETE</strong> /routines/{routineId}/
      <img src="_assets/ThunderClient_8.png" width="100%">
    </li>
  </ol>
  </div>
</details>


## 6. 에러와 에러 해결
### 6.1 회원 가입할때 비밀번호 저장이 왜 안될까?  
회원가입을 하면 개인 정보가 잘 저장되지만, 비밀번호만 공백으로 저장되는 현상

- 문제의 코드
  ```python
  def create(self, validated_data):
      """Return user after creation."""
      user = CustomUser.objects.create(
          username=validated_data["username"], email=validated_data["email"]
      )
      user.set_password(validated_data["password"])  # 비밀번호 암호화       
      user.date_of_birth = validated_data.get("date_of_birth", None)
      user.height = validated_data.get("height", None)
      user.weight = validated_data.get("weight", None)
      user.gender = validated_data.get("gender", None)
      user.save(update_fields=["date_of_birth", "height", "weight", "gender"])
      return user
  ```
  - [스택오버플로우](https://stackoverflow.com/questions/74013247/django-rest-framework-set-password-on-instance-in-update-function-returns-non)의 도움을 받아, set_password을 하면 바로 user.save()를 꼭 해줘야한다는 것을 알게되었습니다.
  - [Django 공식문서](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password)를 보면  사용자 인스턴스에서 비밀번호를 해싱하고 설정하는 것은 user.set_password가 처리하지만 데이터베이스에 인스턴스를 저장하지는 않는다고 명시되어 있습니다.

- 해결 코드
  ```python
  def create(self, validated_data):
      """Return user after creation."""
      user = CustomUser.objects.create(
          username=validated_data["username"], email=validated_data["email"]
      )
      user.set_password(validated_data["password"])  # 비밀번호 암호화
      user.save()
      
      user.date_of_birth = validated_data.get("date_of_birth", None)
      user.height = validated_data.get("height", None)
      user.weight = validated_data.get("weight", None)
      user.gender = validated_data.get("gender", None)
      user.save(update_fields=["date_of_birth", "height", "weight", "gender"])
      return user
  ```
### 6.2 다른 브랜치에 있는 내용이 왜 합쳐지지 않을까?  
- [상황]  
git branch를 다루는 능력을 향상시키기 위해서 main 브랜치 이외에 다른 브랜치 2개를 더 만들어 사용하고 있었습니다.   
accouts 브랜치에 있는 내용을 main 브랜치에 merge한 후, routines 브랜치로 변경해서 main브랜치에 있는 내용을 가져오려고 하였으나 의도대로 되지 않았습니다.  
이때 사용한 명령어는 `git merge origin/main`과 `git pull origin/main` 그리고 `git pull main`입니다.  
주말 새벽에 일어난 일이라 주변 사람들에게 도움을 요청할 수 없었습니다. 그래서 커뮤니티 질문을 활용하여 한 분의 답변에서 힌트를 얻어 이 상황이 벌어진 이유에 대해 파악할 수 있었습니다.  

- [원인]    
  - `git merge`와 `git pull`의 차이를 인지하지 못했다.  
    `git merge`는 다른 브랜치에 있는 내용을 끌어오는 것이고, `git pull`은 현재 브랜치에 있는 내용을 끌어오는 것이라는 것에 대한 차이를 이번 기회에 정확히 인지하게 되었습니다.

  - `origin/main`과 `main`의 차이를 인지하지 못했다.  
    `git merge origin/main`을 했는데도 되지 않았던이유가 다음과 같습니다.
      1. 다른 브랜치에서 main브랜치에 merge하는 과정이 로컬에서만 된 상태였다.(push를 안한 상태)
      2. 원격 저장소인 `origin/main`에는 반영되지않아서 `git merge origin/main`을 해도 아무 소용이 없었다.
    
      `origin/main`은 원격저장소이고` main`은 로컬저장소인 것을 한 번 더 인지하는 계기가 되었습니다.

- [해결]  
  - `git merge main` 명령어 입력 (선택)
  - main branch의 변경사항을 push한 후, `git merge origin/main` 명령어 입력

### 6.3 CORS 에러
- 소문으로 듣던 CORS 에러을 이번 DRF 프로젝트를 하면서 겪게 되었습니다.
![Alt text](_assets/CORS.png)
- CORS(Cross-Origin Resource Sharing)의 약자로, 서로 다른 출처에서 리소스를 공유하는 것을 뜻한다.
- 백엔드 개발의 url은 `http://localhost:8000/` (장고 서버)이고 프론트 개발은 `http://localhost:5500/` (라이브 서버) 이였다.
  - url의 차이때문에 CORS 에러가 발생했다.
- 해결
  - 크롬 브라우저에서 익스텐션을 깔아서 하는 방법이나 프록시 서버를 이용하는 방법이 있었습니다.
  - 그 중에서 제일 간단한 방법이 장고에서 django-cors-headers를 활용하는 것이 였습니다. 
  - django-cors-headers의 (github)[https://github.com/adamchainz/django-cors-headers]을 참고하여 장고의 settings.py에서 수정
    ```python
    # settings.py
  
    INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
    ]
  
    MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
    ]
    
    CORS_ALLOWED_ORIGINS = [
      "http://127.0.0.1:5500",
    ]
    ```

### 6.4 프론트에서는 필요없는 항목이 API응답에는 필요한 상황  
POST 요청시 author 정보가 필요하지만, 프론트에는 author를 입력할 input이 따로 있지 않았습니다. 이를 고려하지 않고 서버를 개발했는데, API 연결 과정에서 이것을 서버에서 처리 해야한다는 것을 알게되었습니다.

![Alt text](_assets/author.png)

views.py에서 serializer.save(author=request.user)을 추가하여 사용자가 따로 입력하지 않아도 들어갈 수 있게 작성했습니다.
- Excerciser 모델에 등록시 (기존 코드에 추가)
  ```py
  def create(self, request):
      ...
      serializer.save(author=request.user)
  ```
- Routine 모델에 등록시 (create 함수 생성)
  ```py
  def create(self, request):
      exerciser_id = request.query_params.get("exerciser_id")
      exerciser_info = Exerciser.objects.get(pk=exerciser_id)

      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save(author=request.user, exerciser_info=exerciser_info)

      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, headers=headers)
  ``` 


## 7. 개발하며 느낀점
- 프론트와 백엔드가 나눠져 있다보니 더 고려할 것이 많았고, 그러다보니 기획이 쉽지 않았습니다. 기획을 빠르게 끝내기 위해서 ChatGPT를 적극 활용하는 노하우도 습득하게 되었습니다.
- 이 프로젝트를 하면서 API 문서의 중요성을 깨달았습니다. 프론트 개발을 할 때 코드와 기억에 의존한채 API 연결을 하려다보니, 오류가 잦았고 왜 오류가 나는지 이유를 알 수 없었습니다. 그래서 API를 명시해둔 ThunderClient를 보고 활용해보니까 오류가 나도 원인을 파악하는데 매우 큰 도움이 되었습니다.
- 모르는 내용은 긴 시간동안 붙잡는 것보단 물어보는 게 더 현명하다는 것을 느끼게 되었습니다. 물어보는 과정에서 한 번더 자신의 상황에 대해서 파악하고, 답변에서 생각하지도 못한 방법을 알아가서 빠른 개발에 도움이 될 수 있었습니다.
- 처음으로 DRF을 통해 API를 개발하고, 프론트까지 연결하는 작업을 했습니다. 비록 완전히 기능을 다 구현하지 못하고 일정이 밀려 배포도 시도하지 못 했지만, 혼자 API를 만들고 활용해서 풀스택을 전반적으로 경험해 본 것이 저에게 유의미한 경험이였습니다.