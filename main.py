import os
from time import sleep

R = 12
def revise_rules():
    num = input("请输入您想修改的规则编号")

    print("----请输入修改后的规则----")
    features = input("请输入动物特征，以逗号分割：")
    features = features.split(",")
    has_feature = ""
    for i in range(len(features)):
        has_feature += "has_feature({}),\n\t".format(features[i])
    Class = input("请输入动物类别：")
    Rec = input("请告诉我这是什么动物：")
    id = "\n%{}\n".format(num)
    rule = id + "animal_rec({}) :- \n\t".format(Rec) + has_feature + "animal_class({}),\n\t".format(Class) + \
           "write('这个动物是{}'), nl.".format(Rec)

    with open('./animal_rec_system.pl', 'r') as plfile:
        content = plfile.read()
        ind = content.find(num)
        replacestr = ""
        while ind < len(content) and content[ind] != ".":
            replacestr += content[ind]
            ind += 1
        replacestr += "."
        print(replacestr)
        target = content.replace(replacestr, rule)
        plfile.close()

    with open('./animal_rec_system.pl', 'w') as plfile:
        plfile.write(target)
        plfile.close()

def delete_rules(num):
    with open('./animal_rec_system.pl', 'r') as plfile:
        content = plfile.read()
        ind = content.find(num)
        replacestr = ""
        while ind < len(content) and content[ind] != ".":
            replacestr += content[ind]
            ind += 1
        print(replacestr)
        target = content.replace(replacestr, "")
        plfile.close()
    with open('./animal_rec_system.pl', 'w') as plfile:
        plfile.write(target)
        plfile.close()
def add_rules():
    # if动物有毛发 and 动物有奶 then 动物是哺乳动物
    global R
    R += 1
    num = "\n%R{}\n".format(R)
    features = input("请输入动物特征，以逗号分割：")
    features = features.split(",")
    has_feature = ""
    for i in range(len(features)):
        has_feature += "has_feature({}),\n\t".format(features[i])
    Class = input("请输入动物类别：")
    Rec = input("请告诉我这是什么动物：")
    rule = num + "animal_rec({}) :- \n\t".format(Rec) + has_feature + "animal_class({}),\n\t".format(Class) + \
           "write('这个动物是{}'), nl.".format(Rec)
    with open('./animal_rec_system.pl', "a+") as plfile:
        plfile.write(rule)
        plfile.close()

sleep(0.4)
print('-----------------------------------------------------------------')
sleep(0.4)
print('*****************************************************************')
sleep(0.2)
print('###################||| EXPERT SYSTEM |||#########################')
sleep(0.4)
print('*****************************************************************')
sleep(0.4)
print('-----------------------------------------------------------------')

#添加规则
a = input("您是否想要增加一些知识库规则(Yes or No):")
while a == "Yes":
    add_rules()
    a = input("您是否还想要增加一些知识库规则(Yes or No):")

#添加规则
b = input("您是否想要删除一些知识库规则(Yes or No):")
while b == "Yes":
    num = input("请输入您想删除的规则编号")
    delete_rules(num)
    print("删除规则成功")
    b = input("您是否还想要删除一些知识库规则(Yes or No):")

c = input("您是否想要修改一些知识库规则(Yes or No):")
while c == "Yes":
    revise_rules()
    print("修改规则成功")
    c = input("您是否还想要修改一些知识库规则(Yes or No):")

cmd = "swipl -s ./animal_rec_system.pl"
os.system(cmd)
