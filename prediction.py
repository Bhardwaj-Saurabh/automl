# import streamlit as st
# import os
# import pandas as pd
# from config import MODEL_DIR
# from pycaret.utils import load_model

# def predict(df, task):
#     # Assuming model is saved and named based on the task for simplicity
#     model_path = os.path.join(MODEL_DIR, f"{task.lower()}_model.pkl")
#     model = load_model(model_path)
    
#     # Creating a form for input data
#     with st.form("prediction_form"):
#         input_data = {}  # Dictionary to store input data

#         # Dynamically create input fields based on the features of the model
#         for feature in df.columns[:-1]:  # Assuming last column is target
#             # You can customize input types based on feature data types
#             input_data[feature] = st.text_input(f"Enter {feature}")
        
#         submitted = st.form_submit_button("Predict")
        
#         if submitted:
#             # Convert input data to DataFrame to match input expectation of PyCaret
#             input_df = pd.DataFrame([input_data])
#             input_df = input_df.apply(pd.to_numeric, errors='coerce')  # Convert inputs to numeric where possible
            
#             # Making prediction
#             prediction = model.predict(input_df)
            
#             # Display prediction
#             st.write(f"Prediction: {prediction}")

# if __name__ == '__main__':
#     predict()