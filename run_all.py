"""
Run every topic file's self-tests:   python run_all.py
Run one topic with its demo:         python 01_basic_math/prime_number.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    files = sorted(p for p in ROOT.glob("0*/*.py"))
    passed, failed = 0, []
    for f in files:
        result = subprocess.run([sys.executable, str(f)], capture_output=True, text=True)
        ok = result.returncode == 0 and "All tests passed" in result.stdout
        print(f"{'PASS' if ok else 'FAIL'}  {f.parent.name}/{f.name}")
        if ok:
            passed += 1
        else:
            failed.append(f.name)
            print(result.stdout, result.stderr)
    print(f"\n{passed}/{len(files)} files passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
