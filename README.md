# btc_datacollection_analysis_automation  

# 주제  
비트코인 가격 데이터 수집과 보고서 작성 자동화 알고리즘  

# 목표  
API를 활용한 비트코인 가격 데이터 수집과 LLM을 활용한 보고서 작성 자동화 및 웹페이지 게시  

# 구조
project/
│
├─ server.py                 # FastAPI 서버
├─ client.py                 # 보고서 전송 클라이언트
│
└─ aa/
   ├─ btc_report.md          # 생성된 Markdown 보고서
   └─ images/
        └─ chart_1301.png    # 차트/시각화 이미지
                 
# Finance API  
1. 데이터 수집  
   (1) BTCUSDT 5분봉 데이터 100개를 수집 시작  
   (2) 5분 간격으로 10번 반복하여 추가 데이터 수  
   
2. 데이터 전처리
   (1) 마지막 시간을 기준으로 중복 데이터 삭제
   (2) timestamp, open, high, low, close, volume 등 csv 파일로 저장  

# Tool  
1. 분석 함수  
   (1) 수익률
   (2) 변동률
   (3) 5분 이동 평균
   (4) RSI(상대 강도지수)
   (5) 거래량 변화율
   (6) 거래 금액   
   (7) 거래량 평균  

2. 시각화 함수
   - 마감가, 5분 이동 평균을 통한 그래프 생성
     
3. 보고서 생성 함수
   (1) 평균 수익률
   (2) 평균 변동률
   (3) RSI
   (4) 평균 거래량
   (5) 현재 종가
   (6) 분석 시간
   (7) 프롬프트  
       - 1. 최근 추세를 상승/하락/횡보 중 하나로 판단하고 근거를 제시해줘.
       - 2. 거래량과 변동성 간의 관계를 분석해줘.
       - 3. 단기 투자자 관점에서 리스크 요인을 2가지 제시해줘.
       - 4. 다음 시점(5분 후)에 대한 간략한 가격 전망을 작성해줘.
       - 5. 마지막으로 "요약 및 결론" 한 문장을 작성해줘
        - 전문적이고 보고서 스타일의 톤으로, 섹션별로 Markdown 형식으로 구분해줘.  
   
# Tool 정의 
```
tools = [
    Tool(
        name = 'Analysis_Data',
        func = analysis_data_summary,
        description = '비트코인 데이터 통계분석'
    ),
    Tool(
        name = "Create_Chart",
        func = create_chart,
        description = "비트코인 가격 차트 이미지"
    ),
    Tool(
        name = "Generate_Report",
        func = generate_report,
        description = "AI 보고서 생성"
    )
]
```  

# 에이전트 구성
```  
prompt = """당신은 비트코인 시장 분석 전문가입니다.
도구를 적절히 활용해 아래 요청에 답변하세요.
도구 사용이 끝나면 결과를 전문 보고서 형태로 Markdown으로 정리하세요."""
```

# 보고서 생성 및 저장
- 'gpt-4o-mini'

``` 
response = agent.invoke({"input" : "비트코인 시장 분석 보고서를 생성해줘."})
```
(1) 정의한 Tool과 LLM을 활용한 비트코인 분석 보고서 작성
(2) HTML, .MD 형식으로 생성된 보고서 저장  

# 웹페이지 게시  
(1) FastAPI를 활용한 서버 구축
(2) client 함수를 정의하여 서버에 게시
