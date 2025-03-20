from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    link = request.form['link']
    yt = YouTube(link)
    title = yt.title
    views = yt.views
    yd = yt.streams.get_highest_resolution()
    if yd:
        yd.download()
        message = "Download complete."
    else:
        message = "No stream found."
    return render_template('result.html', title=title, views=views, message=message)

if __name__ == '__main__':
    app.run(debug=True)
