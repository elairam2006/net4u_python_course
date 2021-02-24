def add_ip(list,ip1,ip2,ip3):
    print("List inside def: " +str(list))
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list

ip_list=[]
ip_n1=input("Enter an ip: ")
ip_n2=input("Enter an ip: ")
ip_n3=input("Enter an ip: ")
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
print(ip_list)

#################################
def add_ip2(ip1,ip2,ip3):
    list=[]
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list

ip_list=[]
ip_n1=input("Enter an ip: ")
ip_n2=input("Enter an ip: ")
ip_n3=input("Enter an ip: ")
ip_list=add_ip2(ip_n1,ip_n2,ip_n3)
ip_list=add_ip2(ip_n1,ip_n2,ip_n3)
print(ip_list)