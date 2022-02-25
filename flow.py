from metaflow import FlowSpec, step


class MetaflowFlow(FlowSpec):
    @step
    def start(self):
        print("start")
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    MetaflowFlow()
