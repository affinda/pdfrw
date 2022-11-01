"""
We need a portable way to get a count of available CPUs. Sadly this is not
baked in yet.
"""
import os

import psutil

def available_cpu_count():
    """
    Number of available virtual or physical CPUs on this system. Use psutil
    for POSIX (except MacOS) and Windows. Do a special dance on MacOS.
    """

    try:
        import psutil
        return len(psutil.Process().cpu_affinity())
    except (ImportError, AttributeError):
        pass

    # POSIX
    try:
        res = int(os.sysconf('SC_NPROCESSORS_ONLN'))
        if res > 0:
            return res
    except (AttributeError, ValueError):
        pass


print(available_cpu_count())
