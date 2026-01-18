# ChaosMath 

**Math. But Unstable.**


`chaosmath` is a Python module that provides mathematical functions which are
*almost* correct.  
Results may vary depending on randomness, time, and pure bad vibes.

> Deterministic? No  
> Accurate? Maybe  
> Entertaining? Absolutely

---


## Installation

```bash
  pip install chaosmath
```
or
```bash
  git clone https://github.com/prathambhandary/ChaosMath.git
  cd ChaosMath
  pip install .
```

---

## Features

- `random_error()` → excuses when things go wrong (over 2500+ excuses)
- `pi()` → returns π-ish values
- `sqrt(x)` → usually right, sometimes not
- `add(a, b)` → addition with attitude
- `multiply(a, b)` → multiplication with chaos
- CLI support for terminal chaos

---

## Examples

```Python
import chaosmath as cm

print(f"[ERROR]: {cm.random_error()}")
# [ERROR]: Memory said 'nah'

print(cm.integrate("x^2"))
# ⚠️ CHAOS MATH: Integration exploded
# ∫ x^2 dx = ??? (Integration exploded)

print(f"Pi: {cm.pi()}")
# Pi: 3

```

## Disclaimer

This is not a bug.
This is the feature.

If the output is wrong, confusing, or deeply disappointing —
chaosmath is functioning correctly.

Do not use for:
- Exams  
- Production 
- Finance    
- Space travel   
- Anything you care about 

You have been warned.
---