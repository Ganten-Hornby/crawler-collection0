from urllib.request import urlretrieve
import os


def download_image(url, name='image', file_path=r'C:\Users\11195\Desktop'):
    try:
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        file_suffix = os.path.splitext(url)[1]
        urlretrieve(url, filename=f'{file_path}\\{name}{file_suffix}')
    except:
        print(f'Download_image{name:^8}fail')


if __name__ == '__main__':
    url = 'http://xuanke.tongji.edu.cn/images/share/title_TJ.gif'
    download_image(url, name='同济大学教务系统')
