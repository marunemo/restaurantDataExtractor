# restaurantDataExtractor

카카오맵 식당 크롤링 데이터 포맷 설정

- 운영시간 포맷
  - changeParsing.py : dateParsing.py와 hanchelin_json.py의 코드를 결합하고, 실제 데이터 사용에 맞게 수정
  - dateParsing.py : hanchelin_json.py에서 추출한 데이터를 list의 형태로 추출
  - hanchelin_json.py : json file에서 opening_hour만 추출
