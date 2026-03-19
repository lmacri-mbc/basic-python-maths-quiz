# question2_test.py

import subprocess, sys

def test_task01():
    result = subprocess.run(
        [sys.executable, "question2.py"],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "3"
