"""
@brief      test log(time=17s)

"""
import os,sys,unittest

try :
    import src
    import pyquickhelper
    import pyensae
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyensae", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper
    import pyensae

from pyquickhelper import fLOG
from src.ensae_teaching_cs.special.rues_paris import get_data, bellman, kruskall, possible_edges, eulerien_extension, distance_paris, euler_path, connected_components, distance_haversine, graph_degree

class TestTranslate(unittest.TestCase):

    def test_translate(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        data = os.path.join(os.path.abspath(os.path.dirname(__file__)),"data")
        russe = os.path.join(data,"russe.txt")
        assert os.path.exists(russe)
        with open(russe, "r", encoding="utf8") as f :
            lines = f.readlines()
        lines = [ _ .strip(" \r\n\t") for _ in lines ]
        lines = [ _ for _ in lines if not _.startswith("#") and len(_) > 0 ]

        temp = os.path.join(data,"..","temp_translate")
        if not os.path.exists(temp): os.mkdir(temp)
        dest = os.path.join(temp, "out_russe_en.txt")

        if not os.path.exists(dest):
            import goslate
            gs = goslate.Goslate()
            tlines = []
            for l in lines:
                tt = gs.translate(l, 'en', 'ru')
                tlines.append(tt)

            with open(dest,"w",encoding="utf8") as f :
                f.write("\n\n".join(tlines))

        assert os.path.exists(dest)


if __name__ == "__main__"  :
    unittest.main ()