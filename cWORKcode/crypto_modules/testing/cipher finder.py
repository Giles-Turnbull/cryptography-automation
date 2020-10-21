import math

cipher_values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
cipher_symbols = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
text = input("input words: ")
numb_symbols = len(cipher_symbols)

#===========================================================================

def convert_string(text):
	letters = list(text)
	num_code = []
	for pl, i in enumerate(letters):
		if i == " ": del letters[pl]
	for i in letters: num_code.append(cipher_symbols.index(i))
	return num_code
#===========================================================================
dat = convert_string(text)
#===========================================================================
def get_ic(dat, cipher_symbols, numb_symbols):
	ct, sum = [], 0
	for i in range(numb_symbols): ct.append(0)
	for i in dat: ct[i] += 1
	for i in range(numb_symbols): sum += ct[i]*(ct[i]-1)
	ic = sum/(len(dat)*(len(dat)-1))
	return ic*1000
#===========================================================================
def get_max_periodic_ic(dat, numb_symbols):
	ct = []
	max_period = 15
	mx=0.0;
	for i in range(max_period):
		temp = []
		for j in range(numb_symbols): temp.append([])
		ct.append(temp)
	for x in (number+1 for number in range(max_period)):
		for y in range(x):
			for z in range(numb_symbols):
				ct[y][z]=0
		ind = 0
		for i in range(len(dat)):
			ct[ind][dat[i]] += 1
			ind = (ind+1)%x
		r = 0
		for i in range(x):
			e, f = 0, 0
			for j in range(numb_symbols):
				e += ct[i][j]*(ct[i][j]-1);
				f += ct[i][j];
			if f>1: r += e/(f*(f-1))
		r = r/x
		if (r>mx): mx = r;
	return mx*1000
#===========================================================================
def get_kappa(dat):
	max_period, loop, mx = 15, True, 0
	for period in (number+1 for number in range(max_period)):
		if period>(len(dat) - 1): loop = False
		if loop == True:
			ct = 0
			for i in range(len(dat)-period):
				if (dat[i]==dat[i+period]):
					ct += 1
			z = ct/(len(dat)-period)
			if z>mx: mx=z
	return 1000.0*mx
#===========================================================================
def get_dict(dat, numb_symbols):
	ct = []
	for i in range(numb_symbols * numb_symbols): ct.append(0)
	for i in range((len(dat)) - 1):
		ct[dat[i]+numb_symbols*dat[i+1]] += 1
	sum = 0
	for i in range(numb_symbols * numb_symbols): sum += ct[i]*(ct[i]-1)
	l = len(dat) - 1
	ic = sum/(l*(l-1))
	return ic * 10000
#===========================================================================
def get_even_dict(dat, numb_symbols):
	ct, l, n = [], len(dat), 0
	for i in range(numb_symbols * numb_symbols): ct.append(0)
	for i in range(0, (l-1), 2):
		ct[dat[i]+numb_symbols*dat[i+1]] += 1
		n += 1
	sum = 0
	for i in range(numb_symbols * numb_symbols):
		sum += ct[i]*(ct[i]-1)
	ic = sum/(n*(n-1))
	return ic*10000
#===========================================================================
def get_LR(dat):
	reps = []
	for i in range(11): reps.append(0)
	print(reps)
	l = len(dat)
	for i in range(l):
		for j in range((i + 1), l, 1):
			n = 0
			print(i+n, j+n)
			while (j+n)<l and dat[i+n]==dat[j+n]:
				n += 1
			if n > 10: n = 10
			reps[n] += 1
	return 1000.0*(math.sqrt(reps[3])/l)
#===========================================================================
def get_ROD(dat):
	sum_all, sum_odd, l = 0, 0, len(dat)
	for i in range(l):
		for j in range((i+1), l, 1):
			n = 0
			while (j+n)<l and dat[i+n]==dat[j+n]:
				n += 1
			if n>1:
				sum_all += 1
				if (j-i)&1:
					sum_odd += 1
	if sum_all == 0: return 50.0
	else: return 100.0*sum_odd/sum_all
#===========================================================================
def get_logdi(dat):
	l,score, loop = (len(dat) - 1), 0, True
	for i in range(l):
		if dat[i]>25 or dat[i+1]>25: loop = True
		else: loop = False
		if loop == True:
			score += logdi[dat[i]][dat[i+1]]					# may not work (logdi needed)
	score *= 100;
	score /= l;
	return score
#===========================================================================
def get_sdd(dat):
	l,score, loop = (len(dat) - 1), 0, True
	for i in range(l):
		if dat[i]>25 or dat[i+1]>25: loop = True
		else: loop = False
		if loop == True:
			score += sdd[dat[i]][dat[i+1]]						# may not work (sdd needed)
	score *= 100;
	score /= l;
	return score
#===========================================================================
cipher_values = [get_ic(dat, cipher_symbols, numb_symbols), get_max_periodic_ic(dat, numb_symbols), get_kappa(dat), get_dict(dat, numb_symbols), get_even_dict(dat, numb_symbols), get_LR(dat), get_ROD(dat), get_logdi(dat), get_sdd(dat)]
#---------------------------------------------------------------------------
def get_num_dev(ctype, cipher_values):
	num_dev = []
	for i in range(len(ctype)):								# may not work (std and ave needed)
		x = 0
		for j in range(9):
			v = std[j][i]
			if j==0: v += 0.001
			if ave[j][i]==0: x += cipher_values[j]
			else: x += math.abs((cipher_values[j] - ave[j][i])/v)
		num_dev.append(ctype[i] + x)
	return num_dev.sort()
#---------------------------------------------------------------------------
print(get_logdi(dat))
