

class BaseEndpoint:
    res = None
    res_json = None

    def check_status_is_200(self):
        assert self.res.status_code == 200

    def check_status_is_404(self):
        assert self.res.status_code == 404
