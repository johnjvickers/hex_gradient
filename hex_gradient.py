import numpy as np

def g_str(x):
	str = hex(x).partition('x')[2].partition('L')[0]
	while len(str) < 2:
		str = '0' + str

	return(str)

def main(start, end, steps):

	r_min = int(start[:2], 16)
	r_max = int(end[:2], 16)
	r_grad = np.linspace(r_min, r_max, steps)

	g_min = int(start[2:4], 16)
	g_max = int(end[2:4], 16)
	g_grad = np.linspace(g_min, g_max, steps)

	b_min = int(start[4:], 16)
	b_max = int(end[4:], 16)
	b_grad = np.linspace(b_min, b_max, steps)


	gradient = []
	for count in range(len(r_grad)):
		gradient.append(
			'#' +
			g_str(r_grad[count]) + g_str(g_grad[count]) + g_str(b_grad[count])
		)

	return(gradient)


if __name__ == '__main__':

	import pylab as pl
	import random as rnd

	g_len = 10

	c = main('00FFFF', 'FF00FF', g_len)

	print c

	# for i, sd in enumerate(np.linspace(0, 5, g_len)):
	# 	x = [rnd.gauss(0,sd) for a in np.arange(1000)]
	# 	pl.hist(x, histtype='step', lw=2, color=c[i])
	#
	# pl.show()

	x = np.arange(0, g_len, 1)
	y = [0]*g_len
	pl.scatter(x, y, c=c, s=1000, linewidths = 0)
	pl.show()
