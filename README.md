# Cisco Learning Portal – an AI-Powered Learning Assistant 🧠


<iframe
	src="https://alexstev-cisco-automation-certification-station.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>




### 🏁 Getting Started

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


### Clone your HuggingFace repo and add the requiredfiles 

Use an access token as git password/credential


When prompted for a password, use an access token with write permissions
Generate one from your settings: https://huggingface.co/settings/tokens
```
git clone https://huggingface.co/spaces/alexstev/cisco-learning-portal
```

Make sure huggingface-cli is installed: pip install -U "huggingface_hub[cli]"
```
huggingface-cli download alexstev/cisco-learning-portal --repo-type=space
```



