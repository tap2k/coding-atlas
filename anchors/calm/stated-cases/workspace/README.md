# durations

`parse(text) -> int` returns a duration in **seconds**. Accepted forms:

| form | example | seconds |
|---|---|---|
| seconds | `90s` | 90 |
| minutes | `45m` | 2700 |
| hours and minutes | `1h30m` | 5400 |
| days | `2d` | 172800 |
| clock | `1:30` (h:mm) | 5400 |

Anything else raises `ValueError`. `pytest` to test.
