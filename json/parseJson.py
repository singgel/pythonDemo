import json

def main():
    # file 文件类型的对象
    with open(r'/Users/yiche/Downloads/xugm-ozzie.txt', encoding="utf-8") as file:
        print(type(file))
        print(file)

        # 以列表的形式输出文本
        lines = list(file)
        print(lines)

        # 输出文本的每一行
        for eachLine in lines:
            print(eachLine)

        # 这样做的效率低


if __name__ == '__main__':
    main()
