from .construct import Construct


class Settings(Construct):

    def get(self):
        """
        Get Workspace information.

        :return: Object including the workspace id, name and slug
        :rtype: papi.common.common.Object
        """
        return self._segment.get('/').workspace
