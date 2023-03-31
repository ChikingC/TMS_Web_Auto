import re
import sys
import math
import yaml


with open("../configini/confif.yaml",'r') as fp:
    try:

        stream = yaml.safe_load(fp)

    except Exception as e:
        print(e)


print(stream)