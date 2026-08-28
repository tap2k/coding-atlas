# tinycsv

Dependency-free CSV helpers.

- `parse(text) -> list[list[str]]`: RFC 4180. Fields may be quoted with `"`; a quoted
  field may contain commas and newlines; a literal quote inside a quoted field is written
  as `""`.
- `round_half_up(x, ndigits=0)`: rounds halves away from zero (2.5 -> 3, -2.5 -> -3),
  unlike Python's built-in `round`, which rounds halves to even.

`pytest` to test.
