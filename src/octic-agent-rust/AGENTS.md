# Octic AI Agent — Rust Workspace Guide

This guide covers the Rust workspace at src/octic-agent-rust/.

## Design principles

- Keep public types explicit and strongly typed.
- Prefer clear error propagation over panics in library code.
- Use asynchronous I/O for network-bound operations.
- Keep abstractions small and focused.
- Add tests for behavior changes and regression fixes.
- Keep examples consistent with the current public API.

## Workspace layout

- The root Cargo.toml defines the workspace.
- The core library is in the core crate directory.
- Procedural macros are in the derive crate directory.
- Command-line entry points are in the CLI crate directory.
- Examples and tests live alongside the workspace crates.

Crate identifiers and imports are part of the compatibility surface. Do not rename them unless all dependent crates, examples, tests, manifests, and release references are updated in the same migration.

## Development checks

Run from this directory:

    cargo fmt --all -- --check
    cargo test --workspace
    cargo clippy --workspace --all-targets

For a focused change, run the relevant crate tests first, then run the workspace checks before submitting.

## Contribution requirements

- Include a regression test when fixing a bug.
- Update Rust documentation and examples when public behavior changes.
- Avoid machine-specific absolute paths in documentation.
- Do not commit build output, local credentials, or generated files.
- Preserve applicable third-party notices and attribution.

Use Octic AI Agent in user-facing documentation. Technical identifiers should remain unchanged unless a coordinated compatibility migration is intended.
