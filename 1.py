from operator import indexOf


def find_item_fun (list ,item ) :
    for i in list :
        if i is item :
            return list.index(i)

    else :
        return None





items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_fun(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
