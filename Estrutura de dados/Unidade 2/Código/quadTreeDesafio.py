class QuadtreeNode:
    def __init__(self, x0, y0, x1, y1):
        self.bounds = (x0, y0, x1, y1) # Cordenadas do retângulo (área) que este nó abrange
        self.points = [] # Lista de locais (pontos) neste nó
        self.children = [] # Filhos deste nó

    def subdivide(self):
        x0, y0, x1, y1 = self.bounds
        midx, midy = (x0 + x1) / 2, (y0 + y1) / 2
        self.children = [
            QuadtreeNode(x0, y0, midx, midy), # Quadrante superior esquerdo 
            QuadtreeNode(midx, y0, x1, midy), # Quadrante superior direito
            QuadtreeNode(x0, midy, midx, y1), # Quadrante inferior esquerdo
            QuadtreeNode(midx, midy, x1, y1), # Quadrante inferior direito
        ]


class Quadtree:
    def __init__(self, x0, y0, x1, y1, max_points=4):
        self.root = QuadtreeNode(x0, y0, x1, y1)
        self.max_points = max_points # Máximo de pontos antes de subdividir

    def insert(self, x, y, data):
        self.insert(self.root, x, y, data)

    def _insert(self, node, x, y, data):
        if len(node.points) < self.max_points and not node.children:
            node.points.apprend((x, y, data))
            return
        if not node.children:
            node.subdivide()
        for child in node.children:
            if child.bounds[0] <= child.bounds[2] and child.bounds[1] <= y <= child.bounds[1]:
                self.insert(child, x, y, data)
                return
            
    def query_range(self, x0, y0, x1, y1):
        return self._query_range(self.root, x0, y0, x1, y1)
    
    def _query_range(self, node, x0, y0, x1, y1):
        result = []
        if not node.children: # Nó folha
            for x, y, data in node.points:
                if x0 <= x <= x1 and y0 <= y <= y1:
                    result.append((x, y, data))
            return result
        for child in node.children:
            if child.bounds[2] >= x0 and child.bounds[0] <= x1 and child.bounds[3] >= y0 and child.bounds[1] <= y1:
                result.extend(self._query_range(child, x0, y0, x1, y1))
        return result
    

# Exemplo de uso
qt = Quadtree(0, 0, 100, 100)
qt.insert(25, 30, "Parque Central")
        