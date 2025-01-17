
# <START-OF-CODE>

import sys

class TaskB:
    def solve(self, testNumber, in, out):
        x = in.next()
        s = []
        c = 0
        for i in range(len(x)):
            s.append(x[i])
            while len(s) > 1:
                p = s.pop()
                q = s.pop()
                if (p == '1' and q == '0') or (p == '0' and q == '1'):
                    c += 1
                    continue
                else:
                    s.append(q)
                    s.append(p)
                    break
        out.println(c * 2)

class InputReader:
    def __init__(self, stream):
        self.reader = BufferedReader(InputStreamReader(stream), 32768)
        self.tokenizer = None

    def next(self):
        while self.tokenizer == None or not self.tokenizer.hasMoreTokens():
            try:
                self.tokenizer = StringTokenizer(self.reader.readLine())
            except IOException as e:
                raise RuntimeException(e)
        return self.tokenizer.nextToken()

class Main:
    def main(self, args):
        inputStream = System.in
        outputStream = System.out
        in = InputReader(inputStream)
        out = PrintWriter(outputStream)
        solver = TaskB()
        solver.solve(1, in, out)
        out.close()

if __name__ == '__main__':
    Main().main(sys.argv)

# 