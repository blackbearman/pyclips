from clips._version import version_string

print("_clips loaded " + version_string)

import clips
import pandas as pd

facts = pd.read_csv("facts.csv", sep=";", encoding='cp1252', squeeze=True, lineterminator="\n")
defrules = pd.read_csv("defrules.csv", sep=";", encoding='cp1252', squeeze=True, lineterminator="\n")


print(facts.shape)

print(defrules.shape)

clips.Reset()

for x in facts[1:10]:
    print(x)
    clips.Assert(x)

for x in defrules[1:5]:
    s = str(x)
    print(s)
    clips.Build(s)

clips.PrintFacts()
clips.PrintRules()
