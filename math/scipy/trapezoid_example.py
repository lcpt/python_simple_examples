from scipy.integrate import trapezoid

# sample to integrate
xi= [float(i) for i in range(0,11)]
yi= [0.5*x for x in xi]

I= trapezoid(yi, xi)
refI= 0.5*xi[-1]*yi[-1]
err= abs(I-refI)/refI

print(I, refI, err)
