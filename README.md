# 뭐먹지?

배달 음식 추천 서비스 — 파이썬 수업 팀 프로젝트

---

## 팀원

| 이름 | 담당 |
|------|------|
| 김건 | 메뉴 데이터 관리 (`menu_data.py`) |
| 김예람 | 랜덤 추천 로직 (`random_recommend.py`) |
| 김태민 | 조건 선택 화면 (`page_select.py`) |
| 김수현 | 홈 / 결과 화면 (`page_home.py`, `page_result.py`) |

---

## 실행 방법

### 1. 코드 받기

오른쪽 위 초록색 `Code` 버튼 → `Download ZIP` → 압축 풀기

또는 git이 설치되어 있다면:
```
git clone https://github.com/kimguny/mwomukji.git
```

### 2. 가상환경 만들기

터미널(맥) 또는 명령 프롬프트(윈도우)에서 프로젝트 폴더로 이동 후:

**맥 / 리눅스**
```
python3 -m venv venv
source venv/bin/activate
```

**윈도우**
```
python -m venv venv
venv\Scripts\activate
```

### 3. 패키지 설치

```
pip install PyQt6
```

### 4. 실행

```
python main.py
```

---

## 파일 구조

```
mwomukji/
├── main.py              # 앱 실행 진입점
├── styles.py            # 공통 색상 및 버튼 스타일
├── page_home.py         # 홈 화면
├── page_mode.py         # 추천 방식 선택 화면
├── page_select.py       # 조건 선택 화면
├── page_result.py       # 결과 화면
├── menu_data.py         # 메뉴 데이터 로드 및 필터링
├── random_recommend.py  # 랜덤 추천 로직
└── menus.json           # 메뉴 데이터 (42개)
```
