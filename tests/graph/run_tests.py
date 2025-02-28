import sys
from pathlib import Path

import pytest


def run_graph_tests():
    """Run all graph system tests"""
    test_dir = Path(__file__).parent

    # Run tests with pytest
    args = [
        str(test_dir),  # Test directory
        "-v",  # Verbose output
        "--tb=short",  # Shorter traceback format
        "-p", "no:warnings",  # Disable warning capture plugin
        "-p", "asyncio"  # Enable asyncio plugin
    ]

    # Run pytest with our arguments
    return pytest.main(args)

if __name__ == "__main__":
    sys.exit(run_graph_tests())
