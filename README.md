# Spotify-History-Predictive-Analysis
Analyzed personal Spotify listening history to understand music preferences, listening trends, and engagement patterns. A machine learning model was developed to predict whether a song was skipped, adding a smart layer of insight into user behavior beyond basic statistics.

Skills, Tools & Techniques Used
🧠 Programming & Libraries
Python – Main language for data manipulation and modeling

Pandas – Data preprocessing, pipeline building, feature engineering

NumPy – Numerical operations

Scikit-learn – Modeling, pipelines, preprocessing, and evaluation

🔄 Data Engineering & Pipelines
Data Cleaning & Wrangling – From raw JSON to structured format

Scikit-learn Pipelines – Streamlined data processing and modeling flow

Custom Transformers – For modular and reusable steps (e.g., skip detection logic)

Cyclic Feature Encoding – Encoded time-based features like hour/day using sine & cosine transforms

📊 Feature Engineering
Ordinal Encoding & One-Hot Encoding – For categorical variables

Cyclic Encoding – For time features (hour, day, month) to capture periodicity

Interaction Features – Combining fields like "user-hour" or "track-duration"

🤖 Machine Learning
Classification Models – To predict if a track was skipped (e.g., Logistic Regression, Random Forest, etc.)

 Cross-Validation – For reliable model evaluation

Hyperparameter Tuning – Used GridSearchCV to optimize model performance

Model Evaluation – Accuracy, Precision, Recall, F1, Confusion Matrix

📈 Visualization & Analysis
Matplotlib / Seaborn / Plotly – For EDA and visualizing trends

Time-Series Analysis – Analyze behavior over hour/day/month

User Behavior Patterns – Identified skip behavior, top tracks, and listening sessions

At the end i deployed the model using flask framework

