""" Built-in Decorators """

class Demo:
  @staticmethod
  def static_method():
      print("I am a static method!")

  @classmethod
  def class_method(cls):
      print(f"I am a class method of {cls}")

Demo.static_method()
Demo.class_method()