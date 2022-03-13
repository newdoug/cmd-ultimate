import sys

from cmdu.ui.shell import Shell


def main() -> int:
    shell = Shell()
    if shell.start():
        print("Successfully ran shell")
    else:
        print("Shell failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
