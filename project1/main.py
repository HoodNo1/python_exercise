import argparse
import sys


def cmd_config(args: argparse.Namespace) -> None:
    """config 子命令"""
    print(f"config: {args=}")


def cmd_run(args: argparse.Namespace) -> None:
    """run 子命令"""
    print(f"run: {args=}")


def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="project1 CLI tool")
    sub = parser.add_subparsers(dest="command", required=True)

    p_config = sub.add_parser("config", help="配置管理")
    p_config.add_argument("--key", "-k")
    p_config.add_argument("--value", "-v")
    p_config.set_defaults(handler=cmd_config)

    p_run = sub.add_parser("run", help="运行任务")
    p_run.add_argument("name", nargs="?", default="default")
    p_run.add_argument("--verbose", action="store_true")
    p_run.set_defaults(handler=cmd_run)

    return parser


def main() -> None:
    parser = setup_parser()
    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
