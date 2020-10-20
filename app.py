from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth
from flask_fontawesome import FontAwesome
from setup import SetupForm
from flask_wtf.csrf import CSRFProtect
import os
from channel_conf import ChannelConfig
from user import User
from sprinkler import Sprinkler

auth = HTTPBasicAuth()
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
fa = FontAwesome(app)
app.config['SECRET_KEY'] = SECRET_KEY
#csrf = CSRFProtect(app)
csrf = CSRFProtect()
#csrf.init_app(app)
sprinkler = Sprinkler()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.verify_password
def verify_password(username, password):
    user = User()
    if username == user.username and \
            user.verify_password(password):
        return username


@app.route('/home', methods=["GET", "POST"])
@auth.login_required
def home():
    config = ChannelConfig().get_channels();
    for channel in config:
        if Sprinkler.get_state(channel["gpio"]) == 0:
            channel["state"] = True
        else:
            channel["state"] = False
    return render_template('home.html', config=config)


@app.route('/setup', methods=["GET", "POST"])
@auth.login_required
def setup():
    config = ChannelConfig()
    form = SetupForm()
    if request.method == "POST":
        req = request.form
        # channel 1
        gpio = req.get("gpio1")
        description = req.get("desc1")
        def_minutes = req.get("defmin1")
        config.set_channel("1", gpio, description, def_minutes)
        # channel 2
        gpio = req.get("gpio2")
        description = req.get("desc2")
        def_minutes = req.get("defmin2")
        config.set_channel("2", gpio, description, def_minutes)
        # channel 3
        gpio = req.get("gpio3")
        description = req.get("desc3")
        def_minutes = req.get("defmin3")
        config.set_channel("3", gpio, description, def_minutes)
        # channel 4
        gpio = req.get("gpio4")
        description = req.get("desc4")
        def_minutes = req.get("defmin4")
        config.set_channel("4", gpio, description, def_minutes)

        config.save()
        # print("gpio for channel one {}".format(req.get("gpio1")))
    elif request.method == "GET":
        d = config.get_channel("1")
        if d != {}:
            form.desc1.data = d["description"]
            form.gpio1.data = d["gpio"]
            form.defmin1.data = d['def_minutes']

        d = config.get_channel("2")
        if d != {}:
            form.desc2.data = d["description"]
            form.gpio2.data = d["gpio"]
            form.defmin2.data = d['def_minutes']

        d = config.get_channel("3")
        if d != {}:
            form.desc3.data = d["description"]
            form.gpio3.data = d["gpio"]
            form.defmin3.data = d['def_minutes']

        d = config.get_channel("4")
        if d != {}:
            form.desc4.data = d["description"]
            form.gpio4.data = d["gpio"]
            form.defmin4.data = d['def_minutes']

    return render_template("setup.html", form=form)


@app.route('/close', methods=['POST'])
# @auth.login_required
def close_spklr():
    channel = int(request.args.get('channel'))
    sprinkler.off(channel)
    return 'Closing channel...' + str(channel)


@app.route('/open', methods=['POST'])
# @auth.login_required
def open_spklr():
    channel = int(request.args.get('channel'))
    sprinkler.on(channel)
    return 'Opening channel...' + str(channel)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
