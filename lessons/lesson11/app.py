from flask import Flask, request, render_template, redirect

app = Flask(__name__)
CITES = []
class City:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size

    @staticmethod
    def create(name, size):
        try:
            size = int(size)
        except:
            return None
        return City(name=name, size=size)

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
            CITES.append(city)
            return redirect('/city/list')
        return render_template('city_create.html')

@app.route('/city/list')
def city_list():
    return render_template('cities.html', date=CITES)



@app.route('/user/template')
def user_template():
    return render_template('hello.html', name="aaaa", bbbb=2222, date={"name": "Anna", "age": 22})


#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#

if __name__ == '__main__':
    app.run(port=8088)
