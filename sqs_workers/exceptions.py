class SQSError(Exception):
    pass


class FailedTasksError(SQSError):
    def __init__(self, result):
        self.result = result
        super(FailedTasksError).__init__("detected failed tasks")
