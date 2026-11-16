# Flight ETA Predictor

A machine-learning system designed to predict flight arrival times using historical flight, aircraft, route, and weather data.

## Project Goal

Develop a model capable of predicting flight duration and arrival delay while minimizing prediction error.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Project Status

Added first ML model (Random Forest Regressor) and compared models results to the baseline model. See commit on 11/16/2026 for more info on additions.

Currently looking for weather data for the month of January in 2026. After seeing some results of the model, outliars in the data were skewed due to weather, specifically on Jan 26 in DFW (large amounts of snow and ice for over three days). Once that is complete, I will be expanding the total data to be more than just one month.

Important to note that this model is being trained exclusively on historical data. Eventually I plan on using predicted weather data but not now.