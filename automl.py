import os
import streamlit as st
import pandas as pd
from utils import move_file
from data_preprocessing import clean_dataframe
from config import MODEL_DIR, RANDOM_SEED


def main():
    st.title('Welcome to Zizo AutoML')

    # Step 1: Ask for the data folder path
    data_folder_path = st.text_input("Enter the data folder path")
    
    if data_folder_path:
        # Read the uploaded file
        df = pd.read_csv(os.path.join(data_folder_path))

        # Display the first five rows of the dataframe
        st.write("First five rows of the dataset:")
        st.dataframe(df.head())

        df = clean_dataframe(df)
        st.write("Data Preprocessing Complete...")

        # Step 2: Ask user to select target column from a drop-down list of all columns from the data
        target_column = st.selectbox('Select the target column', df.columns)

        # Step 3: Ask user if it is a regression or classification problem
        task = st.radio("Select the problem type:", ('Regression', 'Classification'))

        # Step 4: Click button to start training
        if st.button('Start Training'):
            st.write('Training started...')
            # based on the problem_type. Integrate the AutoML training process.

            if task == 'Classification':
                from pycaret.classification import setup, compare_models, pull, save_model, plot_model
                clf = setup(data=df, target=target_column, session_id = RANDOM_SEED)

                best_model = compare_models()
                result = pull()
                result = result.iloc[0, :].reset_index()

                st.write('Best Model Found:')
                st.dataframe(result)  # Displaying the results as a DataFrame

                plot_model(best_model, plot='confusion_matrix', save=True)
                try:
                    plot_model(best_model, plot='feature', save=True)
                except:
                    pass
                plot_model(best_model, plot='auc', save=True)
                plot_model(best_model, plot='pr', save=True)
                plot_model(best_model, plot='learning', save=True)

                destination_dir, images_path = move_file(task)

                for image in images_path:
                    file_path = os.path.join(destination_dir, image)
                    file_name = file_path.split('/')[-1].split('.')[0]
                    st.image(file_path, caption=file_name)

                
            elif task == 'Regression':
                from pycaret.regression import setup, compare_models, pull, save_model, plot_model
                reg = setup(data=df, target=target_column, session_id = RANDOM_SEED)

                best_model = compare_models()
                result = pull()
                result = result.iloc[0, :].reset_index()

                st.write('Best Model Found:')
                st.dataframe(result)  # Displaying the results as a DataFrame

                plot_model(best_model, plot='residuals', save=True)
                plot_model(best_model, plot='error', save=True)
                try:
                    plot_model(best_model, plot='feature', save=True)
                except:
                    pass
                plot_model(best_model, plot='learning', save=True)

                destination_dir, images_path = move_file(task)

                for image in images_path:
                    file_path = os.path.join(destination_dir, image)
                    file_name = file_path.split('/')[-1].split('.')[0]
                    st.image(file_path, caption=file_name)

            # Save final model
            model_path = os.path.join(MODEL_DIR, f"{task.lower()}_model")
            save_model(best_model, model_path)

if __name__ == '__main__':
    main()
