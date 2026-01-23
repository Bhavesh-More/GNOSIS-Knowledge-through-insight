# GNOSIS AI Folder

This folder contains the AI logic, agents, and services for the GNOSIS project. It includes various Python scripts and modules responsible for intelligent processing, query transformation, and interaction with LLMs, vector databases, and multimedia services.

## Table of Contents

1. [Folder Structure](#folder-structure)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Environment Configuration](#environment-configuration)
5. [Dependencies Overview](#dependencies-overview)
6. [Usage](#usage)
7. [Troubleshooting](#troubleshooting)

---

## Folder Structure

- **`agents/`**: Contains specific AI agents that handle different aspects of the reasoning process
  - `gnosisAiEngine.py`: Main engine that orchestrates all agents
  - `evidence.py`: Evidence gathering agent
  - `explainer.py`: Query explanation agent
  - `impacter.py`: Future impact prediction agent
  - `queryTransformer.py`: Query transformation and enhancement
  
- **`prompts/`**: Stores system prompts and templates used to guide AI models
  - `evidence.txt`: Evidence gathering prompts
  - `gnosisExplainer.txt`: Explanation prompts
  - `impacter.txt`: Impact analysis prompts
  - `queryTransformer.txt`: Query transformation prompts

- **`services/`**: Core utility services for external integrations
  - `vectors.py`: Vector database operations using Qdrant and CLIP embeddings
  - `images.py`: Image processing and retrieval services
  
- **`utils/`**: Helper functions and shared utilities
  - `confidenceScore.py`: Confidence scoring algorithms
  - `vectorSort.py`: Vector sorting and ranking utilities
  
- **`resources/`**: Jupyter notebooks for data exploration and testing
  - `imageUpload.ipynb`: Image upload and processing workflow
  - `textUpload.ipynb`: Text upload workflow
  - `videoUpload.ipynb`: Video upload workflow

- **`requirements.txt`**: Complete list of Python dependencies and versions

---

## Prerequisites

Before setting up the AI folder, ensure you have:

1. **Windows OS** (or compatible Linux/macOS system)
2. **Administrative access** to install software
3. **Internet connection** for downloading packages and accessing external services
4. **Sufficient disk space** (~5-10 GB recommended for dependencies)

### External Services Required

The AI engine requires credentials and access to:

- **Qdrant Vector Database**: For semantic search and embeddings storage
  - API Key and URL (obtained from your Qdrant instance)
  
- **OpenAI API** (if using GPT models): For LLM operations
  - API Key from OpenAI

- **CUDA (Optional)**: For GPU acceleration with PyTorch
  - NVIDIA GPU with CUDA Compute Capability 3.5+
  - CUDA Toolkit 11.x or higher
  - cuDNN library

---

## Setup Instructions

Follow these steps to set up the Python environment correctly for the AI folder.

### Step 1: Install Conda/Miniconda

We recommend using Conda to manage the Python environment and dependencies.

1. **Download Miniconda** (Recommended for a lightweight installation):
   - Visit the [Miniconda Installer Page](https://docs.conda.io/en/latest/miniconda.html)
   - Download the Windows installer (64-bit)

2. **Install Miniconda**:
   - Run the downloaded `.exe` file
   - Follow the installation prompts
   - **Recommended**: Check the option to add Miniconda to your PATH (allows `conda` from any terminal)
   - Use the "Anaconda Prompt" or PowerShell after installation

### Step 2: Create and Activate Conda Environment

1. **Open a terminal** (PowerShell, Command Prompt, or Anaconda Prompt)

2. **Navigate to the AI folder**:
   ```powershell
   cd ./ai
   ```

3. **Create a new Conda environment** with Python 3.10:
   ```bash
   conda create -n iitGnosisDataset python=3.10 -y
   ```
   
   *Note: Python 3.10 is recommended for compatibility with PyTorch, transformers, and other deep learning libraries*

4. **Activate the environment**:
   ```bash
   conda activate iitGnosisDataset
   ```
   
   *You should see `(iitGnosisDataset)` at the start of your command prompt*

### Step 3: Install Python Dependencies

With the `iitGnosisDataset` environment activated:

1. **Upgrade pip, setuptools, and wheel**:
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

2. **Install dependencies from requirements.txt**:
   ```bash
   pip install -r requirements.txt
   ```
   
   *This may take 5-15 minutes depending on your internet connection*

3. **For GPU Support (Optional)**:
   If you have an NVIDIA GPU and want to accelerate processing:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```
   
   *Replace `cu118` with your CUDA version (cu117, cu121, etc.) if different*

### Step 4: Configure Environment Variables

The AI engine requires environment variables for external services. Create a `.env` file in the AI folder root:

1. **Create `.env` file**:
   ```powershell
   New-Item -Path ".\ai\.env" -ItemType File
   ```

2. **Add the following environment variables**:
   ```
   # Qdrant Vector Database Configuration
   QDRANT_URL=https://your-qdrant-instance-url
   QDRANT_KEY=your-qdrant-api-key
   
   # OpenAI Configuration (if using GPT models)
   OPENAI_API_KEY=your-openai-api-key
   
   # Other configuration variables as needed
   ```

3. **Save the file** and ensure it's in the `ai/` directory

### Step 5: Verify Installation

To ensure everything is set up correctly:

1. **Check installed packages**:
   ```bash
   conda list
   ```
   
   Verify that key packages are installed:
   - `torch` (PyTorch)
   - `transformers` (Hugging Face)
   - `openai-whisper`
   - `sentence-transformers`
   - `qdrant-client`
   - `numpy`, `pandas`
   - `opencv-python`
   - `pillow`

2. **Test Python import** (Optional):
   ```bash
   python -c "import torch; import clip; import qdrant_client; print('All core imports successful!')"
   ```

3. **Test CUDA availability** (if GPU setup):
   ```bash
   python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
   ```

---

## Environment Configuration

### `.env` File Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `QDRANT_URL` | Qdrant vector database URL | Yes | `https://qdrant.example.com` |
| `QDRANT_KEY` | Qdrant API authentication key | Yes | `xxxxxxxxxxxxxxxx` |
| `OPENAI_API_KEY` | OpenAI API key for LLM access | Optional | `sk-xxxxxxxxxxxxxxxx` |

### Conda Environment Management

**Activate environment**:
```bash
conda activate iitGnosisDataset
```

**Deactivate environment**:
```bash
conda deactivate
```

**View all environments**:
```bash
conda env list
```

**Remove environment** (if needed):
```bash
conda env remove -n iitGnosisDataset
```

---

## Dependencies Overview

### Key Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `torch` | 2.5.1 | Deep learning framework for neural networks |
| `transformers` | 4.57.6 | Hugging Face transformers for LLMs and embeddings |
| `sentence-transformers` | 5.2.0 | Sentence embedding models |
| `qdrant-client` | 1.10.1 | Vector database client |
| `opencv-python` | 4.13.0.90 | Computer vision operations |
| `openai-whisper` | 20250625 | Audio transcription |
| `numpy` | 2.0.1 | Numerical computing |
| `pandas` | 2.3.3 | Data manipulation |
| `pillow` | 11.1.0 | Image processing |
| `scikit-learn` | 1.7.2 | Machine learning utilities |
| `python-dotenv` | 1.2.1 | Environment variable management |
| `pydantic` | 2.12.5 | Data validation |

### Full Dependency Tree

See `requirements.txt` for the complete list of 97 dependencies including transitive dependencies.

---

## Usage

### Running the GNOSIS AI Engine

1. **Activate the environment**:
   ```bash
   conda activate iitGnosisDataset
   ```

2. **Import and use the engine**:
   ```python
   from ai.agents.gnosisAiEngine import invokeEngine
   
   # Invoke the engine with your data
   result = invokeEngine({
       "query": "Your query here",
       # Additional data as needed
   })
   ```

### Using Jupyter Notebooks

To run the provided notebooks:

1. **Install Jupyter** (if not already installed):
   ```bash
   conda install jupyter -y
   ```

2. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

3. **Open the notebooks** from the `resources/` folder:
   - `imageUpload.ipynb`
   - `textUpload.ipynb`
   - `videoUpload.ipynb`

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: `ModuleNotFoundError: No module named 'torch'`
**Solution**: Ensure the `iitGnosisDataset` environment is activated and all dependencies are installed:
```bash
conda activate iitGnosisDataset
pip install -r requirements.txt
```

#### Issue: `QDRANT_URL` or `QDRANT_KEY` not found
**Solution**: Verify the `.env` file exists in the `ai/` folder and contains the correct environment variables:
```bash
cat .env  # View contents
```

#### Issue: CUDA not available / GPU not detected
**Solution**: This is optional and the code will fall back to CPU. To enable GPU:
1. Verify NVIDIA GPU is installed: `nvidia-smi`
2. Install CUDA Toolkit from NVIDIA website
3. Reinstall PyTorch with CUDA support (see Step 3)

#### Issue: Long installation time or network errors
**Solution**: Retry with alternate PyPI mirror:
```bash
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

#### Issue: Permission denied errors on Windows
**Solution**: Run PowerShell or Command Prompt as Administrator

#### Issue: `pip install` fails with compilation errors
**Solution**: Install Microsoft C++ Build Tools:
1. Download from [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/)
2. Select "Desktop development with C++" workload
3. Install and retry `pip install -r requirements.txt`

### Getting Help

1. Check the requirements are installed: `conda list`
2. Verify environment variables: Check `.env` file exists and is readable
3. Test individual modules: `python -c "import <module_name>"`
4. Consult logs and error messages for specific module issues

---

## Additional Notes

- **Python Version**: This project uses Python 3.10. Compatibility with other versions is not guaranteed.
- **Operating System**: Tested on Windows. Linux/macOS may require minor adjustments.
- **GPU vs CPU**: GPU acceleration significantly speeds up model inference. CPU-only operation is supported but slower.
- **Memory Requirements**: Minimum 8GB RAM recommended; 16GB+ for optimal performance with large models.

---

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review error messages and logs carefully
3. Ensure all environment variables are properly configured
4. Verify internet connectivity for downloading dependencies and accessing external services
