# %%
from flask import Flask, request, jsonify
from datetime import datetime, date, time, timedelta


app = Flask(__name__)


@app.route("/", methods = ["GET"])
def server_status():
    return "server is on."


@app.route("/until_next_meal/<meal>", methods = ["GET"])
def next_meal(meal):
    if meal == "breakfast":
        ans = breakfast_driver()
        return ans
    elif meal == "lunch":
        ans1 = lunch_driver()
        return ans1
    elif meal == "dinner":
        ans2 = dinner_driver()
        return ans2
    else:
        return "Check your spellings."


def breakfast_driver():
    breakfast_time = datetime.strptime("10:30:5", "%H:%M:%S")
    current_time = datetime.now()
    crnt = datetime.combine(date.today(), current_time.time())
    bft = datetime.combine(date.today(), breakfast_time.time())
    if crnt > bft:
        time_until = bft - crnt
        ans = time_until + timedelta(hours=24)
        ans1 = datetime.strptime((str(ans)), "%H:%M:%S.%f")
        ans2 = float(ans1.hour)
        print("Time until breakfast is {}".format(ans))
        return jsonify(ans2)
    elif bft > crnt:
        time_until1 = bft - crnt
        ans1 = datetime.strptime(str(time_until1), "%H:%M:%S.%f")
        ans2 = float(ans1.hour)
        print("Time until breakfast is {}".format(time_until1))
        return jsonify(ans2)


def lunch_driver():
    lunch_time = datetime.strptime("13:45:00", "%H:%M:%S")
    current_time = datetime.now()
    crnt = datetime.combine(date.today(), current_time.time())
    lnt = datetime.combine(date.today(), lunch_time.time())
    if crnt > lnt:
        time_until = lnt - crnt
        ans = time_until + timedelta(hours=24)
        ans1 = datetime.strptime((str(ans)), "%H:%M:%S.%f")
        ans2 = float(ans1.hour)
        print("Time until lunch is {}".format(ans))
        return jsonify(ans2)
    elif lnt > crnt:
        time_until1 = lnt - crnt
        ans1 = datetime.strptime(str(time_until1), "%H:%M:%S.%f")
        ans2 = float(ans1.hour)
        print("Time until lunch is {}".format(time_until1))
        return jsonify(ans2)


def dinner_driver():
    dinner_time = datetime.strptime("19:00:00", "%H:%M:%S")
    current_time = datetime.now()
    crnt = datetime.combine(date.today(), current_time.time())
    dnt = datetime.combine(date.today(), dinner_time.time())
    if crnt > dnt:
        time_until = dnt - crnt
        ans = time_until + timedelta(hours=24)
        ans1 = datetime.strptime((str(ans)), "%H:%M:%S.%f")
        ans2 = float(ans1.hour)
        print("Time until dinner is {}".format(ans))
        return jsonify(ans2)
    elif dnt > crnt:
        time_until1 = dnt - crnt
        ans1 = datetime.strptime(str(time_until1), "%H:%M:%S.%f")
        ans2 = float(ans1.hour)
        print("Time until dinner is {}".format(time_until1))
        return jsonify(ans2)


if __name__ == "__main__":
    app.run()
