from _typeshed import Incomplete

from ..config import PyPIRCCommand

class register(PyPIRCCommand):
    description: str
    list_classifiers: int
    strict: int
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def check_metadata(self) -> None: ...
    def classifiers(self) -> None: ...
    def verify_metadata(self) -> None: ...
    def send_metadata(self) -> None: ...
    def build_post_data(self, action): ...
    def post_to_server(self, data, auth: Incomplete | None = ...): ...