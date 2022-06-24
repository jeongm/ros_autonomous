from flask import Flask, session, render_template, redirect, request, url_for, flash
from models import db
import os
from models import User  # models.py에 있는 User 클래스

app = Flask(__name__)
app.secret_key = "abcdef"

@app.route('/')  # main페이지
def index():
    return render_template('index2.html')

# GET => 페이지가 나오도록 요청. POST = 버튼을 눌렀을 때 데이터를 가지고오는 요청, 요청정보를 확인하기 위해 request 모듈 사용
@app.route('/join',methods = ['GET','POST']) # 회원가입 - 원래 sign이었음, insert 해야 함
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else : # form 데이터 가져옴, POST, post는 http요청 메시지에서 body에 데이터를 담아 보냄
        # db전송
        user = User()
        user.userid = request.form.get('id') # get으로 전달된 데이터?? get은 url에 query string로 데이터가 넘어옴
        user.password = request.form.get('password')
        user.username = request.form.get('user_name')
        user.phone = request.form.get('phone_num')
        user.age = request.form.get('age')
        user.sex = request.form.get('SEX1')
        user.height = request.form.get('height')
        user.weight = request.form.get('weight')
        db.session.add(user)
        db.session.commit()
        flash("회원가입이 완료되었습니다.") # 왜 안됨???????
        return redirect(url_for('index')) 

@app.route('/signin', methods=['GET', 'POST']) # 로그인 - 원래 join이었는데 파일이름 임의로 바꿨음 헷갈려서
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    else : # POST
        userid = request.form['id'] 
        password = request.form['pw']
        data = User.query.filter_by(userid=userid, password=password).first() # ID/PW조회 Query 실행
        
        if data is not None: # 쿼리 데이터 존재시
            session['userid'] = userid # userid를 session에 저장
            return redirect(url_for('Dwrite'))
        else:
            flash("로그인 실패.")
            return render_template('signin.html')
        

@app.route('/signout', methods=['GET'])
def signout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/daywrite') # 식단기록, Daywright, 로그인하면 일로와야함
def daywrite():
    return render_template('Dwrite.html')

@app.route('/recommend') # 식단추천페이지
def recommend():
    return render_template('result.html')


if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__)) # database 경로를 절대경로로 설정
    dbfile = os.path.join(basedir, 'db.dqlite') # 데이터베이스 이름과 경로
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # 사용자에게 원하는 정보를 전달완료했을 떄가 TEARDOWN, 그 순간마다 COMMIT을 하도록 함=db반영
    # 여러가지 쌓아져있던 동작들을 Commit을 해주어야 데이터베이스에 반영됨. 이러한 단위들을 트렌젝션 이라고 함
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # True하면 warning 메시지 유발, 추가 메모리를 사용하므로 꺼둔다
    
    db.init_app(app) # app설정값 초기화
    db.app = app # Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
    db.create_all() # DB생성
    
    app.run(host='127.0.0.1', port=5000, debug=True)



