from flask import Flask, render_template, request
import os
from flask import Flask, flash, request, redirect, url_for
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image, ImageFile
from io import BytesIO
import base64

app = Flask(__name__)

app.config['SECRET_KEY'] = 'alskdfhgljxcl13513'
Up = 'files'
app.config["UPLOAD_FOLDER"] = Up

ALLOWED_EXTENSIONS = {'txt', 'pdf'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)



@app.route('/input_page')
def upload():
    return render_template('upload1.html')


@app.route('/next_page', methods=['GET', 'POST'])
def funct():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        elif file and allowed_file(file.filename):
            filename = file.filename
            # print(f" yeyey   {app.config['UPLOAD_FOLDER']}")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            file_content = open(os.path.join(app.config['UPLOAD_FOLDER'], filename),encoding=’cp437’,errors=”ignore”).read()

            wordcloud = WordCloud(  # font_path = r'C:\Windows\Fonts\Verdana.ttf',
                stopwords=STOPWORDS,
                background_color='black',
                width=1200,
                height=1000,
                color_func=random_color_func
            ).generate(file_content)
            '''plt.figure(figsize=(8, 8), facecolor=None)
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.tight_layout(pad=0)
            print("here")'''
            a = np.asarray(wordcloud)  # creating array from image object
            im = Image.fromarray(a)  # creating an img from an array object
            file_obj = BytesIO()  # creating a buffer of Input Output
            im.save(file_obj, 'PNG')  # saving image to buffer
            file_obj.seek(0)
            predicted = base64.b64encode(file_obj.getvalue()).decode('utf8')  # encoding image
            # plt.show()
            # plt.savefig('whatsapp.jpg')
            # return "<img src='whatsapp.jpg'/>"
            return render_template('wordcloud_out.html', plot_url0=predicted)  # render encoded image
        else:
            return render_template('wordcloud_out.html')
    else:
        return render_template('upload1.html')


@app.route('/index')
def output():
    return render_template('wordcloud_out.html')


if __name__ == '__main__':
    app.run(debug=True)
