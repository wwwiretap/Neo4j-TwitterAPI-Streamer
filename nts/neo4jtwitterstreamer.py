from nts.twitterstreamhandler import TwitterStreamHandler
from nts.graphhandler import GraphHandler
from nts.confighandler import Config

from threading import Timer


class Neo4jTwitterStreamer(object):
    def __init__(self, graphhandler: GraphHandler, settings: dict = None):
        if settings:
            Config.set_settings(settings)

        self.graph_handler = graphhandler
        self.twitter_stream_handler = TwitterStreamHandler(
            self.graph_handler.on_data)
        self.filter_list = []
        self.running = False
        self.timed = False
        self.timer = ''

    def add_filter(self, filter):
        if type(filter) == str:
            self.filter_list.append(filter)
        elif type(filter) == list:
            self.filter_list = self.filter_list + filter

    def remove_filter(self, fileter: str):
        self.filter_list.remove(fileter)

    def get_filter(self) -> list:
        return self.filter_list

    def start_async_stream(self):
        if not self.running:
            self.running = True
            self.twitter_stream_handler.start_filter(self.filter_list, True)
        else:
            print('Stream already running')

    def stop_async_stream(self):
        if self.running:
            self.twitter_stream_handler.stop_filter()
            self.running = False
            if self.timed:
                self.timer.cancel()
                self.timed = False
        else:
            print('Not streaming')

    def start_async_stream_timed(self, time: int):
        if not self.running:
            self.start_async_stream()
            self.timed = True
            self.timer = Timer(time, self.stop_async_stream)
            self.timer.start()
        else:
            print('Stream already running')

    def start_blocking_stream(self):
        self.running = True
        self.twitter_stream_handler.start_filter(self.filter_list, False)
