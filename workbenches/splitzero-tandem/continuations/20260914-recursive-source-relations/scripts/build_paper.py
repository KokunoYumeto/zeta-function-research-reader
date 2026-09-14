"""Build the current mathematically revised reader without replaying old adapters."""
from pathlib import Path
import runpy

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).with_name('build_current_reader.py')), run_name='__main__')
