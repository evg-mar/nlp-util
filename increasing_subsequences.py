# -*- coding: utf-8 -*-
"""
@author: evgeniy

Given a sequence of integers to find all MAXIMAL increasing subsequences.
A maximal increasing subsequence is an increasing subsequence which can not
be enlarged to larger increasing subsequence of the original sequence.
I use a tree structure where the root contains a Node value,
all other nodes have a value corresponding to a value from  the
original sequence.

For example the sequence:  seq = [4,5,2,6,3,4,5]
has the following subsequences:
[4,5,6]
[2,6]
[2,3,4,5]

Therefore the largest subsequence is of length 4
"""

class Node(object):
    """
    Base node to be inherited.
    """
    def __init__(self, value=None, depth=None):
        self.value = value
        self.depth = depth
        
class NodeSeq(Node):
    """
    NodeSeq to hold:
    value -> corresponding to a value from the original sequence
    self.sequence -> subsequence corresponding to a subsequence from the
    self.original sequence with values greater than self.value
    """
    def __init__(self, value=None, depth=None, sequence=[]):
        super(NodeSeq, self).__init__(value, depth)
        self.sequence = sequence

    def splitSeq(self):
        """
        Split self.sequence into different corresponding parts
        contained in the pointers part of a NodeHolder
        """
        if len(self.sequence)==0:
            return NodeHolder(self.value, self.depth, [])
            
        pointers = []
        sequence = self.sequence
        while True:
            el01 = sequence[0]
            seq = filter(lambda el: el>el01, sequence)
            pointers.append(NodeSeq(el01, self.depth+1, seq))
            next_min = min(sequence)
            if(el01 == next_min):
                break
            else:
                idxmin = sequence.index(next_min)
                sequence = sequence[idxmin:]
        
        return NodeHolder(self.value, self.depth, pointers)

        
class NodeHolder(Node):

    def __init__(self, value=None, depth=None, pointers=[]):
        super(NodeHolder, self).__init__(value, depth)
        self.pointers = pointers

    def processNode(self):
        """
        Activate the process of splitting the original sequence into
        increasing subsequences.
        """
        if len(self.pointers) == 0:
            return
        for idx, nod in enumerate(self.pointers):
            nodHolder = nod.splitSeq()            
            nodHolder.processNode()            
            self.pointers[idx] = nodHolder
            
    def getLongestSubseq(self):
        if len(self.pointers) == 0:
            return [self.value]
        else:
            last_len = 0
            last_seq = []
            for nod in self.pointers:
                seq = nod.getLongestSubseq()
                seq_len = len(seq)                
                if last_len < seq_len:
                    last_len = seq_len
                    last_seq = seq
            return [self.value] + last_seq
                                
                
sequence = [4,5,2,6,3,4,5]
res01 = NodeSeq(None, 0, sequence).splitSeq()
res01.processNode()
seq = res01.getLongestSubseq()[1:]


