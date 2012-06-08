from __future__ import absolute_import
from line_profiler import CLineProfiler, show_text


class LineProfiler(CLineProfiler):
    """ A class wrapper for CLineProfiler.

    The CLineProfiler is already a context manager so it is compatible with
    the pikos Monitor class for functions. However it does not support
    recorders.

    Notes
    -----
    The LineProfiler current requires a list of functions at initialization
    that will be profiled. These functions do not have to be same as decorated
    function with the Pikos monitor. Please refer to
    `<http://packages.python.org/line_profiler/ for more information>_`
    on the line_profiler.

    """

    def print_stats(self, stream=None):
        """ Write out the results of the timing so far. """
        stats = self.get_stats()
        show_text(stats.timings, stats.unit, stream=stream)
