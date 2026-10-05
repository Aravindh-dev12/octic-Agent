"""Octic AI Agent CLI entrypoint."""
def main() -> None:
    from praisonai.__main__ import main as upstream_main
    upstream_main()
if __name__ == "__main__":
    main()
