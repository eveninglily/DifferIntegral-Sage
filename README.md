# DifferIntegral-Sage

SageMath Implementation of Riemann–Liouville DifferIntegral Operator

# Usage

Install with `sage -pip install differintegral_sage`

Import with `from differintegral_sage import differ_integral`

## Example

Take the 1.5th derivative:

```
x = var('x')
differ_integral(x**2 + 3, x, 1.5)
```

## Arguments

Keyword arguments:

- func -- Function to operate on
- variable -- The variable to act with respect to
- order -- The order to integrate or differentiate to. Positive values are derivatives, negative are integrals.
