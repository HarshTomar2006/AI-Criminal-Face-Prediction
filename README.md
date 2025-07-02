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

## 📸 Demo Screenshot

![Demo Interface](https://github.com/HarshTomar2006/AI-Criminal-Face-Prediction/assets/demo-ui.png)

---

## 📽️ Demo Video (Add after uploading)

> 🎥 [Link to demo video](#) (Upload on YouTube or Drive)

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
4. 📑 Generates a PDF report
5. 💾 Saves all data to case history
6. 🗣️ Chatbot explains what was predicted & why

---

## 📁 Folder Structure

CriminalFace/
├── app.py # Streamlit main app
├── models/ # Trained GAN & ML models (ffhq.pkl - ignored)
├── utils/ # Helper functions, trait prediction logic
├── pages/ # Streamlit multipage support
├── assets/ # Images, icons, logos
├── chatbot/ # AI assistant module
├── history.json # Case history storage
├── requirements.txt # Dependencies
└── README.md # This file


---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/HarshTomar2006/AI-Criminal-Face-Prediction.git
cd AI-Criminal-Face-Prediction
pip install -r requirements.txt
streamlit run app.py

 
## 🔮 Future Scope
This project has vast potential across multiple domains:

Forensic Investigations: Predict criminal faces from DNA found at crime scenes — even without eyewitnesses or CCTV.

Border & National Security: Assist in identifying infiltrators or unknown suspects using DNA at border checkpoints or terrorist incidents.

Missing Person Cases: Help trace lost or abducted individuals by generating predictive facial images using biological samples.

Anti-Trafficking Units: Support human trafficking investigations by reconstructing identities of victims when only DNA evidence is available.

Post-Disaster Identification: Aid in identifying unknown deceased individuals during natural disasters or accidents using genetic material.

AI-Powered Police Tools: Can be integrated into law enforcement tools for faster suspect generation and narrowing down potential matches.

Genetic Research: Opens new possibilities in genetic trait visualization, ancestry reconstruction, and personalized medicine (with ethical safeguards).first-responders' decision making.

4. 🏥 Healthcare & Genetic Research
With ethical expansion, this model can support research on genetic conditions influencing facial traits, helping in early diagnosis.

## 🏆 Why It Should Win IDEA Hackathon 5.0
This project stands at the intersection of AI innovation, national security, and societal impact. Here's why it's a winning idea:

🚨 Real-World Relevance: Tackles pressing problems like criminal identification, missing persons, and national security using cutting-edge AI.

🤖 Technological Uniqueness: Combines DNA analysis with AI-generated face reconstruction — a rare and powerful integration not commonly seen in India.

🧬 Innovative Use of Data: Transforms raw biological data into meaningful visual output, aiding law enforcement beyond traditional methods.

🌍 High Impact Potential: Can scale to benefit border forces, anti-trafficking units, disaster recovery teams, and police investigations.

🚀 Ready for Real Deployment: Already working prototype with plans for API integration, ethical compliance, and real-world use cases.

This project is not just about code — it's about saving lives, solving crimes, and protecting our nation. It embodies the spirit of Make in India, AI for Good, and Digital Empowerment — perfectly aligned with the vision of IDEA Hackathon 5.0.

🙋‍♂️ Made by
Harsh Tomar
B.Tech AI/ML Enthusiast | Forensic Innovation Researcher
📧 harshtomat559@gmail.com
🔗 GitHub | LinkedIn

📜 License
MIT License



Can also be repurposed for heritage reconstructions or visualizations in ancestry/genetic studies.
