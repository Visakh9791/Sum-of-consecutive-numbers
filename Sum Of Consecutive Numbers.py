def sum_cons_num(int_num_list):
    cons_num_list=[]
    for index in range(len(int_num_list)-1):
        cons_num=int_num_list[index] + int_num_list[index +1]
        cons_num_list.append(cons_num)
    return cons_num_list
    

def sum_triangular_cons(int_num_list):
    while len(int_num_list) > 1:
        new_list=sum_cons_num(int_num_list)
        print(new_list)
        int_num_list=new_list


def convert_str_to_int(str_num_list):
    int_list=[]
    for item in str_num_list:
        num=int(item)
        int_list.append(num)
    return int_list




str_num_list=input().split(",")
int_num_list=convert_str_to_int(str_num_list)
print(int_num_list)
#cons_result=sum_cons_num(int_num_list)
#print(cons_result)
tri_cons_result=sum_triangular_cons(int_num_list)