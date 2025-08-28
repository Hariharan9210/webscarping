from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Scrape all headings h1 to h6
            data = [(tag.name, tag.text.strip()) for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        except Exception as e:
            data = [("Error", str(e))]
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
