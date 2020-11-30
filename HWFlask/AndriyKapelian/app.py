from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
db = SQLAlchemy(app)


class Room(db.Model):
    room_id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String)
    room_capacity = db.Column(db.Integer)

    def __repr__(self):
        return f"<{self.room_id} {self.room_name} {self.room_capacity}>"

    @staticmethod
    def create(room_name, room_capacity):
        new_room = Room()
        try:
            new_room.room_name = str(room_name)
            new_room.room_capacity = int(room_capacity)
        except ValueError:
            return None
        db.session.add(new_room)
        db.session.commit()
        return new_room

    @staticmethod
    def get_by_id(pk):
        room_row = Room.query.filter_by(room_id=pk).first()
        return room_row

    @staticmethod
    def update(pk, room_name=None, room_capacity=None):
        room_row = Room.get_by_id(pk)
        if not room_name == None:
            room_row.room_name = room_name
        if not room_capacity == None:
            room_row.room_capacity = room_capacity
        db.session.commit()

    @staticmethod
    def delete_by_id(pk):
        room_row = Room.get_by_id(pk)
        db.session.delete(room_row)
        db.session.commit()


@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/room', methods=['GET', 'POST'])
def room():
    if request.method == 'GET':
        return render_template('room/room_create.html')
    if request.method == 'POST':
        room_name = request.form['room_name']
        room_capacity = request.form['room_capacity']

        new_room = Room.create(room_name=room_name, room_capacity=room_capacity)
        if new_room:
            return redirect('/room/list')
        return render_template('room/room_create.html')


@app.route('/room/list')
def room_list():
    rooms = Room.query.all()
    return render_template('room/room_list.html', rooms=rooms)


@app.route('/room/<pk>')
def room_by_id(pk):
    room_row = Room.get_by_id(pk)
    if room_row:
        return render_template('room/room.html', date=room_row)


@app.route('/room/update/<pk>', methods=['GET', 'POST'])
def room_update_by_id(pk):
    if request.method == 'GET':
        room_row = Room.get_by_id(pk)
        return render_template('room/room_update.html', rooms=room_row)
    if request.method == 'POST':
        room_name = request.form['name']
        room_capacity = request.form['capacity']
        Room.update(pk, room_name=room_name, room_capacity=room_capacity)
        return redirect('/room/list')



@app.route('/room/delete/<pk>')
def room_delete_by_id(pk):
    Room.delete_by_id(pk)
    return redirect('/room/list')


if __name__ == '__main__':
    #db.create_all()

    app.run(port=8088)
