from pj.factories.amazon_credentials_container_factory import AmazonCredentialsContainerFactory

class CSVManagerClient:
    def __init__(self, filename, output_relative_path='', input_absolute_path=None):
        self.input_absolute_path = input_absolute_path
        self.output_relative_path = output_relative_path
        self.filename = filename
        self.relative_output_route = None
        self.absolute_input_route = None


    def get_input_absolute_path(self):
        if not self.input_absolute_path:
            self.input_absolute_path = AmazonCredentialsContainerFactory \
                .get_default_instance().get_absolute_path()
        return self.input_absolute_path


    def set_input_absolute_path(self, input_absolute_path):
        self.input_absolute_path = input_absolute_path


    def get_output_relative_path(self):
        return self.output_relative_path


    def set_output_relative_path(self, output_relative_path):
        self.output_relative_path = output_relative_path


    def get_relative_output_route(self):
        if not self.relative_output_route:
            self.relative_output_route = ''.join([self.output_relative_path, self.filename])
        return self.relative_output_route


    def get_absolute_input_route(self):
        if not self.absolute_input_route:
            self.absolute_input_route = ''.join([self.get_input_absolute_path(), self.filename])
        return self.absolute_input_route
