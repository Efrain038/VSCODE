class A:
    def hablar(self):
        print("estoy hablando desde A")


class B(A):
    def hablar(self):
        print("estoy hablando desde B")


class C(A):
    def hablar(self):
        print("estoy hablando desde C")


class D(B,C):
    def hablar(self):
        print("estoy hablando desde D")

class E(D,A):
    def hablar(self):
        print("estoy hablando desde E")



class F(E,A):
    def hablar(self):
        print("estoy hablando desde F")



class G(E,D):
    def hablar(self):
        print("estoy hablando desde G")



class H(G,F,D):
    def hablar(self):
        print("estoy hablando desde H")



d = H()

print(H.mro())




























































































