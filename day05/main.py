# FastAPI 다시
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # API 서버 시작

# 클래스 : 함수의 변형, 현재는 데이터 구조만
# 데이터 제대로 입력 검증
class studentModel(BaseModel):
   name: str # 이름을 문자열로 받음
   email: str # 이메일 문자열
   age: int # 나이는 정수
   major : str
   #str 문자열 (varchar)

   

@app.get('/') # 데코레이션
def read_root(): #root는 자동으로 / 을 붙임
   return {'message' : 'Hello FastAPI!'}

@app.get('/students') # 기본주소에 /값으로 요청하면 get_student 함수를 실행해라
def get_student():
   return [
     {'id':1, 'name':'김철수', 'major':'인공지능'},
     {'id':2, 'name':'이영희', 'major':'데이터분석'},
     {'id':3, 'name':'성유고', 'major':'컴퓨터공학'}
   ]  # 결과값 파이썬에서는 딕셔너리 / 자바스크립트.웹에서는 json

@app.get('/students/{id}')
def get_student(id: int):
   return {'student_id':id}

@app.get('/search')
def search_student(major: str | None = None):
   return {'major': major}


@app.post('/students')
def create_students(student: studentModel):
 return {
         'message' : '학생등록',
         'data':student
         }

@app.patch('/students/{id}')
def update_students(id: int):
   return {'message' : f'{id}번 학생 수정'}

@app.delete('/students/{id}')
def delete_students(id:int):
   return{ 'message' : f'{id}번 학생 삭제'}

