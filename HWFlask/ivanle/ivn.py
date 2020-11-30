from flask import Flask, request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask import render_template



# http://127.0.0.1:2644/
app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)



class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    capacity = db.Column(db.Integer)

    def __repr__(self):
        return f"<{self.id} {self.name} {self.capacity}>"

    @staticmethod
    def create(name, capacity):
        room = Room()
        try:
            room.name = str(name)
            room.capacity = int(capacity)
        except ValueError:
            return None
        db.session.add(room)
        db.session.commit()
        return room

    @staticmethod
    def get_by_id(pk):
        room = Room.query.filter_by(id=pk).first()
        return room

    @staticmethod
    def update(pk, name=None, capacity=None):
        room = Room.get_by_id(pk)
        if not name == None:
            room.name = name
        if not capacity == None:
            room.capacity = capacity
        db.session.commit()

    @staticmethod
    def delete_by_id(pk):
        room = Room.get_by_id(pk)
        db.session.delete (room)
        db.session.commit()
  ###
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    surname = db.Column(db.String)
    age = db.Column (db.Integer)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=True)
    teacher = db.relationship('Teacher', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"<{self.id} {self.firstname} {self.surname} {self.age}>"

    @staticmethod
    def create(firstname, surname, age):
        user = User()
        try:
            user.firstname = str(firstname)
            user.surname = str(surname)
            user.age = int(age)
        except ValueError:
            return None
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def getuser_by_id (pk):
        user = User.query.filter_by(id=pk).first()
        return user

    @staticmethod
    def user_update(pk, firstname=None, surname=None, age=None):
        user = User.getuser_by_id(pk)
        if not firstname == None:
               user.firstname = firstname
        if not surname == None:
               user.surname = surname
        if not age == None:
               user.age = age
        db.session.commit()

    @staticmethod
    def delete_by_id(pk):
        user = User.getuser_by_id(pk)
        db.session.delete(user)
        db.session.commit()

### Teacher
class Teacher(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     position = db.Column(db.String)

     def __repr__(self):
        return f"<{self.id} {self.position}>"

     @staticmethod
     def create(position):
        teacher = Teacher()
        try:
           teacher.position = str(position)
        except ValueError:
           return None
        db.session.add(teacher)
        db.session.commit()
        return teacher

     @staticmethod
     def get_by_id(pk):
        teacher = Teacher.query.filter_by(id=pk).first()
        return teacher

     @staticmethod
     def update(pk, position=None):
         teacher = Teacher.get_by_id(pk)
         if not position == None:
               teacher.position = position
               db.session.commit()

     @staticmethod
     def delete_by_id(pk):
        teacher = Teacher.get_by_id(pk)
        db.session.delete(teacher)
        db.session.commit()

####Routes

@app.route ('/')
def index():
    return "Welcome students"

@app.route('/room', methods=['GET', 'POST'])
def room():
    if request.method == 'GET':
        return render_template('room_createi.html')
    if request.method == 'POST':
        name = request.form['room']
        capacity = request.form['capacity']

        room = Room.create(name=name, capacity=capacity)
        if room:
            return redirect('/room/list')
        return render_template('room_createi.html')

@app.route('/room/list')
def room_list():
    room = Room.query.all()
    return render_template('room_listi.html', date=room)

@app.route('/room/<pk>')
def room_by_id(pk):
    room = Room.get_by_id(pk)
    if room:
        return render_template('room_i.html', date=room)

@app.route('/room/delete/<pk>')
def room_delete_by_id(pk):
    Room.delete_by_id(pk)
    return redirect('/room/list')

####user
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return render_template('user_create.html')
    if request.method == 'POST':
        firstname = request.form['firstname']
        surname = request.form['surname']
        age = request.form['age']

        user = User.create(firstname=firstname, surname=surname, age=age)
        if user:
            return redirect('/user/list')
        return render_template('user_create.html')

@app.route('/user/list')
def user_list():
    user = User.query.all()
    return render_template('usr_list.html', date=user)

@app.route('/user/<pk>')
def user_by_id(pk):
    user = User.get_by_id(pk)
    if user:
        return render_template('user_i.html', date=user)

@app.route('/user/delete/<pk>')
def user_delete_by_id(pk):
        User.delete_by_id(pk)
        return redirect('/user/list')

#teacher

@app.route ('/teacher', methods=['GET','POST'])
def teacher():
    if request.method == 'GET':
        return render_template('teacher_create.html')
    if request.method == 'POST':
        position = request.form['position']



        teacher = Teacher.create(position=position)
        if teacher:
            return redirect('/teacher/list')
        return render_template('teacher_create.html')

@app.route('/teacher/list')
def teacher_list():
    teacher = Teacher.query.all()
    return render_template('teacher_list.html', date=teacher)

@app.route('/teacher/<pk>')
def teacher_by_id(pk):
    teacher = Teacher.get_by_id(pk)
    if teacher:
        return render_template('teacher.html', date=teacher)

@app.route('/teacher/delete/<pk>')
def teacher_delete_by_id(pk):
        Teacher.delete_by_id(pk)
        return redirect('/teacher/list')




if __name__ == '__main__':
    db.create_all()
    #r1 = Room(name="auditoria",capacity="40")
    #r2 = Room(name="dekanat",capacity="7")
    #db.session.add(r1)
    #db.session.add(r2)
    #db.session.commit()
    app.run(port=8088)






