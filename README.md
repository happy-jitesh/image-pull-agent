# 🧠 Kubernetes ImagePullBackOff Healing Agent (Agentic AI)

![Kubernetes](https://img.shields.io/badge/Kubernetes-Automation-blue)
![Python](https://img.shields.io/badge/Python-Client-yellow)
![Agentic AI](https://img.shields.io/badge/Agentic-AI-purple)
![LLM](https://img.shields.io/badge/LLM-Llama3-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange)

An **AI-powered Kubernetes controller** that detects and automatically resolves **ImagePullBackOff / ErrImagePull** issues using:

* 🧠 **Llama3 (via Ollama)** for reasoning
* ⚙️ **Kubernetes Python client** for direct API interaction
* 🤖 **Agentic AI design pattern** for autonomous healing

---

# 🚀 Problem Statement

One of the most common Kubernetes deployment failures is:

```text
ImagePullBackOff / ErrImagePull
```

This happens due to:

* ❌ Wrong image tag
* ❌ Image not found
* ❌ Typo in repository
* ❌ Private registry authentication issues

Traditionally, engineers debug this manually.

This project shows how an **AI agent can detect and fix it automatically**.

---

# 🧠 How the AI Agent Works

The agent continuously monitors Kubernetes and performs:

```text
Observe → Analyze → Decide → Act → Verify
```

---

# 🔄 Workflow

```text
Kubernetes Cluster
        │
        ▼
Pod enters ImagePullBackOff
        │
        ▼
AI Controller (Python)
        │
        ▼
Detect failure using K8s API
        │
        ▼
Send context to Llama3 (Ollama)
        │
        ▼
LLM decides action
        │
        ▼
Patch deployment image
        │
        ▼
Rolling restart
        │
        ▼
Pods become healthy
```

---

# 🏗 Architecture Diagram

```text
+----------------------+
| Kubernetes Cluster   |
+----------+-----------+
           |
           ▼
   ImagePullBackOff Event
           |
           ▼
+----------------------+
|  AI Controller       |
|  (Python Client)     |
+----------+-----------+
           |
           ▼
+----------------------+
| Llama3 (Ollama)      |
| Decision Engine      |
+----------+-----------+
           |
           ▼
+----------------------+
| Patch Deployment     |
| Fix Image Tag        |
+----------+-----------+
           |
           ▼
   Rolling Restart → Healthy Pods
```

---

# 🛠 Tech Stack

| Component                | Purpose                 |
| ------------------------ | ----------------------- |
| Kubernetes               | Container orchestration |
| Python Kubernetes Client | API interaction         |
| Ollama                   | Local LLM runtime       |
| Llama3                   | Decision making         |
| Agentic AI               | Autonomous control loop |

---

# 📁 Project Structure

```text
image-pull-agent/
│
├── agent.py
├── config.py
├── observer.py
├── actions.py
├── llm_brain.py
│
├── prompts/
│   └── image_prompt.txt
│
└── bad-image.yaml
```

---

# 🧪 Demo Scenario

We intentionally deploy a **broken image**:

```yaml
image: nginx:wrongtag
```

This causes:

```text
ImagePullBackOff
```

The AI agent detects this and automatically fixes the image.

---

# ⚡ Setup Instructions

---

## 1️⃣ Install Dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate

pip3 install kubernetes requests
```

---

## 2️⃣ Start Ollama

```bash
ollama pull llama3
ollama serve

```

Verify:

```bash
curl http://localhost:11434
```

---

## 3️⃣ Deploy Broken Workload

```bash
kubectl create namespace prod
kubectl apply -f bad-image.yaml
```

Verify:

```bash
kubectl get pods -n prod
```

---

## 4️⃣ Run the AI Agent

```bash
python3 agent.py
```

---

# 🤖 AI Actions

| Action            | Description                |
| ----------------- | -------------------------- |
| FIX_IMAGE_TAG     | Replace incorrect image    |
| ESCALATE_TO_HUMAN | For auth or unknown issues |
| DO_NOTHING        | Temporary issue            |

---

# 🧠 Key Learning

This project demonstrates:

* Moving from manual debugging → automated healing
* Using LLMs for decision-making in DevOps
* Building controller-based AI systems
* Using Kubernetes Python client for production-style automation

---

# 📚 Agentic AI for DevOps Series

| Episode | Topic                                       |
| ------- | ------------------------------------------- |
| 1       | AI Incident Resolution                      |
| 2       | OOMKilled Healing                           |
| 3       | CPU Throttling Healing                      |
| 4       | Probe Failure Healing                       |
| 5       | **ImagePullBackOff Healing (This Project)** |

---

# 🚀 Future Enhancements

* Detect private registry auth issues
* Auto rollback to previous working image
* Multi-container support
* CVE-aware image replacement
* GitOps integration

---

# ⭐ Support

If you found this useful:

* ⭐ Star this repo
* 🔔 Subscribe to the YouTube channel
* 💬 Share feedback

---

# 👨‍💻 Author

DevOps Engineer building **AI-powered SRE systems for Kubernetes**

---

# 📜 License

MIT License

---
