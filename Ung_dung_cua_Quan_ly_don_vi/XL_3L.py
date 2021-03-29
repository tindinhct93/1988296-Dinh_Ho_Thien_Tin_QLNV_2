import json
from pathlib import Path
from datetime import datetime
import os

#Xử lý lưu trữ
Thu_muc_du_lieu = Path("../Du_lieu")
Thu_muc_nhan_vien = Thu_muc_du_lieu/"Nhan_vien"
Thu_muc_cong_ty = Thu_muc_du_lieu/"Cong_ty"

Thu_muc_du_lieu = "../Du_lieu"
Thu_muc_Quan_ly_don_vi = Thu_muc_du_lieu + "/Quan_ly_Don_vi"
Thu_muc_nhan_vien = Thu_muc_du_lieu + "/Nhan_vien"
Thu_muc_cong_ty = Thu_muc_du_lieu + "/Cong_ty"

def Doc_Khung_HTML():
    Duong_dan = Thu_muc_du_lieu+"/HTML/Khung.html"
    with open(Duong_dan,"r+",encoding="utf-8") as f:
        chuoi_HTML = f.read()
    return chuoi_HTML

def Doc_Cong_ty():
    Duong_dan = Thu_muc_cong_ty+ "/Cong_ty.json"
    with open(Duong_dan,"r+",encoding="utf-8") as f:
        chuoiSON = f.read()
    cong_ty = json.loads(chuoiSON)
    return cong_ty

def Doc_Danh_sach_Quan_ly_don_vi():
    Danh_sach = []
    Danh_sach_tep = os.listdir(Thu_muc_Quan_ly_don_vi)
    for tep in Danh_sach_tep:
        Duong_dan = Thu_muc_Quan_ly_don_vi + "/" + tep
        with open(Duong_dan,"r+",encoding="utf-8") as f:
            chuoiSON = f.read()
        Quan_ly_don_vi = json.loads(chuoiSON)
        Danh_sach.append(Quan_ly_don_vi)
    return Danh_sach


def Doc_Danh_sach_Nhan_Vien(Quan_ly_Don_vi,chuoi_tra_cuu = ""):
    Danh_sach = []
    Danh_sach_tep = os.listdir(Thu_muc_nhan_vien)
    for tep in Danh_sach_tep:
        Duong_dan = Thu_muc_nhan_vien + "/" + tep
        with open(Duong_dan,"r+",encoding="utf-8") as f:
            chuoiSON = f.read()
        Nhan_vien = json.loads(chuoiSON)
        if Nhan_vien['Don_vi']['Ma_so'] == Quan_ly_Don_vi['Don_vi']['Ma_so'] and chuoi_tra_cuu in Nhan_vien['Ho_ten']:
            Danh_sach.append(Nhan_vien) 
    return Danh_sach


def Ghi_nhan_vien(Nhan_vien):
    Duong_dan = Thu_muc_nhan_vien + "/" + Nhan_vien['Ma_so'] +".json"
    chuojSON = json.dumps(Nhan_vien)
    with open(Duong_dan,"r+",encoding="utf-8") as f:
        f.write(chuojSON)

def Ghi_Hinh_Nhan_vien(Nhan_vien,Hinh):
    Duong_dan = f"""../Media/{Nhan_vien['Ma_so']}.png"""
    Hinh.save(Duong_dan)

def Tao_chuoi_HTML_form_dang_nhap(Thong_bao, Ten_dang_nhap= "QLDV_1",Mat_khau="QLDV_1"):
    chuoi_HTML = f"""<form action="/Dang_nhap" method="post">
              <label for="fname">Tên nhân viên</label><br>
              <input type="text" id="fname" name="Th_Ten_dang_nhap" value="{Ten_dang_nhap}"><br>
              <label for="lname">Mật Khẩu</label><br>
              <input type="password" id="lname" name="Th_Mat_khau" value="{Mat_khau}"><br><br>
              <div style="color:red">{Thong_bao}</div>
              <input type="submit" value="Đăng nhập">
              </form>"""
    return chuoi_HTML

def Tao_page_HTML_Giao_dien_Khoi_dong(Dang_nhap_that_bai = False):
    KhungHTML = Doc_Khung_HTML()
    Thongbao = ''
    if Dang_nhap_that_bai:
        Thongbao = "Đăng nhập thất bại, vui lòng thử lại"
    chuoiHTML = Tao_chuoi_HTML_form_dang_nhap(Thongbao)
    Chuoi_HTML = KhungHTML.replace("Chuoi_HTML",chuoiHTML)
    return Chuoi_HTML

def Tao_page_HTML_Giao_dien_Quan_ly_don_vi(Quan_ly_Don_vi, Danh_sach_nhan_vien=[]):
    if Danh_sach_nhan_vien == []:
        Danh_sach_nhan_vien = Quan_ly_Don_vi['Danh_sach_nhan_vien']
    KhungHTML = Doc_Khung_HTML()
    chuoiHTML = Tao_chuoi_HTML_Menu_Chinh() + Tao_chuoi_HTML_Danh_sach_nhan_vien(Danh_sach_nhan_vien)
    Chuoi_HTML = KhungHTML.replace("Chuoi_HTML",chuoiHTML)
    return Chuoi_HTML

def Tao_chuoi_HTML_Danh_sach_nhan_vien(Danh_sach_nhan_vien):
    chuoi_HTML = ""
    chuoiHTML_traCuu = f'''`<form action="/Tra_cuu" method="get">
                <input type="text" name="Chuoi_tra_cuu" />
                <input type="submit" value="Tra cứu">
                {len(Danh_sach_nhan_vien)}
        </form>'''
    chuoi_HTML += chuoiHTML_traCuu
    for nhan_vien in Danh_sach_nhan_vien:
        chuoi_HTML += Tao_chuoi_HTML_Giao_dien_Nhan_vien(nhan_vien)
    return chuoi_HTML

def Tao_chuoi_HTML_Giao_dien_Nhan_vien(Nhan_vien):
    chuoiHTML = Tao_chuoi_HTML_Thuc_don_Nhan_vien(Nhan_vien) + Tao_chuoi_HTML_Thong_tin_Nhan_vien(Nhan_vien)
    return chuoiHTML

def Tao_chuoi_HTML_Menu_Chinh():
    chuoi_thuc_don = f'''
            <div class="row">
            <a class="btn btn-danger" href="/Nhan_vien" style="margin:5px">Quản lý nhân viên</a>
            <a class="btn btn-danger" href="/Don_xin_nghi_phep" style="margin:5px">Quản lý đơn xin nghỉ phép</a>
            </div>'''
    return chuoi_thuc_don

def Tao_chuoi_HTML_Thong_tin_Nhan_vien(Nhan_vien):
    chuoi_Hinh = f'''<img src="/Media/{Nhan_vien['Ma_so']}.png" style="width: 60px; height: 60px"/>'''
    chuoi_Ngoai_ngu = ""
    for ngoai_ngu in Nhan_vien['Danh_sach_Ngoai_ngu']:
        chuoi_Ngoai_ngu += ngoai_ngu['Ten'] + " "
    chuoi_Thong_tin =f'''<div class= "btn" style="text-align:left">
            {Nhan_vien['Ho_ten']} {Nhan_vien['CMND']} <br/>
             {Nhan_vien['Don_vi']['Ten']} - {Nhan_vien['Don_vi']['Chi_nhanh']['Ten']}      <br/>
             {Nhan_vien['Dien_thoai']} <br/>
             {Nhan_vien['Dia_chi']} <br/>
             {chuoi_Ngoai_ngu}
             </div>'''
    return chuoi_Hinh + chuoi_Thong_tin    

def Tao_chuoi_HTML_Thuc_don_Nhan_vien(Nhan_vien):
    ChuoiHTML = f""" <div class='row'> 
        {Tao_chuoi_HTML_cap_nhat_dien_thoai(Nhan_vien)}
        {Tao_chuoi_HTML_cap_nhat_dia_chi(Nhan_vien)}
        {Tao_chuoi_HTML_cap_nhat_hinh(Nhan_vien)}
        </div>
    """
    return ChuoiHTML

def Tao_chuoi_HTML_cap_nhat_dien_thoai (Nhan_vien):
    chuoi_Click = f'''<div data-toggle="dropdown" class="btn btn-primary">Cập nhật điện thoại</div>'''
    chuoi_Dropdown = f'''<div class="dropdown-menu" style="width:200%">
            <form action="/Cap_nhat_dien_thoai" method="post">
                <input name="Th_Ma_so_nhan_vien" value='{Nhan_vien['Ma_so']}' type ="hidden">
                <input name="Th_Dien_thoai" type="text" required value="{Nhan_vien['Dien_thoai']}" style="width:90%"/>
                <div class="alert">
                    <button class="btn btn-danger" type="submit">Đồng ý</button>                
                </div>
              </form>
            </div>'''
    Chuoi_chuc_nang = f'''<div class ="dropdown btn">{chuoi_Click}{chuoi_Dropdown}</div>'''
    return Chuoi_chuc_nang

def Tao_chuoi_HTML_cap_nhat_dia_chi (Nhan_vien):
    chuoi_Click = f'''<div data-toggle="dropdown" class="btn btn-primary">Cập nhật địa chỉ</div>'''
    chuoi_Dropdown = f'''<div class="dropdown-menu" style="width:200%">
            <form action="/Cap_nhat_dia_chi" method="post">
                <input name="Th_Ma_so_nhan_vien" value={Nhan_vien['Ma_so']} type ="hidden">
                <textarea name="Th_Dia_chi" required cols="25" rows="3" style="width:90%">{Nhan_vien['Dia_chi']}</textarea>
                <div class="alert">
                    <button class="btn btn-danger" type="submit">Đồng ý</button>                
                </div>
              </form>
            </div>'''
    Chuoi_chuc_nang = f'''<div class ="dropdown btn">{chuoi_Click}{chuoi_Dropdown}</div>'''
    return Chuoi_chuc_nang 

def Tao_chuoi_HTML_cap_nhat_hinh (Nhan_vien):
    chuoi_Click = f'''<div data-toggle="dropdown" class="btn btn-primary">Cập nhật hình</div>'''
    chuoi_Dropdown = f'''<div class="dropdown-menu" style="width:200%">
            <form action="/Cap_nhat_hinh" method="post" enctype="multipart/form-data">
                <div class="alert">
                    Cập nhật hình cho nhân viên {Nhan_vien['Ho_ten']}                
                </div>
                 <input name="Th_Ma_so_nhan_vien" value="{Nhan_vien['Ma_so']}" type ="hidden"/>
                 <input type="file" name="Th_Hinh" accept="image/png"/>
                <div class="alert">
                    <button class="btn btn-danger" type="submit">Đồng ý</button>                
                </div>
              </form>
            </div>'''
    Chuoi_chuc_nang = f'''<div class ="dropdown btn">{chuoi_Click}{chuoi_Dropdown}</div>'''
    return Chuoi_chuc_nang 