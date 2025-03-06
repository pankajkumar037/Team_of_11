# 🏏 AI-Powered Fantasy Cricket Team Selector

## 📌 Overview

This AI-powered Streamlit app helps users select the best **Fantasy Cricket Team** based on match details and date. It utilizes multiple AI agents, including:

- **Web Agent** for fetching match-related data
- **Stats Agent** for analyzing player statistics
- **Fantasy Selector Agent** for final team recommendations

The app uses the **Gemini API** and **DuckDuckGo search tools** to enhance predictions.

---
## environment: conda activate team

## 🔧 Setup Instructions

### 1️⃣ Install Dependencies

Ensure you have Python installed, then run:

```sh
pip install -r requirements.txt
```

### 2️⃣ Set Up Environment Variables

Create a `.env` file in the root directory and add:

```
GOOGLE_API_KEY=your_google_api_key
```

### 3️⃣ Run the Streamlit App

Launch the application with:

```sh
streamlit run app.py
```

---

## 🚀 Usage Guide

1. **Enter Match Details** – Specify the teams playing (e.g., `UP Warriorz Women vs Mumbai Indians Women`).
2. **Select Match Date** – Choose the match date from the date picker.
3. **Generate Fantasy Team** – Click the button to receive a **recommended playing XI** with reasoning.
4. **View Results** – The AI will display the best fantasy team in a structured format.

---

## 📽️ Demo Video

Check out the demo video to see the app in action! 


---

## 📞 Contact & Support

For any issues or improvements, feel free to raise an **issue** or **pull request** in this repository. 🚀

