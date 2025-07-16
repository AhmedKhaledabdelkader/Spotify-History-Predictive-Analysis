
from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# ========== Custom Encoding Functions ==========

def cyclical_transform(X, period):
    X = np.asarray(X).astype(float)  # 👈 Convert to numeric array
    radians = 2 * np.pi * X / period
    return np.concatenate([np.sin(radians), np.cos(radians)], axis=1)

def encode_day_name(X):
    return cyclical_transform(X, 7)

def encode_day(X):
    return cyclical_transform(X, 31)

def encode_month(X):
    return cyclical_transform(X, 12)

def encode_hour(X):
    return cyclical_transform(X, 24)

def encode_quarter(X):
    return cyclical_transform(X, 4)

# ========== Load Model ==========
model = joblib.load("LGBM_best_model.h5")

# ========== Routes ==========
@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        day_name_map = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
        'Friday': 4, 'Saturday': 5, 'Sunday': 6
       }
        day_of_week=day_name_map[request.form["ts_day_name"]]
        try:
            input_data = {
                'platform': [request.form['platform']],
                'ms_played': [float(request.form['ms_played'])],
                'reason_start': [request.form['reason_start']],
                'reason_end': [request.form['reason_end']],
                'shuffle': [int(request.form['shuffle'])],
                'ts_year': [int(request.form['ts_year'])],
                'ts_month': [int(request.form['ts_month'])],
                'ts_day': [int(request.form['ts_day'])],
                'ts_day_name': [day_of_week],
                'ts_hour': [int(request.form['ts_hour'])],
                'ts_quarter': [int(request.form['ts_quarter'])]
            }

            input_df = pd.DataFrame(input_data)
            prediction = model.predict(input_df)[0]

        except Exception as e:
            error = str(e)
            print("🚨 ERROR:", e)

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
