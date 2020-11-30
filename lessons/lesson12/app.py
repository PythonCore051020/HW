from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
db = SQLAlchemy(app)

CITES = []


class Base(db.Model):
    __abstract__ = True

    @classmethod
    def get_by_id(cls, pk):
        return cls.query.filter_by(id=pk).first()

    @classmethod
    def delete_by_id(cls, pk):
        element = cls.get_by_id(pk)
        db.session.delete(element)
        db.session.commit()

    @classmethod
    def update(cls, pk, **data):
        element = cls.get_by_id(pk)
        for key, value in data.items():
            setattr(element, key, value)
        try:
            db.session.commit()
        except Exception as e:
            print(f"{cls}, pk:{pk} data:{data}")

    @classmethod
    def create(cls, **data):
        element = cls()
        for key, value in data.items():
            setattr(element, key, value)
        try:
            db.session.add(element)
            db.session.commit()
        except Exception as e:
            print(f"{cls}  data:{data}")
        return element


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    size = db.Column(db.Integer)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    country = db.relationship('Country', backref=db.backref('cities', lazy=True))

    def __repr__(self):
        return f"<{self.id} {self.name} {self.size}>"

    @staticmethod
    def create(name, size):
        city = City()
        try:
            city.name = str(name)
            city.size = int(size)
        except ValueError:
            return None
        db.session.add(city)
        db.session.commit()
        return city

    @staticmethod
    def get_by_id(pk):
        city = City.query.filter_by(id=pk).first()
        return city

    @staticmethod
    def update(pk, name=None, size=None):
        city = City.get_by_id(pk)
        if not name == None:
            city.name = name
        if not size == None:
            city.size = size
        db.session.commit()

    @staticmethod
    def delete_by_id(pk):
        city = City.get_by_id(pk)
        db.session.delete(city)
        db.session.commit()


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"<{self.id} {self.name}>"

    @staticmethod
    def create(name):
        country = Country()
        try:
            country.name = str(name)
        except ValueError:
            return None
        db.session.add(country)
        db.session.commit()
        return country

    @staticmethod
    def get_by_id(pk):
        country = Country.query.filter_by(id=pk).first()
        return country

    @staticmethod
    def update(pk, name=None):
        country = Country.get_by_id(pk)
        if not name == None:
            country.name = name
        db.session.commit()

    @staticmethod
    def delete_by_id(pk):
        country = Country.get_by_id(pk)
        db.session.delete(country)
        db.session.commit()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f"User {username}"


@app.route('/user/<firs_name>/<last_name>')
def show_user_profile2(firs_name, last_name):
    # show the user profile for that user
    return f"User {firs_name} {last_name}"


@app.route('/city', methods=['GET', 'POST'])
def city():
    if request.method == 'GET':
        return render_template('city_create.html')
    if request.method == 'POST':
        name = request.form['city']
        size = request.form['size']

        city = City.create(name=name, size=size)
        if city:
            return redirect('/city/list')
        return render_template('city_create.html')


@app.route('/city/list')
def city_list():
    cities = City.query.all()
    # countries = Country.query.all()
    # date = []
    # for city in cities:
    #     country_name = None
    #     for country in countries:
    #         if country.id == city.country_id:
    #             country_name = country.name
    #     element = {
    #         "id": city.id,
    #         "name": city.name,
    #         "size": city.size,
    #         "country": country_name,
    #         "country_id": city.country_id
    #     }
    #     date.append(element)
    # return render_template('cities.html', date=date)
    return render_template('cities.html', date=cities)


@app.route('/city/<pk>')
def city_by_id(pk):
    city = City.get_by_id(pk)
    if city:
        return render_template('city.html', date=city)


@app.route('/city/update/<pk>', methods=['GET', 'POST'])
def city_update_by_id(pk):
    if request.method == 'GET':
        city = City.get_by_id(pk)
        return render_template('update_city.html', date=city)
    if request.method == 'POST':
        name = request.form['city']
        size = request.form['size']
        City.update(pk, name=name, size=size)
        return redirect('/city/list') \
 \
 \
@app.route('/city/delete/<pk>')
def city_delete_by_id(pk):
    City.delete_by_id(pk)
    return redirect('/city/list')


@app.route('/user/template')
def user_template():
    return render_template('hello.html', name="aaaa", bbbb=2222, date={"name": "Anna", "age": 22})


@app.route('/country/list')
def country_list():
    countries = Country.query.all()
    return render_template('country/countries_list.html', countries=countries)


@app.route('/country/<pk>')
def country_by_id(pk):
    country = Country.get_by_id(pk)
    # cityes = [city for city in City.query.all() if  city.country_id == country.id]
    if country:
        return render_template('country/country.html', country=country)


#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#

if __name__ == '__main__':
    db.create_all()

    # c1 = City(name="Lviv", size=890_000)
    # c2 = City(name="Odesa", size="1_890_000")
    # db.session.add(c1)
    # db.session.add(c2)
    # db.session.commit()
    # s = City.query.all()
    # for i in s:
    #     print(i)
    app.run(port=8088)
