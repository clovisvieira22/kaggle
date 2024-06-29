import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

asd_train = pd.read_csv('seu_arquivo.csv')

categorical_features = ['Marital status', 'Application mode', 'Application order', 'Course', 
                        'Daytime/evening attendance', 'Previous qualification', 'Nacionality', 
                        "Mother's qualification", "Father's qualification", "Mother's occupation", 
                        "Father's occupation", 'Displaced', 'Educational special needs', 
                        'Debtor', 'Tuition fees up to date', 'Gender', 'Scholarship holder', 
                        'International']
numerical_features = ['Previous qualification (grade)', 'Admission grade', 'Age at enrollment', 
                      'Curricular units 1st sem (credited)', 'Curricular units 1st sem (enrolled)', 
                      'Curricular units 1st sem (evaluations)', 'Curricular units 1st sem (approved)', 
                      'Curricular units 1st sem (grade)', 'Curricular units 1st sem (without evaluations)', 
                      'Curricular units 2nd sem (credited)', 'Curricular units 2nd sem (enrolled)', 
                      'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (approved)', 
                      'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)', 
                      'Unemployment rate', 'Inflation rate', 'GDP']

asd_train[categorical_features] = asd_train[categorical_features].astype(str)

encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
encoded_categorical_data = encoder.fit_transform(asd_train[categorical_features])

encoded_categorical_df = pd.DataFrame(encoded_categorical_data, 
                                      columns=encoder.get_feature_names_out(categorical_features))

X = pd.concat([encoded_categorical_df.reset_index(drop=True), 
               asd_train[numerical_features].reset_index(drop=True)], axis=1)

X = X.fillna(0)

print("Tipos de dados de X:\n", X.dtypes)

y = asd_train['Target'].astype(float)  # Certifique-se de que o alvo é numérico

print("Tipo de dados de y:", y.dtypes)

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

print("Shape de train_X:", train_X.shape)
print("Shape de train_y:", train_y.shape)
print("Shape de val_X:", val_X.shape)
print("Shape de val_y:", val_y.shape)

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)

rf_val_predictions = forest_model.predict(val_X)

print("Previsões:", rf_val_predictions)
