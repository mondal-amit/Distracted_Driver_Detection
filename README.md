# 🚗 Distracted Driver Detection

A deep learning project to detect distracted driving behaviors from images and videos using Convolutional Neural Networks (CNNs). This system classifies whether a driver is focused or distracted (e.g., texting, talking on the phone, eating, etc.), aiming to improve road safety.

# 📌 Features
✅ Detects multiple distracted driver behaviors
✅ Built with TensorFlow/Keras CNN model
✅ Trained on State Farm Distracted Driver Dataset
✅ Includes real-time video simulation (Colab)
✅ Streamlit app for easy deployment & demo
✅ Organized folder structure for easy navigation

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

## 🛠️ Tech Stack
1. Python 3.9+
2. TensorFlow/Keras
3. OpenCV (video processing)
4. Streamlit (deployment)
5. Matplotlib/Seaborn (visualizations)

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

## 👨‍💻 Author
📩 amitmondal201889@gmail.com
ℹ️ www.linkedin.com/in/amit-mondal-672a4325b
