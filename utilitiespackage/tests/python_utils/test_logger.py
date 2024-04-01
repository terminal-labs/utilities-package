from utilitiespackage.python_utils.logger import Logged


def test_logged():
    class MyClass(Logged):
        def __init__(self):
            Logged.__init__(self)

    my_class = MyClass()
    my_class.debug("debug")
    my_class.log(0, "log")
    my_class.debug("debug")
    my_class.info("info")
    my_class.warning("warning")
    my_class.error("error")
    my_class.exception("exception")
    my_class.log(0, "log")
