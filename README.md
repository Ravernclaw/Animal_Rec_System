#A Simple Animal Recognization System Based On Production Rules
##Abstract
This project achieves an animal identification system based on production rules. The system is developed using Prolog and the Python technology stack, and users can use the system by running the main.py file. The technical principle of the system is mainly based on the concept of production system, including knowledge base design, system design, system reasoning and system display. In terms of knowledge base design, the production rules describe the characteristics and taxonomic information of the animal and provide basic knowledge for the reasoning process of the system.  The program takes the animal features entered by the user as facts, matches them with the rules in the rule base, and generates inferred results based on the matching results. The system realizes the process of logical reasoning by matching rules one by one and updating the fact base. In the part of system presentation, the operation process of inference matching program is analyzed in detail, and the animal recognition function of the system is shown. Users can input the feature information of animals, and the system will generate inference results according to the matching rules and facts to realize the classification and recognition of animals. 

##Production Rules
R01: if 动物有毛发 and 动物有奶 then 动物是哺乳动物
R02: if 动物有羽毛 and 会生蛋 then 动物是鸟
R03: if 动物吃肉 then 动物是食肉动物
R04: if 动物有锋利牙齿 and 有爪 and 眼向前方 then 动物是食肉动物
R05: if 动物是哺乳动物 and 有蹄 then 动物是有蹄类动物
R06: if 动物是哺乳动物 and 反刍 then 动物是有蹄类动物
R07: if 动物是哺乳动物 and 是食肉动物 and 有黄褐色皮毛 and 有暗斑点 then 动物是豹
R08: if 计动物是哺乳动物 and 是食肉动物 and 有黄褐色皮毛 and 有黑色条纹 then 动物是虎
R09: if 动物是有蹄类动物 and 有长脖子 and 有长腿 and 有暗斑点then 动物是长颈鹿
R10: if 动物是有蹄类动物 and 有黑色条纹 then 动物是斑马 
R11: if 动物是鸟 and 不会飞 and 有长脖子 and 有长腿 and 有黑白二色 then 动物是鸵鸟
R12: if 动物是鸟 and 不会飞 and 会游泳 and 有黑白二色 then 动物是企鹅
R13: if 动物是鸟 and 善飞 then 动物是信天翁
R14: if 动物是哺乳动物 and 有尾巴 then 动物是哺乳动物中的有尾类动物
R15: if 动物有鳞片 then 动物是爬行动物


##Running the demo
In this project, I utilized "prolog" language to realize production rules. So you may have to prepare the SWI-Prolog environment before using it. Follow this introduction:<https://blog.csdn.net/xilimn/article/details/104002770>

After the preparation, you can download the source code. The file "animal_rec_system.pl" includes the production rules needed for the system to recognize the animal. The file "main.py" provides an interface for users to input animals' features, carry out the inferrence and obtain the results.
