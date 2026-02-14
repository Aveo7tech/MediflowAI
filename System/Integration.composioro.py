from composio_langchain import ComposioToolSet
from config.settings import settings

class ToolRouter:

    def __init__(self):
        self.toolset = ComposioToolSet(api_key=settings.COMPOSIO_API_KEY)
        self.tools = self.toolset.get_tools()

    def get_tools(self):
        return self.tools
