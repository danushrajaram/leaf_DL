# 🌿 Leaf Disease Prediction Project 🌿

[Danush Rajaram](https://www.linkedin.com/in/danushrajaram) - I am active on LinkedIn! Follow me to connect, share, and exchange ideas 🌟

---

## 🌟 Project Overview

This project leverages deep learning to classify leaf conditions into three categories: **Healthy**, **Powdery Mildew**, and **Rust**. The model is deployed through a **Streamlit web application** for user interaction and a **Flask API** for programmatic access. The solution is powered by a TensorFlow model trained using a dataset from Kaggle.

---

## 📁 Project Structure

```
Project Root
├── app.py                # Streamlit web application
├── api.py                # Flask API
├── requirements.txt      # Dependencies
├── data_extraction.ipynb # Jupyter Notebook for training and exporting the model
└── cmd.txt               # Key setup commands
```

1. **GitHub Deployment:** Instructions for managing large files (e.g., model files) while pushing to GitHub.

---

## 🚀 Getting Started

### ✅ Prerequisites

1. Python (version 3.7+)
2. TensorFlow 2.x
3. Streamlit
4. Flask
5. Kaggle JSON API key for data extraction

---

### 🛠️ Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/leaf-disease-prediction.git
cd leaf-disease-prediction
```

#### 2. Create and Activate a Virtual Environment

```bash
# Check Python version
python --version

# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scriptsctivate
# On macOS/Linux:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Download Kaggle Dataset

- Place the Kaggle authentication JSON file in the working directory.
- Run `data_extraction.ipynb` in Google Colab to train and download the model.

---

## 💻 Usage

### 🎨 Streamlit App

1. Run the app:
   ```bash
   streamlit run app.py
   ```
2. Open the link displayed in the terminal to access the web UI.
3. Upload a leaf image to receive predictions and confidence scores.

### 🔧 Flask API

1. Run the API:
   ```bash
   python api.py
   ```
2. Use tools like Postman to send a POST request to `http://127.0.0.1:5000/predict` with an image file.
3. Example response:
   ```json
   {
       "prediction": "Healthy",
       "confidence": 0.95
   }
   ```

---

## 📤 Deployment

### 📦 Handling Large Files in GitHub

Since the trained model file exceeds 25 MB, use **Git Large File Storage (LFS):**

1. Install Git LFS:
   ```bash
   git lfs install
   ```
2. Track the model file:
   ```bash
   git lfs track "*.keras"
   ```
3. Add and push files:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

### 🌐 Streamlit Cloud Deployment

1. Push the repository to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and link your GitHub repository.
3. Deploy the app and access it via the provided URL.

---

## 📝 Files Description

### `app.py`

A Streamlit application for users to upload images and receive predictions visually. Key features include:

- Image upload and display.
- Deep learning model integration.
- Displaying prediction results with confidence scores.

### `api.py`

A Flask-based API to programmatically predict leaf diseases. Key features include:

- POST endpoint `/predict` for image upload.
- Returns prediction and confidence as JSON.

### `data_extraction.ipynb`

A Jupyter Notebook for:

- Extracting data from Kaggle using API credentials.
- Training the TensorFlow model.
- Exporting the trained model for deployment.

---

## 📜 Commands

All essential commands for setup are provided in `cmd.txt` for easy reference, including:

- Virtual environment setup.
- Pip installation and upgrades.
- Running Streamlit and Flask.

---

## ✍️ Author

**Danush Rajaram**
