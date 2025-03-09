class A:
    __aaa='hello'
    def all(self):
        print("123")
    def ab(self):
        print('screct',A.__aaa)
c= A()
c.ab()
c.__aaa