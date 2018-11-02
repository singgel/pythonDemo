import json


def main():
    # file 文件类型的对象
    with open(r'/Users/yiche/Downloads/zhangtianjia.txt', encoding="utf-8") as file:
        print(type(file))
        print(file)

        # 以列表的形式输出文本
        lines = list(file)
        num = 0
        count = 0

        # 输出文本的每一行
        for eachLine in lines:
            num += 1

            # 将 JSON 对象转换为 Python 字典
            data = json.loads(eachLine)

            # 这样做的效率低
            for variable in data['variables']:
                if variable['workflow_variable'] == 'TABLE_NAME':
                    count += 1
                    print(data['name'], "\t", variable['dataset_variable'])

        print("num:", num)
        print("count:", count)


if __name__ == '__main__':
    main()
