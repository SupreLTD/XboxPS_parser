from flask import Flask, send_file

app = Flask(__name__)


@app.route('/get_csv_box')
def get_csv_box():
    return send_file('box.csv', as_attachment=True)


@app.route('/get_csv_ps')
def get_csv_ps():
    return send_file('ps.csv', as_attachment=True)


@app.route('/get_csv_ps_e')
def get_csv_ps_e():
    return send_file('ps_e.csv', as_attachment=True)


app.run(host="0.0.0.0")
