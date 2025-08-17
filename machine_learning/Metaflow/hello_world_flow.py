from metaflow import step, FlowSpec, conda_base


class HelloFlow(FlowSpec):
    @step
    def start(self):
        print("Starting 👋")
        self.next(self.eat)

    @step
    def eat(self):
        print("Eating 🍜")
        self.next(self.end)

    @step
    def end(self):
        print("Done! 🏁")


if __name__ == "__main__":
    HelloFlow()
