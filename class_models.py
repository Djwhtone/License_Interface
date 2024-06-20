class Agency():
    def __init__(self, provider_name):
        self.provider_name = provider_name

    def __str__(self):
        return f'\nAgency: {self.provider_name}'