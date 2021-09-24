"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
"""
import numpy as np
class Node(object):
    def __init__(self,name,num):
        self.name=name
        self.index=num

def findItinerary(tickets):
    start = "JFK"
    res = []
    node_name_list=[]
    node_list = []
    path_matrix = np.zeros((5,5))
    cnt=0
    # 构造节点，邻接矩阵
    for index,val in enumerate(tickets):
        if val[0] not in node_name_list:
            node_name_list.append(val[0])
            new_node = Node(val[0],cnt)
            node_list.append(new_node)
            if val[0]=='JFK':
                start_row = index
            index_row = cnt
            cnt+=1
        if val[1] not in node_name_list:
            node_name_list.append(val[1])
            new_node = Node(val[1],cnt)
            node_list.append(new_node)
            index_col = cnt
            cnt+=1
            
        path_matrix[index_row][index_col] = 1

    
    return res


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
findItinerary(tickets)