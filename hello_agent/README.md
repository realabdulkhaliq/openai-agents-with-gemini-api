# Initialize a package

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
```

s
