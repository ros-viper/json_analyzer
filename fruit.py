from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/')
def test_json():
    raw_file = open('d:/Flask/static/fruit.json', encoding='utf-8').read()
    jsn_file = json.loads(raw_file)

    new_dict = {}
    years = sorted(list(set([str(x['Год']) for x in jsn_file['data']])))

    for year in years:
        new_dict.update({year:[{i['Фрукт']:i['Значение']} for i in jsn_file['data'] if i['Год'] == year]})

    first_year = years[0]
    first_fruits = []

    for year, fruits in new_dict.items():
        if year == first_year:
            for fruit in fruits:
                first_fruits.append(fruit)
    

    return render_template('test_json.html', data=new_dict, years=years, first_year=first_year, first_fruits=first_fruits)