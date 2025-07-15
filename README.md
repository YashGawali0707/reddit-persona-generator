##### \# **Reddit-Persona-Generator :**

* A Python-based tool that scrapes Reddit user activity and generates a detailed user persona. Uses local LLMs via Ollama for privacy-friendly AI generation.



##### **# Description :**

* "reddit-persona-generator" is a Python-based tool that analyzes a Reddit user's public activity (posts and comments) to generate a detailed user persona.

* &nbsp;It uses the Reddit API (via PRAW) to collect up to 20 posts and 30 comments from a given profile and then leverages a local large language model (LLM) through "Ollama" to process the data and infer: **1. Interests 2. Personality Traits 3. Writing Tone 4. Benefits and Values.**
* The output is saved as a **.txt** file containing the full persona, along with excerpts from the Reddit activity to support each insight.
* This project is fully offline and privacy-respecting — it uses open-source LLMs like **llama2** (Module of **Ollama**), So no external **API** or internet connection is required after setup.



##### **# Features :**

* **Reddit User Analysis**: Scrapes up to 20 posts and 30 comments from any public Reddit profile using PRAW.
* **AI-Generated Persona**: Generates a detailed user persona including interests, personality traits, writing tone, and values.
* **Citation-Based Insights**: Includes direct excerpts from posts and comments to support each personality insight.
* **Local LLM Integration**: Uses open-source models via **Ollama** — no need for **OpenAI** or internet-based APIs.
* **Automatic Report Generation**: Saves the generated persona into a structured **.txt** file for each user.
* **Privacy-First Design**: All processing happens locally; no personal data leaves your machine.
* **Fully Open-Source \& Customizable**: Modify prompts, scraping limits, or switch between LLMs easily.



##### **# Installations :**

* Install the **Python Environment** (Like **Python 3.13**) and check the version if python is already installed.
* Setup a **Virtual Environment** for a project , Open terminal and type **"python -m venv venv venv\\Scripts\\activate" (venv :Virtual Environment).**
* Install all required Python Libraries **using pip**. On terminal **type "pip install praw python-dotenv requests"**.
* Install **Ollama** for running Local AI model.**(Worked as a LLM's)**. After installation On terminal just type **"ollama run llama2"** to run **Ollama.**
* Add **Reddit App credentials : 1. Go to the "https://www.reddit.com/prefs/apps" and click "Create App" 2. Save the fields "Client\_ID" ,"Client\_SecretKey" ,"User\_Agent".**
* Setup the **GitHub Environment** like install **"Git Bash"** and **"Git CLI".** Execute all the commands that given in the descriptions of **GitHub.**



##### **# Usage :**

* Follow the below steps to run the **Reddit Persona Generator:**

   **1.** Make sure you are inside the project folder in your terminal.

&nbsp;     On terminal just type **"python main.py".**

   **2.** After program getting successfully runs you see the output as:

&nbsp;     **"Enter a Reddit URL Profile:"** Then paste the URL that given to you. For example:**"https://www.reddit.com/user/kojied/".**

   **3. Ollama** will generate a Reddit User persona and the scripts will contains: 

&nbsp;      **1. Scrape up to 20 posts and 30 comments from the Reddit profile.** 

       **2. Send the content to your local LLM (e.g., llama2 running via Ollama).**

       **3. Generate a detailed user persona based on writing patterns, tone, beliefs, and interests.**

   **4.** View the output in the **.txt** file which is automatically created in the project folder.

&nbsp;  **5.** The file includes: \[Key traits] \[Writing tone] \[Personality characteristics] \[Supporting quotes from Reddit content].

##### 

##### **# Environment Variables :**

* This project uses a **.env** file to securely store Reddit API credentials.
* The file called **user.env** was added in the **GitHub Repository** already. It contains the following credentials: **1. CLIENT\_ID=your\_reddit\_client\_id 2. CLIENT\_SECRET=your\_reddit\_client\_secret 3. USER\_AGENT=script:reddit-persona:v1.0 (by /u/your\_reddit\_username).** 
* The above credential you will get when you **"Create App"** on **Reddit.**



##### **# Project Structure :**

* The project structure is as follows:



&nbsp;       **reddit-persona-generator/**

       **├── main.py                   # Main Python script that runs the Reddit persona generator**

       **├── requirements.txt          # Python dependencies required to run the project**

       **├── user.env                      # Contains Reddit API credentials (not uploaded to GitHub)**

       **├── .gitignore                # Prevents pushing .env and system files to GitHub**

       **├── README.md                 # Project documentation and setup instructions**

       **├── persona\_kojied.txt        # Sample output for Reddit user: kojied**

       **└── persona\_HungryMove.txt    # Sample output for Reddit user: Hungry-Move-6603**



* **main.py:** Scrapes Reddit activity and sends it to a local LLM via Ollama to generate user personas.
* **.env:** Stores CLIENT\_ID, CLIENT\_SECRET, and USER\_AGENT from your Reddit developer app.
* **Output .txt files:** Contain AI-generated personas for Reddit profiles.



##### **# Technologies Used :**



**| Technology               | Purpose                                                                |**

**| ------------------------ | -----------------------------------------------------------------------|**

**| \*\*Python 3\*\*             | Core programming language for the entire project                       |**

**| \*\*PRAW\*\*                 | Python Reddit API Wrapper – used to fetch Reddit posts and comments    |**

**| \*\*Ollama\*\*               | Local AI runtime for running open-source LLMs like `llama2`, `mistral` |**

**| \*\*LLama2\*\* / \*\*Mistral\*\* | LLM used to generate the user persona from Reddit content              |**

**| \*\*Requests\*\*             | To send HTTP requests to the Ollama API                                |**

**| \*\*python-dotenv\*\*        | Loads environment variables from a `.env` file securely                |**

**| \*\*Git\*\*                  | Version control and collaboration                                      |**

**| \*\*GitHub\*\*               | Hosting and sharing the project repository                             |**

**|--------------------------|------------------------------------------------------------------------|**




##### **# Author/Contact Info :**



###### &nbsp; ***Yash Jaypal Gawali***



* **Built with ❤️ as part of the reddit-persona-generator internship task.**



* **LinkedIn :** [**Yash-Gawali**](https://www.linkedin.com/in/yash-gawali/)
  
* **GitHub :** [**Yash-Gawali0707**](https://github.com/YashGawali0707/)



* **Email :** [**gawaliyash2412@gmail.com**](gawaliyash2412@gmail.com)
  
* 
**##### \# License :**



* **This project is open source under the MIT License. Feel free to use, modify, or extend it with credit.**













