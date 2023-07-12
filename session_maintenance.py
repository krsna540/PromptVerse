import os
import json
import gc
import uuid
import datetime
import tempfile
import errno
from session import Session, PromptModel, PromptCollection


class SessionMaintenance:
    def __init__(self, session_descriptor: Session):
        self.session_descriptor: Session = session_descriptor

    def __isWritable(self):
        try:
            testfile = tempfile.TemporaryFile(
                dir=self.session_descriptor.offline_folder_path)
            testfile.close()
        except OSError as e:
            if e.errno == errno.EACCES:  # 13
                return False
            e.filename = self.session_descriptor.offline_folder_path
            raise
        return True

    def __validate_offline_storage(self):
        if self.session_descriptor.offline_folder_path == "" or self.session_descriptor.offline_folder_path is None:
            self.session_descriptor.offline_folder_path = "."
        return self.__isWritable()

    def __activate_storage(self):
        """Create a json file if file doesn't exists"""
        self.session_descriptor.filename = self.session_descriptor.session_id+".json"
        if not os.path.exists(self.session_descriptor.filename):
            f = open(self.session_descriptor.offline_folder_path+self.session_descriptor.filename,
                     'w')  # open file in append mode
            session_obj = json.dumps(
                vars(self.session_descriptor), default=lambda o: o.__dict__)
            f.write(session_obj)
            f.close()

    def create(self):
        """create : creating a session with DB entry or offline entry for session. All the activities will be tracked in that session node created.
        """
        storage_status = self.__validate_offline_storage()
        if storage_status:
            self.session_descriptor.active_status = True
            self.__activate_storage()
        else:
            print("Unable to create session storage for saving the session as required")
            self.stop_session()

    def stop_session(self):
        """stop_session : Stop the session and close the storage objects
        """
        self.session_descriptor.active_status = False
        gc.collect()

    def update_storage(self):
        pass

    def add_prompt(self, model: PromptModel):
        self.session_descriptor.registry.append(model)