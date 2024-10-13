
# **KnowGenAI - Knowledge Base Generator with RAG and ICL**

KnowGenAI is a Python-based project designed to generate JSON-formatted knowledge bases from question-answer pairs. It now integrates advanced techniques like **Retrieval-Augmented Generation (RAG)** and **In-Context Learning (ICL)** for enhanced information retrieval and dynamic question answering with large language models (LLMs).

![App](image/app.png)

![API](image/api.png)

![Generated JSON file](image/json_kb.png)

## **Features**
- **Generate JSON files**: Convert question-answer pairs into structured JSON files, with metadata like `title`, `segment`, and `journey`.
- **Export to ZIP**: Automatically export generated JSON files into a ZIP archive.
- **RAG-Enhanced Knowledge Base**: The project includes functionality to create embeddings and store them in a vector database for semantic search and RAG implementation.
- **In-Context Learning**: Provide context and examples to LLMs, using question-answer examples from the knowledge base for dynamic generation.
- **Gradio-based UI**: A simple Gradio-based interface for uploading question-answer sets and downloading knowledge base files.

## **Table of Contents**
- [Installation](#installation)
- [Usage](#usage)
- [Gradio Interface](#gradio-interface)
- [Knowledge Base Structure](#knowledge-base-structure)
- [RAG & ICL Integration](#rag--icl-integration)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/knowgenai.git
cd knowgenai
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Install Additional Libraries for RAG**
If you're using RAG, install the required libraries for embeddings and vector databases:
```bash
pip install faiss-cpu sentence-transformers pinecone-client
```

## **Usage**

### **1. Running the Gradio Interface**
To launch the Gradio interface, run the following:
```bash
python app.py
```

Once the app is running, you can access the Gradio UI in your browser, allowing you to:
- Input question-answer pairs.
- Generate and download a ZIP file containing the JSON knowledge base.

### **2. Input Format**
Provide question-answer pairs in the following format:
```
Pergunta: What is quantum physics?
Resposta: Quantum physics is the branch of physics dealing with the smallest particles and phenomena in the universe, such as atoms and subatomic particles.
```

### **3. Download the ZIP**
Once the JSON files are generated, you can download the ZIP file containing them.

## **Gradio Interface**
The Gradio interface simplifies the process of generating the knowledge base by allowing users to directly upload their question-answer pairs via a web interface.

### **Interface Features**:
- **Input Form**: Upload a text file or manually input question-answer pairs.
- **Downloadable ZIP**: After processing, users can download a ZIP file with all JSON files.
- **User-Friendly**: No need for direct interaction with the code.

## **Knowledge Base Structure**
The generated JSON files follow this structure:
```json
{
  "titulo": "Título-1: What is quantum physics?",
  "produto": "Example Product",
  "segmento": "Example Segment",
  "jornada": "Example Journey",
  "pergunta": "What is quantum physics?",
  "resposta": "Quantum physics is the branch of physics dealing with the smallest particles and phenomena in the universe, such as atoms and subatomic particles."
}
```

Each question-answer pair is converted into a single JSON file and structured with additional metadata fields such as `title`, `product`, `segment`, and `journey`. This structure ensures consistency across the knowledge base.

## **RAG & ICL Integration**

### **Retrieval-Augmented Generation (RAG)**
KnowGenAI can generate embeddings from the knowledge base and store them in a vector database like FAISS or Pinecone. These embeddings are then used in a RAG pipeline to enable more accurate and contextually relevant responses from an LLM.

Steps to enable RAG:
1. Generate embeddings from the question-answer pairs using Sentence-Transformers.
2. Store the embeddings in a vector database such as FAISS or Pinecone.
3. Query the vector database to retrieve relevant knowledge base entries during LLM inference.

### **In-Context Learning (ICL)**
The JSON files generated by KnowGenAI can be fed into an LLM to serve as examples for In-Context Learning (ICL). This technique improves the quality of the model's responses by providing context and example question-answer pairs.

**Steps for ICL**:
1. Feed multiple question-answer examples from the knowledge base to the LLM.
2. Ask new questions, and the model will use the provided examples to guide its responses.

## **Roadmap**
- [ ] **Vector Database Options**: Expand support for additional vector databases for RAG (e.g., Weaviate, Qdrant).
- [ ] **Multi-Language Support**: Add functionality for multi-language question-answer pairs.
- [ ] **Advanced UI Features**: Enhance the Gradio interface with additional settings and customization options.
- [ ] **API Support**: Enable API endpoints for external integration with other applications.
- [ ] **Real-Time Generation**: Implement real-time knowledge base generation for large datasets.

## **Contributing**
We welcome contributions from the community! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

