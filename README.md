# 🛒 E-commerce Sales Prediction App

A Streamlit web application for predicting e-commerce sales based on various features. 📊

## ✨ Features

### 📝 Input Parameters
- 🆔 **CustomerID**: Unique identifier for each customer (Range: 0-10000)
- 📅 **DayOfWeek**: Day of the week when purchase was made (Range: 1-7)
  - 1 = Monday
  - 7 = Sunday
- 🕒 **Hour**: Hour of the day when purchase was made (Range: 0-23)
- 📆 **Month**: Month of the year (Range: 1-12)
- 💰 **UnitPrice**: Price per unit of product (Range: 0-1000)

### 🚀 Technical Features
- 🌐 Built with Streamlit for interactive web interface
- 🤖 Uses scikit-learn for machine learning model
- ⚡ Real-time predictions
- 🎯 User-friendly sidebar inputs
- ⚠️ Error handling and validation

## 🔧 Installation

1. Clone the repository
```bash
git clone <repository-url>
cd e-commerce-project
```

2. Create virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## 📖 Usage

1. Activate virtual environment:
```bash
.\venv\Scripts\activate
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser and navigate to:
```
http://localhost:8501
```

## 🤖 Model Details

- 📊 Type: Machine Learning Model (Random Forest/Linear Regression)
- 📈 Input Features: 5 features (CustomerID, DayOfWeek, Hour, Month, UnitPrice)
- 🎯 Output: Predicted sales value
- 💾 Model File: `model.pkl`

## 📦 Dependencies

- 🐍 Python 3.8+
- 🌐 streamlit==1.32.0
- 🐼 pandas==2.2.1
- 🔢 numpy==1.26.4
- 🤖 scikit-learn==1.3.2
- 🥒 pickle-mixin==1.0.2

## 📁 File Structure
```
e-commerce project/
├── app.py              # 🎯 Main Streamlit application
├── model.pkl          # 🤖 Trained machine learning model
├── requirements.txt   # 📦 Project dependencies
└── README.md         # 📖 Project documentation
```

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create your feature branch
3. 💾 Commit your changes
4. 🚀 Push to the branch
5. 🎯 Create a new Pull Request

## 📫 Support

For support, please open an issue in the repository or contact the maintainers.
