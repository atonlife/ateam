
class JiraCFG:

    def __init__(self, config: dict) -> None:
        self.server = config.get('server')
        self.user = config.get('user')
        self.password = config.get('password')
