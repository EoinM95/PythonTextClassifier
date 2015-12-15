from classifieur import Instance, most_common, classify_instance, read_instances, predict, eval_classif, compute_coords, read_word_instances
import unittest


class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.inst = [Instance("orange", (0, 0)),
                   Instance("orange", (0, 5)),
                   Instance("orange", (-8, 49)),
                   Instance("citron", (499, 1100)),
                   Instance("orange", (50, 0)),
                   Instance("citron", (1200, 768)),
                   Instance("orange", (9, 9)),
                   Instance("citron", (999, 666)),
                   Instance("citron", (1394, 1988)),
                   Instance("citron", (1001, 1002))]

    def test_Instance_str(self):
        string = str(self.inst[0])
        self.assertNotEqual(string,repr(self.inst[0]),"Il faut implémenter __str__")
        self.assertIsInstance(string,str,"__str__ doit renvoyer une str")

    def test_InstanceDistance(self):
        d = self.inst[0].distance(self.inst[1])
        self.assertIsInstance(d,float,"La distance doit être de type float.")

    def test_Instanceknn(self):
        neighbors = self.inst[0].knn(3,self.inst[1:])
        self.assertEqual(len(neighbors),3,"La fonction knn doit renvoyer k voisins.")
        self.assertIsInstance(neighbors,list,"La fonction knn doit renvoyer une liste.")
        self.assertTrue(all(type(x) is Instance for x in neighbors),"La fonction knn doit renvoyer une liste d'instances.")

    def test_mostcommon(self):
        cat = most_common(self.inst)
        self.assertIsInstance(cat,str,"La fonction most_common doit renvoyer une str")

    def test_classify_instance(self):
        cat = classify_instance(5,self.inst[0],self.inst[1:])
        self.assertIsInstance(cat,str,"La fonction classify_instance doit renvoyer une str")

    def test_read_instances(self):
        lread = read_instances("orangeTest.txt")
        self.assertTrue(all(type(x) is Instance for x in lread),
                        "La fonction read_instances doit renvoyer une liste d'instances")

    def test_predict(self):
        p = predict(self.inst[:5],self.inst[5:],3)
        self.assertIs(p, None)

    def test_eval_classif(self):
        result = eval_classif([Instance("orange", (0, 5)), Instance("orange", (-8, 49))],
                         [Instance("citron", (0, 5)), Instance("orange", (-8, 49))])

        self.assertIsInstance(result,float,"La fonction eval_classif doit renvoyer un float")


    def test_compute_coords(self):
        coord = compute_coords(["Le", "chat", "dort"])
        self.assertIsInstance(coord,tuple,"Les coordonnées doivent être un tuple")
        self.assertTrue(all(x == 0 or x ==1 for x in coord),"Les coordonnées doivent valoir 0 ou 1")


    def test_read_word_instances(self):
        lread = read_word_instances("trigramTest.txt")
        self.assertTrue(all(type(x) is Instance for x in lread),
                        "La fonction read_word_instances doit renvoyer une liste d'instances")
