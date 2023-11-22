from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze/<category>')
def analyze(category):
    df = pd.read_csv('data.csv')

    plt.figure(figsize=(10, 5))
    if category == 'gender':
        column = 'sex'  # 성별 데이터가 있는 열
    elif category == 'age':
        column = 'age'  # 나이 데이터가 있는 열
    elif category == 'race':
        column = 'race'  # 인종 데이터가 있는 열
    else:
        return "Invalid category"

    df[column].hist()
    plt.title('Histogram of ' + category)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(False)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('analysis.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
