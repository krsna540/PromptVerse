import os
import json
import gc
import uuid
import datetime
import tempfile
import errno


class PromptCollection:
    """prompt_collection : storing everything related to multiple versions of prompts
    """

    def __init__(self, prompt_text: str = "", version: int = 0):
        self.prompt_text: str = prompt_text
        self.created_timestamp: str = str(datetime.datetime.now())
        self.prompt_template: str = None
        self.version: int = version
        self.executable: bool = False
        self.output: str = None
        self.metrics = []
        self.response_time: float = None


class PromptModel:
    """PromptModel- to store complete information about a prompt and encapsulation of prompt collections
    """

    def __init__(self, name, description):
        self.prompt_id: str = uuid.uuid4().hex
        self.name = name
        self.description = description
        self.created_timestamp: str = str(datetime.datetime.now())
        self.updated_timestamp: str = str(datetime.datetime.now())
        self.collection: list = []


class Session:
    """PromptVerseSession : for creating a session with  offline storage -  local storage json path to store data.
       Methods - create,load_session,stop_session
    """

    def __init__(self, name: str, description: str, offline_folder_path: str):
        self.name = name
        self.description = description
        self.session_id: str = uuid.uuid4().hex
        self.active_status: bool = False
        self.offline_folder_path: str = offline_folder_path
        self.created_timestamp: str = str(datetime.datetime.now())
        self.update_timestamp: str = str(datetime.datetime.now())
        self.filename = None
        self.registry: list = []