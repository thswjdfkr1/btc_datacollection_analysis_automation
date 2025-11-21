import requests


def run_pipeline():
    url = "http://127.0.0.1:8000/api/btc_report"
    
    with open('C:/Users/thswj/Desktop/aa/btc_report.md', 'r', encoding='utf-8') as f:
              final_report = f.read()
    # 서버전송 
    response = requests.post(url, json={"btc_report": final_report})
    print("서버 응답:", response.status_code, response.text)

if __name__ == "__main__":
    run_pipeline()