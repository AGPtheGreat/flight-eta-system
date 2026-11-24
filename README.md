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

Cloned project on my other PC, which is basically better in every way (Six cores vs four and more RAM). This will speed up ML training times by a significant amount. 

Working on expanding the dataset from the month of January through June of 2026. This will provide more seasonal variation in the data. I am doing this before adding a weather variable to see if that variable will improve the predictions by a significant margin. My prediction has been that the weather will improve predictions substantially, since there are major storms that cause delays all the time such as Jan 26, 2026 in DFW (large amounts of snow and ice for over three days).

Important to note that this model is being trained exclusively on historical data. Eventually I plan on using predicted weather data but not now.