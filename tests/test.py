import unittest
import requests


# def soma(a, b):
#     return a+b

# class TestSoma(unittest.TestCase):
#     def test_soma(self):
#         self.assertEqual(soma(5, 5), 10, msg="5+5 = 10")
#         self.assertEqual(soma(3, 2), 5)
#         self.assertEqual(soma(4, 6), 10)
#         self.assertEqual(soma(4, 6), 10)



class ApiTest(unittest.TestCase):
    url = "http://127.0.0.1:5000/pessoas"
    url_obj = {
        "nome": "Marino Soares Costa",
        "endereco": "SãoVicente",
        "email": "marinoscosta@email.com.sv",
        "telefone": "13-97744-5566",
    }

    def test_get_all_pessoas(self):
        r = requests.get(ApiTest.url)
        self.assertEqual(r.status_code, 200)
        #self.assertEqual(len(r.json()), 6)

    # def test_post_pessoa(self):
    #     r = requests.post(ApiTest.url, json=ApiTest.url_obj)
    #     self.assertEqual(r.status_code, 201)

    def test_get_id_pessoa(self):
        id_pessoa = 5
        r = requests.get(f"{ApiTest.url}/{id_pessoa}")
        print(r)
        self.assertEqual(r.status_code, 200)
        # self.assertDictEqual(r.json(), ApiTest.url_obj)

    def test_update_get_id(self):
        pessoa_id = 16
        updPessoa = {
            "nome": "Marino Soares Costa",
            "endereco": "Santos",
            "email": "marinoscosta@email.com.st",
            "telefone": "13-97744-5566",
        }
        r = requests.put("{}/{}".format(ApiTest.url, pessoa_id), json = updPessoa)
        self.assertEqual(r.status_code, 204)


if __name__ == '__main__':
    unittest.main()
