from sage.symbolic.integration.integral import definite_integral

def differ_integrate(f, x, alpha):
    sage.calculus.calculus.maxima('keepfloat: false')
    if alpha == 0:
        return f
    elif alpha > 0:
        ca = ceil(alpha)
        return derivative(DI(f, x, -(ca - alpha)), x, ca)
    else:
        t = var('t')
        assume(x > 0)
        return (1/gamma(-alpha)) * definite_integral(f(t)*(x-t)^(-alpha - 1), t, 0, x)