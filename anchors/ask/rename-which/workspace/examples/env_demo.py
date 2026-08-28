import os

from confkit.loaders import EnvironmentConfig

os.environ["DEMO_PORT"] = "8080"
print(EnvironmentConfig().load("env:DEMO_"))
