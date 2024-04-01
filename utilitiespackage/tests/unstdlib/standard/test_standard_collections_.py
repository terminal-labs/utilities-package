from utilitiespackage.unstdlib.standard.collections_ import RecentlyUsedContainer


def test_standard_collections_recentlyusedcontainer():
    ruc = RecentlyUsedContainer()
    ruc["1"] = 1
    ruc["2"] = 2
    ruc["3"] = 3
    ruc["4"] = 4
    ruc["5"] = 5
    ruc["6"] = 6
    ruc["7"] = 7
    ruc["8"] = 8
    ruc["9"] = 9
    ruc["10"] = 10
    ruc["11"] = 11
