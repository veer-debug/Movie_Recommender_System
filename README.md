# 🎬 Movie Recommender System

## 🚀 Project Overview

The **Movie Recommender System** is a machine learning-based application designed to provide personalized movie suggestions. By analyzing user behavior and film data, the system predicts user preferences, offering tailored movie recommendations that enhance user satisfaction. The system learns from users' viewing history, continuously improving its predictions.

## 🎯 Features

- **Personalized Recommendations**: Provides movie suggestions based on users' past behavior and preferences.
- **Data-Driven Insights**: Utilizes film metadata, user ratings, and behavioral patterns to predict movie preferences.
- **Continuous Learning**: The model adapts and improves over time as more user data is accumulated.

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - **Scikit-Learn**: For building and evaluating the machine learning models.
  - **Pandas**: For data manipulation and analysis.
  - **Surprise**: For building collaborative filtering models.
  - **Flask**: For deploying the recommendation system as a web application.
  - **HTML/CSS**: For creating the web interface.

## 📁 Project Structure


- `data/`: Contains the datasets used for training and testing the model.
- `src/`: Source code for data preprocessing, model training, recommendation logic, and the Flask app.
- `templates/`: HTML templates for the web application.
- `models/`: Saved models for making recommendations.

## 🚀 How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Movie_Recommender_System.git
   cd Movie_Recommender_System
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
3. **Run the Flask App**:
    ```bash
    python src/app.py
4. **Access the Web Application**:
- Open your browser and go to http://localhost:5000.

## 📊 Results

The system provides personalized movie recommendations by accurately predicting user preferences based on viewing history and film data. It continuously improves its recommendations as it learns more from user interactions.

## 🔮 Future Work

- Integrate more advanced machine learning algorithms, such as deep learning models, for better predictions.
- Expand the recommendation system to include TV shows and other media types.
- Implement real-time recommendation updates based on user interactions.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.
