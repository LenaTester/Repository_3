from restapi_lesson.base_api import BaseAPI


class MatrixPersonAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.user_url = "/api/users"
