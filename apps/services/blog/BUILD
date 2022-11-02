
python_sources(
    name="blog",
    dependencies=[
        "apps/shared",
        "//:requirements"
    ],
)

pex_binary(
    name="run",
    entry_point="run.py",
    dependencies=[
        ":blog",
        "//:requirements"
    ],
    restartable=True,
)