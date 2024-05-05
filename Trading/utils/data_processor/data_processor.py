from abc import abstractmethod
from logging import Logger
import signal
from Trading.utils.data_processor.file_rw import FileRW
from typing import Optional


"""
    Process large amounts of data in a JSON file incrementally.
    The data is stored in a dictionary and the processor keeps track of the current step being processed.
    The processor can be interrupted with a SIGINT signal and the data will be saved to the file.
    The processor is meant to be subclassed and the _process_data method should be implemented.
    The process_item method should be implemented to process a single item, if iterate_items is used.
"""


class DataProcessor:
    def __init__(
        self, file_rw: FileRW, logger: Logger, should_read: Optional[bool] = True
    ):
        self.file_rw = file_rw
        self.logger = logger

        if should_read:
            try:
                self.data = file_rw.read()
                self.logger.info(
                    f"Read from file: {self.file_rw.file_name} data of len {len(self.data)}"
                )
            except Exception as e:
                self.logger.error(
                    f"Failed to read from file: {self.file_rw.file_name}, starting with empty data."
                )
                self.data = {}
        else:
            self.data = {}

        # Setup the signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)

    @abstractmethod
    def _process_data(self, *args, **kwargs):
        """Template method for processing data."""
        ...

    def iterate_items(self, items, *args, **kwargs):
        """General iteration method for processing items."""
        items_len = len(items)
        if len(self.data) == items_len:
            self.logger.info("All items already processed, skipping...")
            return

        for item in items:
            if item in self.data:
                self.logger.info(f"Item {item} already processed, skipping...")
                continue

            self.process_item(item, *args, **kwargs)
            self.logger.info(f"Processed item {item} {len(self.data)} / {items_len}")
        self.logger.info("Finished processing all items.")

    @abstractmethod
    def process_item(self, item, *args, **kwargs):
        """Process a single item."""
        pass

    def _signal_handler(self, signum, frame):
        """Handles the SIGINT signal."""
        self.logger.info("Interrupt signal received, saving data...")
        self.file_rw.write(self.data)
        self.logger.info("Data saved, exiting.")
        exit(0)

    def run(self, *args, **kwargs):
        """Main method to run the processor."""
        try:
            self._process_data(*args, **kwargs)
        except Exception as e:
            raise e
        self.file_rw.write(self.data)
