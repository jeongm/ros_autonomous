# database 관련

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy() # SQLALchemy를 사용해 데이터베이스 저장

'''
class Question(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)

class Answer(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'cascade'))
    question = db.relationship('Question', backref=db.backref('answer_set', ))
    # question = db.relationship('Question', backref=db.backref('answer_set', casecade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
'''
class User(db.Model) : # user 테이블
    __table_name__ = 'user' # table 이름
    user_seq = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(200), unique=True, nullable=True) # id는 email형식으로 받자
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(150), nullable = False)
    phone = db.Column(db.String(150), unique=True, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    sex = db.Column(db.String(2), nullable = False)
    height = db.Column(db.Float(150), nullable = False)
    weight = db.Column(db.Float(150),  nullable = False)
    field1 = db.Column(db.Float(150),  nullable = False)
    field2 = db.Column(db.Float(150),  nullable = False)
    field3 = db.Column(db.Float(150),  nullable = False)
    field4 = db.Column(db.Float(150),  nullable = False)
    field5 = db.Column(db.Float(150),  nullable = False)
    field6 = db.Column(db.Float(150),  nullable = False)
    field7 = db.Column(db.Float(150),  nullable = False)
    field8 = db.Column(db.Float(150),  nullable = False)
    field9 = db.Column(db.Float(150),  nullable = False)
    field10 = db.Column(db.Float(150),  nullable = False)
    field11 = db.Column(db.Float(150),  nullable = False)
    field12 = db.Column(db.Float(150),  nullable = False)
    field13 = db.Column(db.Float(150),  nullable = False)
    field14 = db.Column(db.Float(150),  nullable = False)
    field15 = db.Column(db.Float(150),  nullable = False)
    field16 = db.Column(db.Float(150),  nullable = False)
    
    menu_Table = db.relationship("menu", backref="user") # 외래키 관계 선언
    rate_Table = db.relationship("rate", backref="user")

class Nutrition(db.Model) : # 음식 정보 테이블
    __table_name__ = 'nutrition' # table 이름
    food_seq = db.Column(db.Integer, primary_key=True) # food index와 같음
    foodname = db.Column(db.String(200), unique=True, nullable=True)
    category = db.Column(db.Float(150), nullable=False)
    gram = db.Column(db.Float(150), unique=True, nullable = False)
    kcal = db.Column(db.Float(150), unique=True, nullable = False)
    protein = db.Column(db.Float(150), nullable = False)
    fat = db.Column(db.Float(150), nullable = False)
    carbohydrate = db.Column(db.Float(150), nullable = False)
    sodium = db.Column(db.Float(150),  nullable = False)
    
    diet_Table = db.relationship("dietTable", backref="nutrition") # 외래키 관계 선언
    menu_Table = db.relationship("menu", backref="nutrition")

class DietTable(db.Model) : # 음식 조합 테이블
    __table_name__ = 'dietTable' # table 이름
    diet_seq = db.Column(db.Integer, primary_key=True)# food index와 같음
    food_index1 = db.Column(db.Integer, ForeignKey('nutrition.food_seq')) # 음식 정보 테이블의 인덱스와 관계설정 / 외래키
    food_index2 = db.Column(db.Integer, ForeignKey('nutrition.food_seq'))
    food_index3 = db.Column(db.Integer, ForeignKey('nutrition.food_seq'))
    field1 = db.Column(db.Float(150),  nullable = False)
    field2 = db.Column(db.Float(150),  nullable = False)
    field3 = db.Column(db.Float(150),  nullable = False)
    field4 = db.Column(db.Float(150),  nullable = False)
    field5 = db.Column(db.Float(150),  nullable = False)
    field6 = db.Column(db.Float(150),  nullable = False)
    field7 = db.Column(db.Float(150),  nullable = False)
    field8 = db.Column(db.Float(150),  nullable = False)
    field9 = db.Column(db.Float(150),  nullable = False)
    field10 = db.Column(db.Float(150),  nullable = False)
    field11 = db.Column(db.Float(150),  nullable = False)
    field12 = db.Column(db.Float(150),  nullable = False)
    field13 = db.Column(db.Float(150),  nullable = False)
    field14 = db.Column(db.Float(150),  nullable = False)
    field15 = db.Column(db.Float(150),  nullable = False)
    field16 = db.Column(db.Float(150),  nullable = False)


class Menu(db.Model) : # 식단 정보 테이블
    __table_name__ = 'menu' # table 이름
    menu_seq = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, ForeignKey('user.user_seq'))
    food_id = db.Column(db.Integer, ForeignKey('nutrition.food_seq'))
    date = db.Column(db.Date, nullable=True)

class AttainmentRate(db.Model) : # 달성률 테이블
    __table_name__ = 'rate' # table 이름
    rate_seq = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, ForeignKey('user.user_seq'))
    date = db.Column(db.Date, unique=True, nullable=True)
    A_rate = db.Column(db.Float(150),  nullable = False)
    kcal = db.Column(db.Float(150), unique=True, nullable = False)
    protein = db.Column(db.Float(150), nullable = False)
    fat = db.Column(db.Float(150), nullable = False)
    carbohydrate = db.Column(db.Float(150), nullable = False)
    sodium = db.Column(db.Float(150),  nullable = False)