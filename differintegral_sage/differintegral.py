from sage.calculus.functional import derivative
from sage.calculus.calculus import maxima
from sage.all import var, gamma
from sage.symbolic.integration.integral import definite_integral
from sage.functions.other import ceil
from sage.symbolic.assumptions import assume

def differ_integral(func, variable, order):
    """Takes the fractional derivative or intergral.

    Keyword arguments:
    func -- Function to operate on
    variable -- The variable to act with respect to
    order -- The order to integrate or differentiate to. Positive values are derivatives, negative are integrals.
    """
    maxima('keepfloat: false')
    if order == 0:
        return func
    elif order > 0:
        new_order = ceil(order)
        return derivative(differ_integral(func, variable, -(new_order - order)), variable, new_order)
    else:
        t = var('t')
        assume(variable > 0)
        return (1/gamma(-order)) * definite_integral(func.subs(variable=t)*(variable-t)**(-order - 1), t, 0, variable)