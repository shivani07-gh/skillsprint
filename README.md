# 🚀 SkillsPrint

# Live Demo (Version 1)

A basic working version (**Version 1**) of **SkillsPrint** has been deployed for testing and demonstration purposes.

🔗 **Live Application:** https://skillsprint-vs.onrender.com

> **Learn Concepts. Practice Infinitely. Crack Placements.**

SkillsPrint is an AI-powered placement preparation platform designed to help students prepare for aptitude exams through **structured learning**, **concept-based practice**, and **dynamic AI-generated questions**.

Unlike traditional aptitude websites that rely on static question banks, SkillsPrint ensures students **understand concepts rather than memorize answers** by generating fresh questions while maintaining the same topic, pattern, and difficulty level.

---

## 📖 Table of Contents

- Overview
- Problem Statement
- Solution
- Learning Flow
- Features
- AI-Powered Question Generation
- Project Structure
- Tech Stack
- Future Scope
- Installation
- Contributors
- License

---

# 📌 Overview

SkillsPrint provides a structured roadmap for placement preparation.

Students learn a concept through a curated YouTube tutorial, practice concept-specific questions, and evaluate themselves through topic-wise tests.

The platform uses Large Language Models (LLMs) to generate new questions based on predefined concepts, enabling unlimited practice without repeating the same questions.

---

# ❗ Problem Statement

Most aptitude platforms provide a fixed set of questions.

As students repeatedly practice those questions, they begin to memorize answers instead of understanding concepts.

This leads to:

- Repetitive practice
- Limited question variety
- Memorization instead of conceptual learning
- Poor preparation for unseen placement questions

---

# 💡 Solution

SkillsPrint combines structured learning with AI-powered question generation.

Students first understand a topic through a recommended YouTube tutorial and then practice AI-generated questions based on the selected concept and difficulty level.

Every practice session feels fresh while staying aligned with the curriculum.

---

# 🎯 Learning Flow

```text
Login / Signup
        │
        ▼
Dashboard
        │
        ▼
Choose Subject
(Arithmetic / Reasoning / Verbal)
        │
        ▼
Choose Topic
(Profit & Loss, Percentage, Time & Work...)
        │
        ▼
🎥 Watch Recommended YouTube Tutorial
        │
        ▼
📝 Practice
        │
        ▼
Choose Pattern / Subtopic
        │
        ▼
🤖 AI Generates New Questions
        │
        ▼
📊 Topic Test
        │
        ▼
📈 Progress & Analytics
```

---

# 📚 Subject Structure

```text
Arithmetic
│
├── Percentage
├── Profit & Loss
├── Time & Work
├── Time, Speed & Distance
├── Ratio & Proportion
├── Simple Interest
└── ...

Reasoning
│
├── Blood Relations
├── Coding-Decoding
├── Seating Arrangement
├── Direction Sense
└── ...

Verbal
│
├── Reading Comprehension
├── Synonyms
├── Antonyms
├── Sentence Correction
└── ...
```

---

# 🧠 Topic Structure

Example:

```text
Arithmetic
        │
        ▼
Profit & Loss
        │
        ├── 🎥 YouTube Tutorial
        │
        ├── Practice
        │      ├── Basic Profit & Loss
        │      ├── Discount
        │      ├── Marked Price
        │      ├── Successive Discount
        │      └── Net Percentage
        │
        └── 📊 Topic Test
```

---

# 📝 Practice System

Each pattern is divided into three difficulty levels.

Example:

```text
Net Percentage

Easy
15 Questions

Medium
10 Questions

Hard
5 Questions
```

Instead of repeatedly displaying the same static questions, SkillsPrint uses AI to generate **fresh questions** based on:

- Subject
- Topic
- Pattern
- Difficulty
- Seed Questions

Students therefore practice the concept rather than memorizing answers.

---

# 🤖 AI-Powered Question Generation

SkillsPrint does not allow AI to generate random aptitude questions.

Instead, it follows a guided generation approach.

The system provides the LLM with:

- Subject
- Topic
- Pattern
- Difficulty
- Curated reference questions

The AI then generates new questions that:

- Test the same concept
- Preserve the same difficulty level
- Use different values
- Introduce new real-world scenarios
- Generate unique options
- Provide the correct answer and explanation

This enables unlimited concept-based practice while maintaining curriculum quality.

---

# 📊 Topic Tests

Topic tests are generated dynamically.

Instead of fixed papers, SkillsPrint creates unique assessments using predefined topic blueprints.

Example:

```text
Profit & Loss Test

2 Basic Questions

2 Discount Questions

2 Marked Price Questions

2 Successive Discount Questions

2 Net Percentage Questions
```

Every learner receives a different test while maintaining balanced topic coverage.

---

# ✨ Features

- 🔐 Secure Authentication
- 📚 Subject-wise Learning
- 🎥 Curated YouTube Tutorials
- 📝 Pattern-wise Practice
- 🤖 AI-Generated Questions
- 📊 Dynamic Topic Tests
- 📈 Performance Analytics
- 🎯 Concept-Based Learning
- ♾️ Unlimited Practice
- 📱 Responsive UI

---

# 🛠️ Tech Stack

## Frontend

- React
- Vite
- Tailwind CSS
- React Router
- Axios

## Backend

- FastAPI
- SQLAlchemy
- JWT Authentication
- Pydantic

## Database

- SQLite
- MySQL (Planned)

## AI

- Large Language Models (LLMs)
- Prompt Engineering
- Dynamic Question Generation
- JSON Structured Outputs

---

# 📂 Project Structure

```text
skillsprint/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── assets/
│
├── backend/
│   ├── app/
│   │   ├── config/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── middleware/
│   │   └── utils/
│   │
│   ├── datasets/
│   └── requirements.txt
│
└── README.md
```

---

# 🌟 Why SkillsPrint?

Traditional Platforms

- Fixed question banks
- Memorization-based practice
- Repeated questions
- Limited learning experience

SkillsPrint

- Concept-based learning
- AI-generated fresh questions
- Unlimited practice
- Dynamic topic tests
- Personalized learning experience

---

# 🚀 Future Scope

- Adaptive Question Generation
- AI Performance Analysis
- Personalized Learning Paths
- Company-Specific Placement Preparation
- Coding Practice
- CS Fundamentals
- Interview Preparation
- Leaderboards & Gamification
- Mobile Application

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/skillsprint.git
```

Move into the project directory

```bash
cd skillsprint
```

### Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve SkillsPrint, feel free to:

- Fork the repository
- Create a feature branch
- Commit your changes
- Open a Pull Request

---

# 📄 License

This project is developed for educational and research purposes.

---

# 👩‍💻 Authors

**Shivani Barot**

B.Tech Computer Science Engineering

AI • Full Stack Development • EdTech • Placement Preparation

---

## ⭐ If you like this project, don't forget to star the repository!
