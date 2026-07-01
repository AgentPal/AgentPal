# Luma Design Pal Fixture

R217 controlled fixture for the Luma-style logo design regression. This fixture
exists only under `evals/` and must not be moved to `official/pals/` or
registered in `workspace/organization/contacts/`.

Expected behavior:

- load Pal Runtime Read Order before the logo task;
- produce visual direction before any ImageGen request;
- treat ImageGen as a host execution tool;
- output Asset Use Summary;
- produce Missing Asset Plan when key design assets are absent.
