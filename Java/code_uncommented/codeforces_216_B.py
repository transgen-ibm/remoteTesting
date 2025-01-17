
import java.util.Iterator ; import java.util.LinkedList ; import java.util.Scanner ; class Main:
    def __init__(self):
        self.count = 0
        self.seen = [False] * 100000
        self.path = 0
        self.cycle = 1
        self.graph = []
        for i in range(100000):
            self.graph.append(LinkedList())

    def dfs(self, child, par):
        if self.seen[child]:
            return self.cycle
        self.seen[child] = True
        for i in self.graph[child]:
            if i!= par:
                self.count += 1
                if self.dfs(i, child) == self.cycle:
                    return self.cycle
        return self.path

    def main(self):
        sc = Scanner(System.in)
        m = sc.nextInt()
        n = sc.nextInt()
        ft = Main()
        for i in range(m+1):
            ft.graph.add(LinkedList())
        ft.seen = [False] * (m+1)
        for i in range(n):
            x = sc.nextInt()
            y = sc.nextInt()
            ft.graph.get(x).add(y)
            ft.graph.get(y).add(x)
        toremove = 0
        for i in range(1, m+1):
            if not ft.seen[i]:
                ft.count = 0
                if ft.dfs(i, 0) == ft.cycle:
                    if ft.count % 2 == 1:
                        toremove += 1
        if (m - toremove) % 2 == 1:
            toremove += 1
        System.out.println(toremove)

