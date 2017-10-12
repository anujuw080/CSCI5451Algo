class Tree(object):
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def postorder(tree, passed_val, ret):
    if(tree is not None):
        postorder(tree.left, passed_val + '1', ret)
        postorder(tree.right, passed_val + '0', ret)
        if(len(tree.data[0]) == 1):
            # print(tree.data[0] + " " + passed_val)
            ret.append((tree.data[0], passed_val))

            
def huffman(txt):
    root = Tree()
    right_leaf = Tree()
    left_leaf = Tree()

    ret_list = []

    right_leaf.data = 25
    left_leaf.data = 20

    root.left = left_leaf
    root.right = right_leaf

    # str = "Hello Siddhant. Siddhant Be A Scouser! Forever!!"
    str = txt
    str_l = []

    for x in str:
        str_l.append(x)

    # print(str_l)

    freq_list = []
    # temp_char = None
    while((not str_l) == False):
        temp_str = str_l
        for x in temp_str:
            temp = 0
            while(True):
                if(x in temp_str):
                    temp = temp + 1
                    temp_str.remove(x)
                else:
                    break
            t = Tree()
            t.left = None
            t.right = None
            t.data = (x, temp)
            freq_list.append(t)
        str_l = list(temp_str)
        
    freq_list.sort(key=lambda t: t.data[1])
    freq_list.reverse()

    # print(freq_list)

    for x in freq_list:
        print(x.data)

    print("DONNEEEEE=====================")

    l = None
    r = None
    root = None
    while((len(freq_list)) > 1):

        print("ITERATION!!!!!")
        l = freq_list.pop()
        r = freq_list.pop()
        t = Tree()
        t.left = l
        t.right = r

        l_data = l.data[0]
        r_data = r.data[0]

        print(l_data)
        print(r_data)

        res = l_data + r_data

        print(res)

        t.data = (res, (l.data[1] + r.data[1]))
        # t.data[0] = res
        # t.data[1] = l.data[0] + r.data[0]
        root = t
        freq_list.append(t)
        freq_list.sort(key=lambda t: t.data[1])
        freq_list.reverse()
        
        for x in freq_list:
            print(x.data)
     #got the list

    #now create tree
    print(root.data[0])
    print(root.data[1])
    postorder(root, '', ret_list)
    print(ret_list)
    ret_list.sort(key=lambda t: len(t[1]))
    return list(ret_list)


#huffman("MISSISSIPPI RIVER")
  
