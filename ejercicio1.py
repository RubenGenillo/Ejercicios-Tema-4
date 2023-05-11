import sys

class Heap:
    def __init__(self):
        self.vector = []
        self.tamanio = 0

    def agregar(heap, valor):
        heap.vector.append(valor)
        heap.flotar(heap.tamanio)
        heap.tamanio += 1

    def flotar(heap, indice):
        while(indice > 0):
            if(heap.vector[indice].valor > heap.vector[(indice - 1) // 2].valor):
                aux = heap.vector[indice]
                heap.vector.pop(indice)
                heap.vector.insert((indice - 1) // 2, aux)
                indice = (indice - 1) // 2
            else:
                break
    
    def quitar(heap, dato):
        valor = heap.vector[dato]
        heap.vector[dato] = heap.vector[-1]
        heap.vector.pop()
        if heap.tamanio > 1:
            Heap.hundir(heap, dato)
        heap.tamanio -= 1
        return valor
    
    def hundir(heap, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while(control and hijo_izq < heap.tamanio-1):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < heap.tamanio-1):
                if(heap.vector[hijo_der].valor > heap.vector[hijo_izq].valor):
                    aux = hijo_der
            if(heap.vector[indice].valor < heap.vector[aux].valor):
                naux = heap.vector[indice]
                heap.vector[indice] = heap.vector[aux]
                heap.vector[aux] = naux                
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False



class nodoArbol():
    def __init__(self, valor, letra):
        self.valor = valor
        self.letra = letra
        self.izq = None
        self.der = None
    
    def insertar_nodo(raiz, nodo):
        if raiz is None:
            raiz = nodoArbol(nodo)
        elif nodo.valor < raiz.valor:
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, nodo)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, nodo)
        return raiz

    def eliminar_nodo(raiz, clave):
        x = None
        if(raiz is not None):
            if(clave < raiz.valor):
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.valor):
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.valor
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.valor
        return raiz, x
    
    def remplazar(raiz):
        aux = None
        if(raiz.der is None):
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux   


class huffman:
    def __init__(self, valor, letras):
        self.heap = Heap()
        dividir = sum(valor)
        for posicion in range(len(valor)):
            nodoAux = nodoArbol(valor[posicion]/dividir, letras[posicion])
            self.heap.agregar(nodoAux)
        self.__ordenar()

    def __ordenar(self):
        if self.heap.tamanio >= 2:
            nodoAux = nodoArbol(None, None)
            nodoAux.izq = self.heap.quitar(-1)
            nodoAux.der = self.heap.quitar(-1)
            nodoAux.valor = nodoAux.izq.valor + nodoAux.der.valor
            self.heap.agregar(nodoAux)        
            self.__ordenar()

    def leer(self, texto):
        buscador = self.heap.vector[0]
        cadena = ""
        for i in texto:
            if i == "0":
                if buscador.izq is not None:
                    buscador = buscador.izq
                else:
                    cadena += buscador.letra
                    buscador = self.heap.vector[0]
            else:
                if buscador.der is not None:
                    buscador = buscador.der
                else:
                    cadena += buscador.letra
                    buscador = self.heap.vector[0]
        return cadena
    
def main():
    cantidad = [11, 2, 4, 3, 14, 3, 6, 6, 3, 6, 7, 4, 1, 10, 4, 3, 4, 2, 17, 2]
    caracter = ["A", "B", "C", "D", "E", "G", "I", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", " ", ","]    
    huff = huffman(cantidad, caracter)
    print(huff.leer("10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"))
    print(huff.leer("0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"))
    print("mensaje1 binario: ", sys.getsizeof(huff.leer("10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100")), "mensaje1 original:", sys.getsizeof("GIDMDNTBDDBDGDNQSGDTGIDDPSGDDTPTSBQT,DQODDDGDDCNCBTQNGPTUTMUDQNDDDQDDUNPGDDGGDTTNPTDDQMTBSUNMDGTNPDTTPTSBQTDT"))
    print("mensaje2 binario: ", sys.getsizeof(huff.leer("0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010")), "mensaje2 original: ", sys.getsizeof("TPONTPDTDNQBMPCDGDDTCSPDTDNGTUPTUMMDTTUBDT"))
if __name__ == "__main__":
    main()