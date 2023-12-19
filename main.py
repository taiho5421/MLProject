import yaml
import os


class Main(object):
    def __init__(self):
        super(Main, self).__init__()

    def run(self, file_path: str):
        try:
            file_list = os.listdir(file_path)
            if list(filter(lambda x: 'main.py' in x, file_list)).__len__():
                print('hello world')
            else:
                raise Exception('找不到 main.py 文件')
        except FileNotFoundError as e:
            print(f'[錯誤][{e.__class__.__name__}]: {e} -> 第 {e.__traceback__.tb_lineno} 行')
            print(f'[文件路徑]: {e.__traceback__.tb_frame.f_code.co_filename}')
        except Exception as e:
            print(f'[錯誤][{e.__class__.__name__}]: {e} -> 第 {e.__traceback__.tb_lineno} 行')
            print(f'[文件路徑]: {e.__traceback__.tb_frame.f_code.co_filename}')


if __name__ == '__main__':
    main = Main()
    main.run('DepartureOfStaff/')
