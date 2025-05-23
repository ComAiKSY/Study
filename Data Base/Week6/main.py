import pymysql
import tkinter
import tkinter.messagebox as mbox

# INSERT 함수
def insertData():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='market_db', charset='utf8')
    cursor = conn.cursor()

    data1 = edt1.get()
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()
    data5 = edt5.get()
    data6 = edt6.get()
    data7 = edt7.get()
    data8 = edt8.get()

    sql = """
        INSERT INTO member (mem_id, mem_name, mem_number, addr, phone1, phone2, height, debut_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        data1,
        data2 if data2 else None,
        data3 if data3 else None,
        data4 if data4 else None,
        data5 if data5 else None,
        data6 if data6 else None,
        data7 if data7 else None,
        data8 if data8 else None
    )

    cursor.execute(sql, data)
    conn.commit()
    conn.close()

    mbox.showinfo("성공", "1건 등록 완료")
    selectData()

# SELECT 함수
def selectData():
    strDatas = [[] for _ in range(8)]  # 8개 컬럼

    headers = ["ID", "이름", "인원수", "주소", "전화1", "전화2", "키", "데뷔일"]
    for i in range(8):
        strDatas[i].append(headers[i])
        strDatas[i].append("--------------")

    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='market_db', charset='utf8')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            mem_id,
            IFNULL(mem_name, '-'),
            IFNULL(mem_number, '-'),
            IFNULL(addr, '-'),
            IFNULL(phone1, '-'),
            IFNULL(phone2, '-'),
            IFNULL(height, '-'),
            IFNULL(debut_date, '-')
        FROM member
        ORDER BY mem_id
    """)

    while True:
        row = cursor.fetchone()
        if row is None:
            break
        for i in range(8):
            strDatas[i].append(str(row[i]))

    for listbox in listBoxes:
        listbox.delete(0, tkinter.END)
    for items in zip(*strDatas):
        for i in range(8):
            listBoxes[i].insert(tkinter.END, items[i])

    conn.close()

# DELETE 함수
def deleteData():
    uid = edt1.get()
    if uid == "":
        mbox.showwarning("경고", "삭제할 ID를 입력하세요")
        return

    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='market_db', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM member WHERE mem_id = %s"
    result = cursor.execute(sql, (uid,))
    conn.commit()
    conn.close()

    if result == 0:
        mbox.showinfo("실패", f"{uid}는 존재하지 않습니다.")
    else:
        mbox.showinfo("성공", f"{uid} 삭제 완료")
        selectData()

# ---------------- GUI ----------------
window = tkinter.Tk()
window.geometry("900x400")
window.title("Member 관리")

# 입력창 프레임
edtFrame = tkinter.Frame(window)
edtFrame.pack()

# 출력창 프레임
listFrame = tkinter.Frame(window)
listFrame.pack(side='bottom', fill='both', expand=1)

# Entry 위젯들
edt1 = tkinter.Entry(edtFrame, width=10); edt1.pack(side='left', padx=5, pady=5)  # mem_id
edt2 = tkinter.Entry(edtFrame, width=10); edt2.pack(side='left', padx=5, pady=5)  # mem_name
edt3 = tkinter.Entry(edtFrame, width=10); edt3.pack(side='left', padx=5, pady=5)  # mem_number
edt4 = tkinter.Entry(edtFrame, width=10); edt4.pack(side='left', padx=5, pady=5)  # addr
edt5 = tkinter.Entry(edtFrame, width=10); edt5.pack(side='left', padx=5, pady=5)  # phone1
edt6 = tkinter.Entry(edtFrame, width=10); edt6.pack(side='left', padx=5, pady=5)  # phone2
edt7 = tkinter.Entry(edtFrame, width=10); edt7.pack(side='left', padx=5, pady=5)  # height
edt8 = tkinter.Entry(edtFrame, width=10); edt8.pack(side='left', padx=5, pady=5)  # debut_date

# 버튼들
btnInsert = tkinter.Button(edtFrame, text="입력", command=insertData)
btnInsert.pack(side='left', padx=10, pady=5)

btnSelect = tkinter.Button(edtFrame, text="조회", command=selectData)
btnSelect.pack(side='left', padx=10, pady=5)

btnDelete = tkinter.Button(edtFrame, text="삭제", command=deleteData)
btnDelete.pack(side='left', padx=10, pady=5)

# 리스트박스 8개
listBoxes = []
for _ in range(8):
    lb = tkinter.Listbox(listFrame, bg='lightyellow')
    lb.pack(side='left', fill='both', expand=1)
    listBoxes.append(lb)

window.mainloop()
