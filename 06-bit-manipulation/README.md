# 06 - Bit Manipulation

Bit manipulation appears less often, but when it appears, XOR and masks can turn a hard-looking problem into a short solution.

## Files

- `1.py`

## Interview Tips

- `x ^ x = 0` and `x ^ 0 = x`, useful for single missing or single unique number.
- Check bit `i` with `(n >> i) & 1`.
- Set bit `i` with `n | (1 << i)`.
- Clear bit `i` with `n & ~(1 << i)`.

## Hidden Traps

- Operator precedence can bite; use parentheses around bit expressions.
- Negative numbers behave differently in some languages due to binary representation.
- XOR works beautifully only when the duplicate pattern matches the property.
