# genDummyReport
허레에는 허식으로...
별 쓸데도 없고 효과도 없고 생각도 없는 '허례'에 대응하기 위한 프로그램

## install

pip install -r requirements.txt

## How to use

### Terminal 에서 직접 실행하기
1. lab_safety_report.py파일을 열어 원하는 날짜로 변경

```
    generator.generate('./output/lab_safety_report.docx', 2021,4,10)
```

2. 실행
```
$ python lab_safety_report.py
```
3. 결과물 확인
output 디렉토리에 파일이 생김.

### 웹 브라우저에서 사용하기
1. streamlit 서버 실행
```
$ streamlit run streamlit_genReport.py
```
2. 웹 브라우저에서 관련 내용 입력하고, 생성 후 다운로드
 

### Future plan
실제 국경일/공휴일 반영
공공 포털에서 openAPI 써서 하면 되는데.. 일단은 귀찮으므로...