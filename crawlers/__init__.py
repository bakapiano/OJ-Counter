import os, importlib


SUPPORTED_OJ = []
CRAWLERS = {}

for file in os.listdir(__name__):
    if not file.startswith("__"):
        oj_name = file.split(".")[0]
        SUPPORTED_OJ.append(oj_name)
        module = importlib.import_module(__name__+"."+oj_name)
        CRAWLERS[oj_name] = module.Crawler


print(SUPPORTED_OJ, CRAWLERS)


