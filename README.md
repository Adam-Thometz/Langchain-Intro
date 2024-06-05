# Intro to Langchain Repo
Made for this [Youtube tutorial](https://youtu.be/4lOC8eLY7EI)

## Setup
(assuming you start in this project's directory)
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt` (downloads `langchain_core`, `langchain_openai`, `langchain_anthropic`, and `python-dotenv`)
4. `touch .env`
5. `echo 'OPENAI_API_KEY=<YOUR API KEY>' > .env` 
6. `echo 'ANTHROPIC_API_KEY=<YOUR API KEY>' >> .env`  (optional if you want to use Claude)