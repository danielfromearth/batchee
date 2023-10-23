"""A Harmony CLI wrapper around the concatenate-batcher"""
from argparse import ArgumentParser

import harmony

from batcher.harmony.service_adapter import ConcatBatching as HarmonyAdapter


def main(config: harmony.util.Config = None) -> None:
    """Parse command line arguments and invoke the service to respond to them.

    Parameters
    ----------
    config : harmony.util.Config
        harmony.util.Config is injectable for tests

    Returns
    -------
    None
    """
    parser = ArgumentParser(
        prog="Pre-concatenate-batching", description="Run the pre-concatenate-batching service"
    )
    harmony.setup_cli(parser)
    args = parser.parse_args()
    if harmony.is_harmony_cli(args):
        harmony.run_cli(parser, args, HarmonyAdapter, cfg=config)
    else:
        parser.error("Only --harmony CLIs are supported")


if __name__ == "__main__":
    main()
