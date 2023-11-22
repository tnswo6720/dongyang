from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)

@app.route('/')
def home():
    # 데이터 분석
    df = pd.read_csv('data.csv')  # 'data.csv'는 분석하려는 데이터 파일입니다.
    summary = df.describe()

    # 데이터 시각화
    plt.figure(figsize=(10, 5))
    df['column'].hist()  # 'column'은 분석하려는 열 이름입니다.
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(False)
    plt.tight_layout()

    # Matplotlib 그래프를 이미지 파일로 변환하여 HTML에서 사용할 수 있게 합니다.
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('index.html', summary=summary, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
