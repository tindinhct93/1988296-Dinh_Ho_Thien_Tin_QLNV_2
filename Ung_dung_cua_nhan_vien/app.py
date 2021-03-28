from flask import Flask, request, session
from XL_3L import *
app = Flask(__name__,static_url_path="/Media",static_folder="../Media")
app.secret_key = "super secret key"


@app.route("/",methods=["GET"])
def XL_Khoi_dong():
    chuoi_HTML = Tao_page_HTML_Giao_dien_Khoi_dong()
    return chuoi_HTML

@app.route("/Ho_so",methods=["GET"])
def XL_Tra_cuu_ho_so():
    Nhan_vien = session["Nguoi_dung"]
    chuoi_HTML = Tao_page_HTML_Giao_dien_Nhan_vien(Nhan_vien)
    return chuoi_HTML

@app.route("/Dang_nhap",methods=["POST"])
def XL_Dang_nhap():
    Danh_sach_nhan_vien = Doc_Danh_sach_nhan_vien()
    Ten_dang_nhap = request.form.get('Th_Ten_dang_nhap')
    Mat_khau = request.form.get('Th_Mat_khau')
    Danh_sach = [Nhan_vien for Nhan_vien in Danh_sach_nhan_vien if Nhan_vien['Ten_Dang_nhap']== Ten_dang_nhap and Nhan_vien["Mat_khau"] == Mat_khau]
    Hop_le = any(Danh_sach)
    if Hop_le:
        Nhan_vien = Danh_sach[0]
        session["Nguoi_dung"] = Nhan_vien
        chuoiHTML = Tao_page_HTML_Giao_dien_Nhan_vien(Nhan_vien)
        return chuoiHTML
    chuoiHTML = Tao_page_HTML_Giao_dien_Khoi_dong(True)
    return chuoiHTML

