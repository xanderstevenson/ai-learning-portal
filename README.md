# Cisco Learning Portal – an AI-Powered Learning Assistant 🧠

This is a Streamlit-based AI app that integrates learning content from:

- Cisco U.
- Cisco Networking Academy (NetAcad)
- Cisco Learning Network (CLN)

## 🏁 Getting Started

```bash
git clone https://github.com/YOUR-USERNAME/ai-learning-portal.git
cd ai-learning-portal
pip install -r requirements.txt
streamlit run app.py
```


### Go to Hugging Face -> Spaces (https://huggingface.co/spaces) -> New Space:

- Name it, describe it, and denote the License
- Choose SDK -> Docker -> Streamlit
- Space Hardware -> the Free option
- Make it Public
- `Create Space`


### Mirror HF Repo from GitHub via Git Remotes

- Clone your GitHub repo and push it to the Hugging Face Space:

```
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

- Add the HF Space repo as a remote:

```
git remote add hf https://huggingface.co/spaces/alexstev/cisco-learning-portal
```

- Push your GitHub code to the HF Space:

```
git push hf main
```
