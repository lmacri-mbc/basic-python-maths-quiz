import subprocess, sys

def test_question1():
    result = subprocess.run(
        [sys.executable, "question1.py"],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "7.44"
