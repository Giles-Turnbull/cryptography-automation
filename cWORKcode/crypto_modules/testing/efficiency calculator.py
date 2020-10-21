import random
efflist, tot = [], 0
for i in range(1000):
    estimate_cycles = random.randint(111111, 999999999)
    actual_cycles = random.randint(111111, 9999999)
    eff = (actual_cycles / estimate_cycles) * 100
    efflist.append(eff)
    print(eff)
for pl, i in enumerate(efflist): tot = tot + i
tot = tot / (pl + 1)
mean = tot 
# remove outliers (1.5 times the mean) / standard deviation
totmean = 0
efflist.sort()
medianth = int((len(efflist) + 1) / 2)
quartiles = int((medianth - 1) / 2)
median = efflist[medianth - 1]
LQ = efflist[int(medianth / 2)]
UQ = efflist[int((medianth / 2) + medianth)]
IQR = UQ - LQ
outliers = 1.5 * IQR
LQ = LQ - outliers
UQ = UQ + outliers
for plout, x in enumerate(efflist):
    if x > (UQ + outliers): del efflist[plout]
    elif x < (LQ - outliers): del efflist[plout]
for plmeanie, u in enumerate(efflist): totmean = totmean + u
totmean = totmean / plmeanie
# remove outliers (1.5 times the mean) / standard deviation
print("median", median)
print("uq", UQ)
print("mean eff", totmean)
random_case_es = random.randint(111111, 999999999)
random_case_ac = random.randint(111111, 9999999)
calc = ((totmean / 100) * random_case_es)
print("=========================================")
print("max itts", random_case_es)
print("actual itts", random_case_ac)
print("estimated cycles is", str(calc) ," with a mean efficiency of", str(totmean))
print(IQR, mean)
