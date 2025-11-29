# Information Retrieval System

An **information retrieval system** developed in **Python**, capable of indexing local text files and performing efficient searches using the **BM25** ranking model — similar to a basic search engine.  
The application includes a simple **desktop interface** to run queries and display ranked results.

![GUI](docs/images/principal-function.png)

---

## 🚀 Key Features

- Indexing of local `.txt` documents  
- Automatic construction of an **inverted index**  
- BM25 relevance scoring for search results  
- Stopword removal and tokenization using NLTK  
- Desktop interface for intuitive searching  
- Ranked results with snippet previews  
- Compatible with **Windows and Linux**

---

## 🧠 System Architecture

The system is built around three main components:

### 📄 Document Processor
- Loads `.txt` files  
- Cleans text (lowercasing, stopwords, tokenization)  
- Builds the inverted index  

### 🔍 Retrieval Engine
- Processes user queries  
- Computes relevance using **BM25**  
- Sorts documents by ranking score  

### 🖥️ Desktop Interface
- Allows the user to input queries  
- Displays ranked results  
- Shows preview snippets  

---

## 🛠️ Installation

### 1️⃣ Clone the repository
```
git clone https://github.com/StivenJM/InformationRetrievalSystem.git
cd InformationRetrievalSystem
```

### 2️⃣ Create a virtual environment (optional but recommended)

#### Windows
```
py -m venv .venv
.venv/Scripts/Activate.ps1
```

#### Linux / WSL
```
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

Or run the setup script:

```
py setup_project.py
```

---

## ▶️ Running the Application

With the virtual environment activated:

```
py main.py
```

Or on Linux:

```
python3 main.py
```

---

## 📘 How the Search Works

1. Documents are preprocessed (lowercasing, stopwords, tokenization).  
2. An inverted index is built.  
3. User queries go through the same preprocessing.  
4. Candidate documents are retrieved.  
5. BM25 scores are computed for each document.  
6. Results are sorted and displayed with previews.

---

## 🧩 Technologies Used

- **Python 3**  
- **NLTK** – text preprocessing  
- **Tkinter** or CLI – user interface  
- **BM25** – ranking model  

---

## ⚠️ Current Limitations

- Works only with `.txt` files  
- Not optimized for very large datasets  
- Does not use modern NLP models  
- Language support depends on installed stopwords  

---

## 🚧 Possible Improvements

- Support for PDF, Word, and other file types  
- Query autocomplete  
- Synonym or query expansion  
- Search history  
- Spell correction  
- More scalable architecture  

---

## 📄 License

This project is licensed under the **MIT License**.  
This allows you to use, copy, modify, merge, publish, distribute, and sublicense the software freely, as long as you retain the original copyright notice.

See the `LICENSE` file for more details.

---
