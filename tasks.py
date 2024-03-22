from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task
def coveragereport(ctx):
    ctx.run("coverage report -m")

@task(test)
def coveragehtml(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")
