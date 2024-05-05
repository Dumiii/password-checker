import signal

class SignalHandler:
    shutdown = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

    def request_shutdown(self):
        print("Shutdown request received, stopping")
        self.shutdown = True

    def can_run(self):
        return not self.shutdown
