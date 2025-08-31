# 🚗 Distracted Driver Detection

A deep learning project to detect distracted driver behaviors using CNNs.

## 📂 Project Structure
- `app/` → Streamlit web app
- `models/` → Trained models (`.keras`)
- `notebooks/` → Training Jupyter Notebooks
- `utils/` → Helper scripts (preprocessing, visualization)
- `reports/` → Project report & documentation

## ⚡ Quick Start
### 🔹 Local Run
```bash
pip install -r requirements.txt
cd app
streamlit run app.py
```

### 🔹 Colab Run
```bash
!streamlit run app/app.py & npx localtunnel --port 8501
```

### 🔹 Streamlit Cloud
1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Deploy by selecting `app/app.py`.

## 📊 Dataset
Kaggle's **State Farm Distracted Driver Detection** dataset.

## 📜 License
This project is licensed under the MIT License.
