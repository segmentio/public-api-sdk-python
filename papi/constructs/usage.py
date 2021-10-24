from ..lib import Command
from ..common import common
from .construct import Construct


class Usage(Construct):  # https://api.segmentapis.com/docs/usage/api-calls/#get-daily-workspace-api-calls-usage

    def __init__(self, segment):
        super().__init__(segment)
        self.sources = Sources(segment)
        self.workspace = Workspace(segment)


class Sources(Construct):

    def __init__(self, segment):
        super().__init__(segment)
        self.api = common.bunch(daily=Command(self.daily, 'api-calls', 'dailyPerSourceAPICallsUsage'))
        self.mtu = common.bunch(daily=Command(self.daily, 'mtu', 'dailyPerSourceMTUUsage'))

    def daily(self, metric, attr, period):
        print(period)
        return self._segment.iterator(f'/usage/{metric}/sources/daily', attr)


class Workspace(Construct):

    def __init__(self, segment):
        super().__init__(segment)
        self.api = common.bunch(daily=Command(self.daily, 'api-calls', 'dailyWorkspaceAPICallsUsage'))
        self.mtu = common.bunch(daily=Command(self.daily, 'mtu', 'dailyWorkspaceMTUUsage'))

    def daily(self, metric, attr, period):
        print(period)
        return self._segment.iterator(f'/usage/{metric}/daily', attr)
