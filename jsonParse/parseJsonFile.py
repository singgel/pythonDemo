# -*- coding:utf-8 -*-

__author__ = 'hekuangsheng'

import json

if __name__ == "__main__":
    with open('/Users/yiche/Downloads/hue-documents-2018-11-02-(355).json', 'r') as f:
        data = json.load(f)

        num = 0
        count = 0
        for item in data:
            num += 1

            dic = json.loads(item['fields']['data'])
            if 'variables' in dic:
                count += 1
                flag = True;
                for variable in dic['variables']:
                    try:
                        if 'input_path' == variable['workflow_variable']:
                            flag = False;
                            print(item['fields']['name'].strip(), "\t", variable['dataset_variable'].strip(), "\t",
                                  variable['dataset_variable'].split('/')[3].strip(), "\t",
                                  variable['dataset_variable'].split('/')[4].strip())
                            continue
                    except:
                        print(item['fields']['name'].strip(), "***************", variable)
                if flag:
                    print(item['fields']['name'].strip())

            else:
                print(item['fields']['name'].strip())

    print("num:", num)
    print("count:", count)
