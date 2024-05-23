
import pandas as pd
import joblib

model_path = 'C:/Users/bnice/OneDrive/Desktop/sample_project1/loan_data.pkl'
transformer_path = 'C:/Users/bnice/OneDrive/Desktop/sample_project1/column_transformer.pkl'

# Load the model and transformer
model = joblib.load(model_path)
transformer = joblib.load(transformer_path)

def get_data_ready(features):
#      loan_data = pd.DataFrame([features], columns=[
#         'credit.policy', 'purpose', 'int.rate', 'installment', 'log.annual.inc',
#         'dti', 'fico', 'days.with.cr.line', 'revol.bal', 'revol.util',
#         'inq.last.6mths', 'delinq.2yrs', 'pub.rec'
#     ])
#      transformed_loan_data = transformer.transform(loan_data)
#      return transformed_loan_data

# def predictor(features):
#      transformed_features = get_data_ready(features)
#      prediction = model.predict(transformed_features)
     # return prediction[0].item()
     return {
          "Test":"Works"
     }
