% 事实
start:-
        write('请告诉我关于要查询的动物的特征:'), nl,
        collect_features,
        end.

collect_features :-
        read(Feature),
        (Feature = 'NA' ->
                animal_rec(X)
        ;
                add_feature(Feature),
                collect_features
        ).

end:-
        nl,nl,nl,
        sleep(0.7),
        write('*****************************************************************'),nl,
        sleep(0.4),
        write('################||| THANK YOU FOR USE ME |||#####################'),nl,
        sleep(0.4),
        write('*****************************************************************'),halt.

:- dynamic(has_feature/1).

add_feature(Feature) :-
        assertz(has_feature(Feature)).
add_class(Class) :-
        assertz(animal_class(Class)).
add_rec(Rec) :-
        assertz(animal_rec(Rec)).

%R1
animal_class(Mammal):-
        has_feature(有毛发),
        has_feature(有奶).
%R2
animal_class(Carnivore):-
        has_feature(吃肉);
        (has_feature(有锋利牙齿),
        has_feature(有爪),
        has_feature(眼向前方)).
%R3
animal_class(Bird):-
        has_feature(有羽毛),
        has_feature(会生蛋).
%R4
animal_class(Ungulates):-
        (has_feature(有毛发),
        has_feature(有奶),
        has_feature(有蹄));
        (has_feature(有毛发),
        has_feature(有奶),
        has_feature(反刍)).
%R5
animal_rec(Tail):-
        has_feature(有尾巴),
        animal_class(Mammal),
        write('这个动物是有尾类动物'), nl.
%R6
animal_rec(Leopard):-
        has_feature(有黄褐色皮毛),
        has_feature(有暗斑点),
        has_feature(有黑色条纹),
        animal_class(Carnivore),
        animal_class(Mammal),
        write('这个动物是豹.'), nl.
%R7
animal_rec(Tiger):-
        has_feature(有黄褐色皮毛),
        has_feature(有黑色条纹),
        animal_class(Mammal),
        animal_class(Carnivore),
        write('这个动物是虎'), nl.
%R8
animal_rec(Reptile):-
        has_feature(有鳞片),
        write('这个动物是爬行类动物'), nl.
%R9
animal_rec(Giraffe):-
        has_feature(有黑色条纹),
        animal_class(Ungulates),
        write('这个动物是长颈鹿'), nl.
%R10
animal_rec(Ostrich):-
        has_feature(有长脖子),
        has_feature(有长腿),
        has_feature(有黑白两色),
        has_feature(不会飞),
        animal_class(Bird),
        write('这个动物是鸵鸟'), nl.
%R11
animal_rec(Penguin):-
        has_feature(会游泳),
        has_feature(有黑白两色),
        has_feature(不会飞),
        animal_class(Bird),
        write('这个动物是企鹅'), nl.
%R12
animal_rec(Albatross):-
        has_feature(善飞),
        animal_class(Bird),
        write('这个动物是信天翁.'), nl.