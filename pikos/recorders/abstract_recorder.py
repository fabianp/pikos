import abc


class RecorderError(Exception):
    pass

class AbstractRecorder(object):
    """ Abstract recorder class.

    A recorder is reposnible for storing the record data that are provided by
    the logger or profiler. The records are expected to be nametuple-like
    classes.

    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def prepare(self, record):
        """ Perform any setup required before the recorder is used.

        Parameters:
        record : NamedTuple
            An instance of the record class that is going to be used.

        """

    @abc.abstractmethod
    def finalize(self):
        """ Perform any tasks to finalize and clean up when the recording
        is completed.

        """

    @abc.abstractmethod
    def record(self, data):
        """ Record a measurement.

        Parameters:
        data : NamedTuple
            An instance of the record class that is going to be used.

        """
