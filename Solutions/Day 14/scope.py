class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        self.maximumDifference = None
        for i in range(0, len(self.__elements)):
            for j in range(i+1, len(self.__elements)):
                diff = abs(a[i]-a[j])
                if not self.maximumDifference or self.maximumDifference < diff:
                    self.maximumDifference = diff


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
