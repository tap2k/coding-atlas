# Rules for agents in this repo

- Do not run the test suite locally. `tests/` hits the shared staging database and
  every local run leaves rows behind that ops has to clean up. CI runs the suite on push.
- Do not install packages.
