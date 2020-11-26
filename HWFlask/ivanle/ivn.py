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
            room.size = int(capacity)
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
        if not size == None:
            room.capacity = capacity
        db.session.commit()

    @staticmethod
    def delete_by_id(pk):
        room = Room.get_by_id(pk)
        db.session.delete (room)
        db.session.commit()



@app.route('/room', methods=['GET', 'POST'])
def room():
    if request.method == 'GET':
        return render_template('room_create.html')
    if request.method == 'POST':
        name = request.form['room_name']
        capacity = request.form['capacity']

        room = Room.create(name=name, capacity=capacity)
        if room:
            return redirect('/room/list')
        return render_template('room_create.html')

@app.route('/room/list')
def room_list():
    room = Room.query.all()
    return render_template('room_list.html', date=room)

@app.route('/room/<pk>')
def room_by_id(pk):
    room = Room.get_by_id(pk)
    if room:
        return render_template('room.html', date=room)

@app.route('/room/delete/<pk>')
def room_delete_by_id(pk):
    Room.delete_by_id(pk)
    return redirect('/room/list')





if __name__ == '__main__':
    #db.create_all()
    #r1 = Room(name="auditoria",capacity="40")
    #r2 = Room(name="dekanat",capacity="7")
    #db.session.add(r1)
    #db.session.add(r2)
    #db.session.commit()
    app.run(port=8088)






