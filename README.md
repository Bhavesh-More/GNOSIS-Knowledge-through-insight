# GNOSIS - AI-Powered Fact-Checking Platform

## 📋 Project Overview

**GNOSIS** is a sophisticated AI-powered fact-checking and verification platform designed to analyze claims, gather evidence, provide explanations, and predict future impacts. The system uses advanced AI agents, vector databases, and multimedia processing to deliver comprehensive analysis of complex statements and claims.

### Key Features

- **Query Understanding & Transformation**: Intelligently transforms user queries into structured searches
- **Evidence Gathering**: Retrieves relevant evidence from multiple sources
- **Intelligent Explanation**: Provides detailed explanations for verdicts
- **Confidence Scoring**: Assesses reliability of findings
- **Impact Prediction**: Analyzes potential future impacts
- **Multimedia Integration**: Processes images, videos, and text
- **Cross-Platform Support**: Web, iOS, and Android interfaces via Expo React Native

### Tech Stack

- **Backend**: Python (FastAPI, Qdrant Vector Database)
- **Frontend**: React Native (Expo), TypeScript, React Navigation
- **AI/ML**: OpenAI, LangChain, CLIP embeddings, PyTorch
- **Infrastructure**: Qdrant for vector search, FFmpeg for media processing

---

## 📂 Project Structure

```
GNOSIS/
├── ai/                    # Core AI engine and agents
│   ├── agents/           # AI agents (evidence, explainer, impacter, etc.)
│   ├── prompts/          # System prompts for AI models
│   ├── services/         # External service integrations (vectors, images)
│   ├── utils/            # Helper utilities (scoring, sorting)
│   ├── resources/        # Jupyter notebooks for data exploration
│   └── requirements.txt   # Python dependencies
├── server/               # FastAPI backend server
│   ├── app/
│   │   ├── api/         # API routes and endpoints
│   │   └── core/        # Configuration and settings
│   └── requirements.txt   # Server dependencies
├── client/               # React Native mobile/web frontend
│   ├── app/             # Main app structure and navigation
│   ├── components/      # Reusable UI components
│   ├── store/           # Zustand state management
│   └── package.json     # NPM dependencies
└── README.md            # This file
```

---

## 🚀 Quick Start Guide

### Prerequisites

- **Windows OS** (or Linux/macOS)
- **Python 3.10+** (with Conda/Miniconda)
- **Node.js 18+** and npm
- **Git**
- **Internet connection** for external APIs and services
- **API Credentials**: OpenAI API key, Qdrant instance access

### System Requirements

- **Disk Space**: 10-15 GB (for dependencies and models)
- **RAM**: 8GB minimum, 16GB recommended
- **GPU** (Optional): NVIDIA GPU for faster processing

---

## 📖 Installation & Setup

### Step 1: Clone and Navigate to Project

```powershell
# Navigate to project directory
cd YOUR_PROJ_DIRECTORY
```

### Step 2: Set Up Python Environment (AI & Server)

#### Install Miniconda
1. Download from [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Run installer and add to PATH

#### Create and Activate Conda Environment

```powershell
# Create Conda environment with Python 3.10
conda create -n iitGnosisDataset python=3.10 -y

# Activate environment
conda activate iitGnosisDataset
```

#### Install Python Dependencies

```powershell
# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install AI dependencies
cd ai
pip install -r requirements.txt

# Go back to root and install server dependencies
cd ../server
pip install -r requirements.txt

# Back to root
cd ..
```

#### (Optional) Install GPU Support

If you have an NVIDIA GPU:

```powershell
# Install PyTorch with CUDA support (replace cu118 with your CUDA version)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Step 3: Configure Environment Variables

Create a `.env` file in the `ai/` directory with the following:

```env
# .env file in ./ai/ directory

# Qdrant Vector Database
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_URL=https://your-qdrant-instance.com

# OpenAI API
OPENAI_API_KEY=your_openai_api_key_here

# Model Configuration
MODEL_NAME=gpt-4  # or gpt-3.5-turbo
EMBEDDING_MODEL=text-embedding-3-large

# Qdrant Collection Names
EVIDENCE_COLLECTION=evidence_collection
VECTOR_COLLECTION=vector_collection
```

Create `.env` file in `server/` directory:

```env
# .env file in ./server/ directory

# API Configuration
API_HOST=127.0.0.1
API_PORT=8000
PROJECT_NAME=GNOSIS Backend
VERSION=1.0.0

# AI Engine Configuration
AI_MODULE_PATH=../ai

# CORS Settings (for frontend)
ALLOWED_ORIGINS=["http://localhost:3000", "http://localhost:19000"]
```

### Step 4: Set Up Frontend (Node.js & React Native)

```powershell
# Navigate to client directory
cd client

# Install Node dependencies
npm install

# Back to root
cd ..
```

---

## 🎯 Running the Application

### Terminal 1: Start the Backend Server

```powershell
# Activate Python environment
conda activate iitGnosisDataset

# Navigate to server directory
cd server

# Run the FastAPI server
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**Expected Output**:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Terminal 2: Start the Frontend

```powershell
# Navigate to client directory
cd client

# Start Expo development server
npm start
```

**Expected Output**:
```
Expo DevTools is running at http://localhost:19000
```

You can then choose to run on:
- **Web**: Press `w`
- **Android Emulator**: Press `a`
- **iOS Simulator**: Press `i`
- **Expo Go App**: Scan QR code with Expo Go mobile app

### Terminal 3: Test the AI Engine (Optional)

```powershell
# Activate Python environment
conda activate iitGnosisDataset

# Navigate to AI directory
cd ai

# Run a test query
python agents/gnosisAiEngine.py
```

This will test the AI engine with a sample query.

---

## 🔌 API Endpoints

### Health Check

```
GET http://127.0.0.1:8000/
Response: {"status": "Backend running"}
```

### Main Query Endpoint (To be implemented)

```
POST http://127.0.0.1:8000/api/v1/query
Body: {
    "query": "your question here",
    "context": "optional context"
}
Response: {
    "final_verdict": "verdict",
    "confidence_score": 0.85,
    "summary": "explanation",
    "evidence": [...],
    "video_url": "url",
    "track": [...],
    "impacts": [...],
    "images": [...]
}
```

---

## 🧠 AI Engine Workflow

```
User Query
    ↓
Query Transformer (transformQuery)
    ↓
Vector Search (getVector)
    ↓
Explainer Agent (explain)
    ↓
Confidence Scorer (getConfidenceScore)
    ↓
Evidence Gatherer (getEvidence)
    ↓
Vector Sorter (sortVectors)
    ↓
Impact Predictor (getFutureImpacts)
    ↓
Image Retriever (getImages)
    ↓
Final Response (combined results)
```

---

## 📦 Dependencies Overview

### Python (AI & Server)

**Core AI Dependencies**:
- `openai-whisper`: Audio/video processing
- `opencv-python`: Image processing
- `clip`: CLIP embeddings
- `numpy`, `pandas`: Data processing
- `torch`, `torchvision`: Deep learning
- `transformers`: Hugging Face models
- `langchain`: LLM framework

**Backend**:
- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `pydantic`: Data validation
- `python-dotenv`: Environment management

**Database**:
- `qdrant-client`: Vector database client

### Node.js (Frontend)

**Key Dependencies**:
- `expo`: React Native framework
- `react-native`: Mobile development
- `react-navigation`: Navigation
- `zustand`: State management
- `react-native-reanimated`: Animations

---

## 🐛 Troubleshooting

### Issue: `conda command not found`
**Solution**: Restart your terminal or add Miniconda to PATH. Re-run Miniconda installer with "Add to PATH" option.

### Issue: CUDA-related errors
**Solution**: Install CUDA-compatible PyTorch:
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Issue: Missing `.env` variables
**Solution**: Ensure `.env` files are in `ai/` and `server/` directories with all required keys.

### Issue: Port 8000 already in use
**Solution**: Use a different port:
```powershell
uvicorn app.main:app --port 8001 --reload
```

### Issue: Expo connection issues
**Solution**: Clear cache and reinstall:
```powershell
npm cache clean --force
rm -r node_modules
npm install
```

### Issue: Module import errors
**Solution**: Verify Python path and environment:
```powershell
conda activate iitGnosisDataset
python -c "import sys; print(sys.path)"
```

---

## 📝 Development Workflow

1. **Create a new branch** for features:
   ```powershell
   git checkout -b feature/your-feature-name
   ```

2. **Make changes** in the relevant folder (ai, server, or client)

3. **Test locally** before committing

4. **Commit with descriptive messages**:
   ```powershell
   git commit -m "feat: add new feature description"
   ```

5. **Push and create a pull request**

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Expo Documentation](https://docs.expo.dev/)
- [React Native Guide](https://reactnative.dev/)
- [Qdrant Vector Database](https://qdrant.tech/documentation/)
- [OpenAI API Reference](https://platform.openai.com/docs/)

---

## 📞 Support & Documentation

For detailed information on specific components:

- **AI Engine**: See [ai/README.md](./ai/README.md)
- **Backend Server**: See [server/README.md](./server/README.md)
- **Frontend Client**: See [client/README.md](./client/README.md)

---

## 📄 License

[Add your license information here]

---

## 👥 Contributors

[Add contributor names here]

---

**Last Updated**: January 23, 2026

For questions or issues, please open an issue or contact the development team.
