from flask import Flask, render_template

from _8_composite_realisation import SubordinateAgent, DepartmentManager

app = Flask("Insurance")


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/employers")
def employers():
    _employers = list()
    mm_employer = DepartmentManager("Sinatra", "Frank")
    m_employer = DepartmentManager("Armstrong", "Luis")
    s_employer = SubordinateAgent("Benet", "Tony")
    m_employer.add_subordinate(s_employer)
    mm_employer.add_subordinate(m_employer)
    _employers.append(mm_employer)
    _employers.append(m_employer)
    _employers.append(s_employer)
    return render_template('employers.html', employers=_employers)

if __name__ == '__main__':
    app.run()

