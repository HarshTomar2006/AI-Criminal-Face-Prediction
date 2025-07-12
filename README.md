# 🧬 AI-Based Criminal Face Prediction from DNA
> IDEA Hackathon 5.0 – Revolutionizing Forensic Investigations with AI & GANs  
> **Built to Win 🏆 | MSME Innovation Challenge | ₹15 Lakh Grant Targeted**

![Project Banner](https://github.com/HarshTomar2006/AI-Criminal-Face-Prediction/assets/your-banner-image.png)

---

## 🧠 About the Project

What if **DNA alone** could help generate a **realistic face prediction** of an unknown suspect?  
This project merges **Genomics + AI + GANs** to **predict criminal facial traits** from genetic markers and generate a human face using advanced **StyleGAN2-ADA**.

> 📌 Empowering law enforcement with a futuristic tool to reduce unsolved crimes.

---

## 💡 Problem Statement

🚨 **98% of unknown suspects are never identified** in crimes without CCTV or witness evidence.  
🧬 DNA is available — but there's **no tool** to visualize the suspect.

> Our solution? Predict the **face**, **personality traits**, and **store full reports** — all from a DNA input!

---

## 🚀 Key Features

| Feature                             | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| 🔬 DNA-to-Trait Predictor            | Converts DNA data into phenotype traits like hair, eye color, etc.         |
| 🧠 AI-Based GAN Face Generator       | Generates a human-like face using StyleGAN2-ADA                            |
| 📃 Auto PDF Report Generation        | Summarized report including predicted traits and generated face            |
| 🧾 Save Case History                 | Stores all predictions with timestamp in a secure database or JSON         |
| 👤 Login & Authentication            | Secure login system for forensic experts                                   |
| 🧠 Chatbot Assistant (AI Explainer) | Chatbot explains the prediction to officers using simple terms             |
| 🌐 Hosted UI on Streamlit           | Accessible via browser — no install required                               |

---

## 📸 Demo Screenshots

📂 [Click here to view all screenshots](https://drive.google.com/drive/folders/1g3yyoEtEZJEemaFC21WBFfRBbcl4In3_?usp=drive_link)

---

## 📽️ Demo Video

🎥 [Watch Project Demo](https://drive.google.com/file/d/1_pVawRp8kvi6jc7gDnDQhCxMKNRFQ-rP/view?usp=drive_link)

---

## 🔧 Tech Stack

- 🧠 **AI Models**: StyleGAN2-ADA (PyTorch), Trait Predictor (XGBoost/ML)
- 💬 **Chatbot**: OpenAI / Langchain + Streamlit integration
- 🌐 **Frontend**: Streamlit + Streamlit Components
- 📂 **Backend**: Python, Pandas, Numpy, PIL
- 🛡️ **Auth & Storage**: Session state, SQLite / JSON

---

## 🧪 How It Works

1. 🧬 User selects traits (or uploads dummy DNA markers)  
2. 🧠 Traits mapped to visual properties (hair color, face structure, etc.)  
3. 🧑‍🎨 GAN generates realistic face  
4. 📑 PDF report is generated  
5. 💾 Case history stored securely  
6. 🗣️ Chatbot explains prediction to end-user

---

## 📁 Folder Structure

AI-Criminal-Face-Prediction/
├── app.py # Streamlit main app
├── models/ # Trained GAN & ML models
├── utils/ # Helper functions
├── pages/ # Streamlit multipage UI
├── assets/ # Images, icons
├── chatbot/ # AI chatbot module
├── history.json # Prediction storage
├── requirements.txt # Required dependencies
└── README.md # This file


---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/HarshTomar2006/AI-Criminal-Face-Prediction.git
cd AI-Criminal-Face-Prediction
pip install -r requirements.txt
streamlit run app.py

##🔮 Future Scope
Forensic Investigations: Predict faces from DNA in unsolved crimes

Border & National Security: Identify infiltrators using genetic evidence

Missing Person Recovery: Predict visuals for lost individuals

Anti-Trafficking Investigations

Disaster Victim Identification

AI Tools for Police Use

Genetic Research & Diagnosis

##🏆 Why It Should Win IDEA Hackathon 5.0
This project stands at the intersection of AI innovation, national security, and societal impact. Here's why it deserves to win:

🚨 Real-World Relevance – Fights crime and helps law enforcement

🤖 Tech Uniqueness – Rare combo of DNA + GAN face generation

🧬 Smart Use of Data – Turns DNA into action

🌍 Impact Potential – Scalable across multiple sectors

🚀 Deployment Ready – Working prototype with roadmap ahead

🇮🇳 Aligns with “Make in India”, “Digital India”, and “AI for Good” missions.


##🙋‍♂️ Made by
Harsh Tomar
B.Tech AI/ML Enthusiast | Forensic Innovation Researcher
📧 harshtomat559@gmail.com
🔗 GitHub: HarshTomar2006

##📜 License
MIT License — Free to use, build, or expand with credit.
