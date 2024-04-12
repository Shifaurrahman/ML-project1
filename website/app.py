from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor1.pickle'
    with open(filename, 'rb') as file:
    
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value



@app.route('/', methods=['POST', 'GET'])
def index():
    pred=0
    if request.method == 'POST':
        Age = request.form['Age']
        YearsOfExperience = request.form['Years of Experience']
        EducationLevel = request.form['Education Level']
        jobName = request.form['job_name']
        

        feature_list = []

        feature_list.append(int(Age))
        feature_list.append(int(YearsOfExperience))
        

        Education_list = ["Bachelor's", "Master's", "PhD"]
        

        job_list = ["Analyst", "Business Analyst", "Business Development", "Data Scientist", "Director of Marketing", 
                    "Director of Operations", "Finacial Analyst","Manager", "Marketing Analyst", "Marketing Coordinator", "Marketing Manager", 
                    "Marketing Specialist", "Operations Analyst", "Operations Manager", "Product Manager", 
                    "Project Manager", "Software Engineer", "Other"]
        
        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse_list(Education_list,EducationLevel)
        traverse_list(job_list,jobName)

        
        pred = prediction(feature_list)
        pred=pred[0]
        

    return render_template("index.html",pred=pred)

if __name__ == '__main__':
    app.run(debug=True)
