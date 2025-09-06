# Hello agent using OpenAI Agents SDK, Gemini API Key and Chainlit for CUI

## Initialize a package

```
uv init --package hello_agent
```

## Run your project

In the .toml file see the name of project to run

```
[project.scripts]
hello-agent = "hello_agent:main"
Variable    = Value
Variable    = project_name:method
```

To run

```
uv run hello-agent
```

## Add Dependency

```
uv add openai-agents
uv add chainlit
uv add python-dotenv
```

## Run Chainlit

```
uv run chainlit hello
```

Now create a file chatbot.py in src\hello_agent folder.
To run chatbot.py file

```
cd src
cd hello_agent
uv run chainlit run chatbot.py -w
```

-w flag is for hot reload
