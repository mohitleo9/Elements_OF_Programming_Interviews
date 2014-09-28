def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks > 0:
        helperPeg = 6 - startPeg - endPeg

        hanoi(ndisks-1, startPeg, helperPeg)
        print "Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg)
        hanoi(ndisks-1, helperPeg, endPeg)

hanoi(ndisks=3)
