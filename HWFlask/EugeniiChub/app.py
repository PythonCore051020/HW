from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
db = SQLAlchemy(app)




class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String)
    capacity = db.Column(db.Integer)

    def __repr__(self):
        return f"<{self.id} {self.room_name} {self.capacity}>"

    @staticmethod
    def create(room_name, capacity):
        room = Room()
        try:
            room.room_name = str(room_name)
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
    def update(pk, room_name=None, capacity=None):
        room = Room.get_by_id(pk)
        if not room_name == None:
            room.room_name = room_name
        if not capacity == None:
            room.capacity = capacity
        db.session.commit()

    @staticmethod
    def delete_by_id(pk):
        room = Room.get_by_id(pk)
        db.session.delete(room)
        db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    # teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=True)
    # teacher = db.relationship('Teacher', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"<{self.id} {self.first_name} {self.last_name} {self.age}>"

    @staticmethod
    def create(first_name, last_name, age):
        user = User()
        try:
            user.first_name = str(first_name)
            user.last_name = str(last_name)
            user.age = int(age)
        except ValueError:
            return None
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_id(pk):
        user = User.query.filter_by(id=pk).first()
        return user

    @staticmethod
    def update(pk, first_name=None, last_name=None, age=None):
        user = User.get_by_id(pk)
        if not first_name == None:
            user.first_name = first_name
        if not last_name == None:
            user.last_name = last_name
        if not age == None:
            user.age = age
        db.session.commit()

    @staticmethod
    def delete_by_id(pk):
        user = User.get_by_id(pk)
        db.session.delete(user)
        db.session.commit()


# class Teacher(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     position = db.Column(db.String)
#
#     def __repr__(self):
#         return f"<{self.id} {self.position}>"
#
#     @staticmethod
#     def create(position):
#         teacher = Teacher()
#         try:
#             teacher.position = str(position)
#         except ValueError:
#             return None
#         db.session.add(teacher)
#         db.session.commit()
#         return teacher
#
#     @staticmethod
#     def get_by_id(pk):
#         teacher = Teacher.query.filter_by(id=pk).first()
#         return teacher
#
#     @staticmethod
#     def update(pk, position=None):
#         teacher = Teacher.get_by_id(pk)
#         if not position == None:
#             teacher.position = position
#         db.session.commit()
#
#     @staticmethod
#     def delete_by_id(pk):
#         teacher = Teacher.get_by_id(pk)
#         db.session.delete(teacher)
#         db.session.commit()

# @app.route('/')
# def start_window():
#     return redirect('stwin.html')

@app.route('/')
def home():
    return redirect('/Room/room/')


@app.route('/Room/room/', methods=['GET', 'POST'])
def room():
    if request.method == 'GET':
        return render_template('Room/room_create.html')
    if request.method == 'POST':
        room_name = request.form['room']
        capacity = request.form['capacity']

        room = Room.create(room_name=room_name, capacity=capacity)
        if room:
            return redirect('/Room/room/list')
        return render_template('Room/room_create.html')


@app.route('/Room/room/list')
def room_list():
    rooms = Room.query.all()
    return render_template('Room/users.html', date=rooms)


@app.route('/Room/room/<pk>')
def room_by_id(pk):
    room = Room.get_by_id(pk)
    if room:
        return render_template('Room/user.html', date=room)


@app.route('/Room/room/update/<pk>', methods=['GET', 'POST'])
def room_update_by_id(pk):
    if request.method == 'GET':
        room = Room.get_by_id(pk)
        return render_template('Room/update_user.html', date=room)
    if request.method == 'POST':
        room_name = request.form['room']
        capacity = request.form['capacity']
        Room.update(pk, room_name=room_name, capacity=capacity)
        return redirect('Room/room/list')


@app.route('/Room/room/delete/<pk>')
def room_delete_by_id(pk):
    Room.delete_by_id(pk)
    return redirect('Room/room/list')

####################################################################
@app.route('/Users/user/', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return render_template('Users/user_create.html')
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']

        user = User.create(first_name=first_name, last_name=last_name, age=age)
        if user:
            return redirect('/Users/user/list')
        return render_template('Users/user_create.html')


@app.route('/Users/user/list')
def user_list():
    users = User.query.all()
    return render_template('Users/users.html', date=users)


@app.route('/Users/user/<pk>')
def user_by_id(pk):
    user = User.get_by_id(pk)
    if user:
        return render_template('Users/user.html', date=user)


@app.route('/Users/user/update/<pk>', methods=['GET', 'POST'])
def user_update_by_id(pk):
    if request.method == 'GET':
        user = User.get_by_id(pk)
        return render_template('Users/update_user.html', date=user)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        User.update(first_name=first_name, last_name=last_name, age=age)
        return redirect('/Users/user/list')


@app.route('/Users/user/delete/<pk>')
def user_delete_by_id(pk):
    User.delete_by_id(pk)
    return redirect('Users/user/list')


if __name__ == '__main__':
    db.create_all()
    app.run(port=8088)
