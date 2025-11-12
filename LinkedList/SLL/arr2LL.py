def arrayToList(arr):
        # code here
        Nodes = []
        for i in range(len(arr))  :
            node = Node(arr[i])
            node.next = None
            Nodes.append(node)
        for i in range(len(Nodes) -  1):
            Nodes[i].next = Nodes[i + 1]
        Nodes[-1].next = None
            
        return Nodes[0]
            