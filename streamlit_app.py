import streamlit as st
import pickle
from sklearn import pickle

def prediction(lst):
    filename = 'website/model/predictor1.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value[0]  # Return the first element of the prediction array

def main():
    st.title('Salary Prediction App')

    # Sidebar inputs
    age = st.number_input('Age', value=30, min_value=0, max_value=100)
    years_of_experience = st.number_input('Years of Experience', value=5, min_value=0, max_value=100)
    education_level = st.selectbox('Education Level', ["Bachelor's", "Master's", "PhD"])
    job_name = st.selectbox('Job Name', ["Analyst", "Business Analyst", "Business Development", "Data Scientist", "Director of Marketing", 
                                          "Director of Operations", "Finacial Analyst","Manager", "Marketing Analyst", "Marketing Coordinator", "Marketing Manager", 
                                          "Marketing Specialist", "Operations Analyst", "Operations Manager", "Product Manager", 
                                          "Project Manager", "Software Engineer", "Other"])

    if st.button('Predict Salary'):
        feature_list = [age, years_of_experience]
        # Convert education_level and job_name to one-hot encoding
        education_list = ["Bachelor's", "Master's", "PhD"]
        job_list = ["Analyst", "Business Analyst", "Business Development", "Data Scientist", "Director of Marketing", 
                    "Director of Operations", "Finacial Analyst","Manager", "Marketing Analyst", "Marketing Coordinator", "Marketing Manager", 
                    "Marketing Specialist", "Operations Analyst", "Operations Manager", "Product Manager", 
                    "Project Manager", "Software Engineer", "Other"]

        feature_list.extend([1 if education_level == edu else 0 for edu in education_list])
        feature_list.extend([1 if job_name == job else 0 for job in job_list])

        pred = prediction(feature_list)
        st.write(f'Predicted Salary: {pred}')

if __name__ == '__main__':
    main()
