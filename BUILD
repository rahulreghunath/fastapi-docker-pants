python_requirement(name="fastapi", requirements=["fastapi"])
python_sources(
    name="root",
)

pex_binary(
  name="app",
  entry_point="blog/run.py",
  dependencies=["uvicorn","fastapi"],
)
