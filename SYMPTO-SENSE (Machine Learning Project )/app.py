from flask import Flask, request, render_template
from joblib import load
import json
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load('model\\MDD_using_catboost_model.joblib')

# Define the feature names
feature_names = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing',
    'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity',
    'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
    'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety',
    'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
    'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
    'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
    'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea',
    'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation',
    'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload',
    'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
    'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
    'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion',
    'chest_pain', 'weakness_in_limbs', 'fast_heart_rate',
    'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising',
    'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
    'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
    'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
    'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness',
    'stiff_neck', 'swelling_joints', 'movement_stiffness',
    'spinning_movements', 'loss_of_balance', 'unsteadiness',
    'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
    'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases',
    'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability',
    'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
    'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes',
    'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
    'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
    'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma',
    'stomach_bleeding', 'distention_of_abdomen',
    'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum',
    'prominent_veins_on_calf', 'palpitations', 'painful_walking',
    'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
    'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails',
    'blister', 'red_sore_around_nose', 'yellow_crust_ooze'
]

# File path of the JSON file
file_path = "model\disease_info.json"

# Load the dictionary from the JSON file
with open(file_path, "r") as file:
    disease_info = json.load(file)

def predict_disease(input_values):
    prediction = model.predict([input_values])
    disease_name = str(prediction[0])  # Convert to string to ensure it's hashable
    # Extract only the disease name without brackets or any additional characters
    disease_name = disease_name.strip("[]").replace("'", "")
    info = disease_info.get(disease_name, {})  # Get the information for the predicted disease
    description = info.get('description', 'No description available')
    precautions = info.get('precautions', 'No precautions available')
    medications = info.get('medications', 'No medications available')
    return disease_name, description, precautions, medications



@app.route('/')
def index():
    return render_template('index.html', feature_names=feature_names)

@app.route('/predict', methods=['POST'])

def predict():
    if request.method == 'POST':
        input_values = []
        search_input = request.form.get('search', '')  # Get the search input
        filtered_features = [feature for feature in feature_names if search_input.lower() in feature.lower()]
        
        for feature in filtered_features:
            input_value = request.form.get(feature, '0')  # Use '0' as default if the field is not present
            if input_value == '':
                input_value = '0'  # Use '0' as default if the field is empty
            input_values.append(int(input_value))

        # Convert input_values to a regular Python list
        input_values = np.array(input_values).tolist()

        prediction, description, precautions, medications = predict_disease(input_values)
        return render_template('index.html', feature_names=filtered_features, prediction=prediction, description=description, precautions=precautions, medications=medications)


if __name__ == '__main__':
    app.run(debug=True)
