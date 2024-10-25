
class BaseTask:
  def __init__(self, task_name: str):
    self.task_name = task_name
    print("Hello World!")

  def run(self):
    print("Program starts running task: ", self.task_name)