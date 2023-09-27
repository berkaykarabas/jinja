from flask import Flask,render_template
import datetime
import requests
app = Flask(__name__)

response = requests.get("https://api.agify.io/")
print(response)
@app.route("/")
def main():
    current_year = datetime.date.today().year
    return render_template(template_name_or_list="index.html",year=current_year)
@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data=gender_response.json()
    gender=gender_data["gender"]
    age_url=f"https://api.agify.io/?name={name}"
    age_response=requests.get(age_url)
    age_data=age_response.json()
    age=age_data["age"]
    country_url=f"https://api.nationalize.io/?name={name}"
    country_response = requests.get(country_url)
    country_data=country_response.json()
    country=country_data["country"][0]["country_id"]
    return render_template("guess.html",person_name=name,gender=gender,age=age,country=country)
@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("blog.html",all_data=data)
if __name__=="__main__":
    app.run(debug=True)
