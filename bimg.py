from icrawler.builtin import BingImageCrawler
import subprocess
from icrawler.builtin import BingImageCrawler
import img2pdf
import os
import re
from PIL import Image
from pathlib import Path
import shutil
def main():
    QUERY= input('キーワード＞＞')  
    QUERY_= QUERY.replace(" ", "_")
#    SAVE_DIR = input('保存フォルダ名（絶対パス）もしくはBingImgの下：>>')
    SAVE_DIR = r'D://03c_BingImg//temp'
    if os.path.exists(SAVE_DIR):
        backup_path = SAVE_DIR + "_bk"
        os.rename(SAVE_DIR, backup_path)
        print(f"既存のフォルダをバックアップしました: {backup_path}")
    os.mkdir(SAVE_DIR)
    PdfName=SAVE_DIR+QUERY_+'.pdf'
    if ':' not in SAVE_DIR:
        SAVE_DIR=r'D://03c_BingImg//'+SAVE_DIR
    bing_crawler = BingImageCrawler(
        downloader_threads=4,
        storage={'root_dir': SAVE＿DIR})
    bing_crawler.crawl(
        keyword=QUERY,
        max_num=1000)
    img_Folder = SAVE_DIR
    if(img_Folder[-1:]!="\\"):
        img_Folder=img_Folder + '\\'
    folder_name=img_Folder.split('\\')[-2]
    print(folder_name)
    base_Image = img_Folder
    path = Path(base_Image)
    Create_pdf=path.parent
    images = sorted([str(p) for p in path.glob('**/*') if re.search('/*\.(jpg|jpeg|png)', str(p), re.IGNORECASE)])
#    folder_name_pdf=folder_name+'.pdf'
#    PdfName = os.path.join(Create_pdf, folder_name_pdf)
    with open(PdfName , "wb") as f:
        f.write(img2pdf.convert(images))
    print(Create_pdf)
    shutil.rmtree(SAVE_DIR)
if __name__ == "__main__":
    main()