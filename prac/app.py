from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, Main!'

@app.route('/home')
def home():
    return '''
    <h1>이건 h1 제목</h1>
    <p>이건 p 본문 </p>
    <a href="https://flask.palletsprojects.com">Flask 홈페이지 바로가기</a>
    '''
#    return 'Hello, World!'
    
@app.route('/user')
def user():
	return 'Hello, User!'


if __name__ == '__main__':
    app.run(debug=True)

	