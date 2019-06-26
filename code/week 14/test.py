class Algorithm ():
    point_list = []
    edge_list = []

    def dijkstra(self, start_point, point_list, edge_list):
        # 列表点
        temp_point = []
        # 起始点，在列表点中的位置
        point_index = point_list.index (start_point)
        # 初始点到其余各点的距离字典
        dis_dic = dict ()
        # 边列表的首端点列表
        temp_edge = []
        # 距离初始化
        dis_list = ['inf'] * len (point_list)
        temp_point.append (start_point)
        dis_list[point_index] = 0
        for i in range (len (point_list)):
            dis_dic.setdefault (point_list[i], dis_list[i])
        for i in range (len (edge_list)):
            temp_edge.append (edge_list[i][0])
        point = start_point
        # 依次遍历加入最小距离的点，并更新原列表中点的距离
        while len (temp_point) < len (point_list):
            index = self.find_index (point, temp_edge, edge_list, temp_point)
            # 判断是否走的通
            if len (index) > 0:
                value = edge_list[index[0]][2]
                add_index = index[0]
                for i in index:
                    if edge_list[i][0] in dis_dic:
                        dis_dic[edge_list[i][1]] = min (float (edge_list[i][2]) + float (dis_dic[point]),
                                                        float (dis_dic[edge_list[i][1]]))
                    if value > edge_list[i][2]:
                        value = edge_list[i][2]
                        add_index = i
                temp_point.append (edge_list[add_index][1])
                point = edge_list[add_index][1]
            else:
                point = in_list[in_list.index (point) - 1]
        print
        dis_dic
        return dis_dic

    def find_index(self, point, temp_edge, edge_list, temp_point):
        '''
        @point:遍历点基准点
        @temp_edge：边列表的首端点列表
        @edge_list：边权列表
        @temp_point：列表点
        @返回边权列表列表索引
        '''
        # 寻找点的索引，并去除已在列表中的点
        index = []
        for i in range (len (temp_edge)):
            if point == temp_edge[i] and edge_list[i][1] not in temp_point:
                index.append (i)
        return index


if __name__ == "__main__":
    print
    '请输入无向图的顶点'
    point_list = input ()
    print
    '请输入无向图的边'
    edge_list = list (input ())
    print
    '请输入各边长度'
    for i in range (len (edge_list)):
        print
        '顶点' + str (edge_list[i][0]) + '顶点' + str (edge_list[i][1]) + '的长度为：'
        length = [input ("长度为：")]
        edge_list[i] += length
        edge_list.append ([edge_list[i][1], edge_list[i][0], length[0]])
    while True:
        print
        '请输入起始点'
        start_point = input ("start_point=")
        if start_point in point_list:
            obj = Algorithm ()
            obj.dijkstra (start_point, point_list, edge_list)
            break
        else:
            print
            '该点不在图中，请重新输入:'
            continue