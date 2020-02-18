from flask import Flask, render_template, render_template_string
import os

app = Flask(__name__)


@app.route("/hi")
def hello():
    return "hi"


@app.route('/index')
def index():
    # 将模板内容响应给用户
    return render_template('index.html')
    # 渲染一内容响应给用户
    # return render_template_string('<h1 style="color:green;font-size:18px;">原谅色</h1>')


@app.route('/')
def pubu():
    # 将模板内容响应给用户
    return render_template('pubu.html')
    # 渲染一内容响应给用户
    # return render_template_string('<h1 style="color:green;font-size:18px;">原谅色</h1>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
