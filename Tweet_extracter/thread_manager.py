class thread_manager:
    def __init__(self):
        self.active_threads = []

    def add_thread(self, thread):
        self.active_threads.append(thread)

    def remove_thread(self, thread):
        self.active_threads.remove(thread)

    def kill_threads(self):
        for thread in self.active_threads:
            thread._stop()
            self.remove_threads(thread)
