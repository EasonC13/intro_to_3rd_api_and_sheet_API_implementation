evaluator_script = '''from io import StringIO 
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def check_get_new_york_time():
    ny_time = new_york_time

    ans = requests.get("http://worldtimeapi.org/api/timezone/America/New_York").json()

    if ny_time['timezone'] == ans['timezone']:
        print("恭喜你完成本單元的測試！")
    else:
        print("測試失敗，請檢查變數 new_york_time 並且再試一次")
        print("你可以執行 hint 或 answer 來取得提示")

def hint_get_new_york_time():
    print("""倫敦（London）是在歐洲（Europe），紐約（New_York）是在美洲（America）\n想想看 "http://worldtimeapi.org/api/timezone/Europe/London" 這個網址，要怎麼改才會變成在美洲的紐約呢？""")

def answer_get_new_york_time():
    print("""#最佳做法
def get_new_york_time():
    return requests.get("http://worldtimeapi.org/api/timezone/America/New_York").json()""")

def hint_check_account_is_finish():
    print("""'email in df["你的信箱"]' 無法正確得到結果，因為 df["你的信箱"] 是 Series 資料型別，因此要轉換為 list 才能進行檢查""")
    
def answer_check_account_is_finish():
    print("""def check_account_is_finish(email = 'example@gmail.com'):
    return email in list(df['你的信箱'])""")
    
def check_email_is_finish():
    passTest = True
    for email in list(df['你的信箱']):
        if email_is_finish(email) == False:
            passTest = False
    if passTest:
        print("恭喜你完成本單元的測試！")
    else:
        print("""測試失敗，請編輯函式 email_is_finish 並且再試一次 \n你可以執行 hint 或 answer 來取得提示""")

def check_creat_new_sheet():
    if type(my_sheet) == gspread.models.Spreadsheet:
        print("恭喜你完成本單元的測試！")
    else:
        print("""測試失敗，請將新建立的 sheet 放在變數 `my_sheet` 並且再試一次\n你可以執行 hint 或 answer 來取得提示""")

def hint_creat_new_sheet():
    print("""1. 請你於 scope 處加入 'https://www.googleapis.com/auth/drive' ，這樣你的 API 才能操作 Google Drive
2. 請查看錯誤訊息，他是不是有要請你做什麼呢？""")

def answer_create_new_sheet():
    print("""#範例程式碼
# 這次範圍除了 Sheet，還需要有 Google Drive
gss_scopes = ['https://spreadsheets.google.com/feeds']
gss_scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)

# 建立新的 Sheet
my_sheet = gss_client.create('A_new_spreadsheet')""")

def check_sheet_url():
    ans = f"https://docs.google.com/spreadsheets/d/{my_sheet.id}"
    if my_sheet_url[:len(ans)] == ans:
        print("恭喜你完成本單元的測試！")
    else:
        print("""測試失敗，請將在瀏覽器打開 my_sheet 的連結網址貼到變數 `my_sheet_url` \n你可以執行 hint 或 answer 來取得提示""")

def hint_sheet_url():
    print("請你檢查既有的 Google Sheet 他們的網址格式，my_sheet 的 id 能夠被放在哪裡呢？")

def answer_sheet_url():
    print(f"""# 解法一
# 因為 my_sheet.id 為 {my_sheet.id}
# 又因為 Google Sheet 網址格式為 {'https://docs.google.com/spreadsheets/d/{my_sheet.id}'}
# 所以你可以透過以下網址打開 my_sheet https://docs.google.com/spreadsheets/d/{my_sheet.id}

my_sheet_url = "https://docs.google.com/spreadsheets/d/{my_sheet.id}" 

# 解法二，如果你有在 my_sheet 後面按下 TAB 看他有提供哪些接口的話
my_sheet_url = my_sheet.url""")

def check_sheet_share():
    print("此題無法進行檢查，如果你無法透過連結正確檢視，就代表你的分享權限設定錯誤囉！")

def hint_sheet_share():
    print("請去 gspread 的官方文件左上角 `search docs` 搜尋 `share` 看看搜尋結果，然後試著改寫範例吧！")

def answer_sheet_share():
    print("""# 指定 email 可寫入
my_sheet.share("yourEmail@gmail.com", perm_type='user', role='writer')

# 所有人都可讀取
my_sheet.share(None, perm_type='anyone', role='reader')""")

def init_with_data(worksheet):
    # 寫入整個 DF
    df = get_titanic_data()
    worksheet.clear()
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    
def get_titanic_data():
    df = pd.DataFrame(
        gss_client.open_by_key(
            "1S1sKUrkkk9xtneZGUf9eWn562j5q_bqh9KmV7Rjc5Go"
        ).worksheets()[0].get_all_records())
    return df

import numpy as np
import pandas as pd
def check_titanic_df():
    if titanic_df.equals(pd.DataFrame(worksheet.get_all_records())):
        print("恭喜你完成本單元的測試！")
    else:
        print("""測試失敗，讀取整個 worksheet 為 Pandas DataFrame，並寫入變數 titanic_df \n你可以執行 hint 或 answer 來取得提示""")
        
    
    
def hint_titanic_df():
    print("試著翻翻看 gspread 官方文件，使用搜尋功能找你要的資訊，你能找到 pandas 相關的資訊嗎？")

def answer_titanic_df():
    print("""# 在官方文件搜尋 Pandas 後的第一個結果，即可看到範例
titanic_df = pd.DataFrame(worksheet.get_all_records())""")

def check_get_answers_df():
    if answers_df.equals(pd.DataFrame(
        gss_client.open_by_key(
            "1JvnRvPy55nOMYfdFdPveyFmpsuHYm4Q2aMg4TtoGM6I"
        ).worksheets()[0].get_all_records())
        ):
        print("恭喜你完成本單元的測試！")
    else:
        print("""測試失敗，讀取整個 worksheet 為 Pandas DataFrame，並寫入變數 answers_df \n你可以執行 hint 或 answer 來取得提示""")

def hint_get_answers_df():
    print("請參考第三單元，要如何讀取 Google Sheet 呢？")
    
def answer_get_answers_df():
    print("""# 方法一
answers_df = gss_client.open_by_key("1JvnRvPy55nOMYfdFdPveyFmpsuHYm4Q2aMg4TtoGM6I").worksheets()[0]
answers_df = pd.DataFrame(answers_df.get_all_records())

# 方法二
answers_df = gss_client.open_by_url("https://docs.google.com/spreadsheets/d/1JvnRvPy55nOMYfdFdPveyFmpsuHYm4Q2aMg4TtoGM6I").worksheets()[0]
answers_df = pd.DataFrame(answers_df.get_all_records())""")

def check_write_my_sheet():
    df = pd.DataFrame(worksheet.get_all_records())

    df = df[:len(answers_df)]

    df = df.drop(columns= set(df.columns).difference(set(answers_df.columns)))

    if df.equals(answers_df):
        print("恭喜你完成本單元的測試！打開瀏覽器去看看 Google Sheet 的情況吧！")
    else:
        print("""測試失敗，請把測驗結果作為 Pandas DataFrame 寫入 My Sheet 的 work_sheet 部分 \n你可以執行 hint 或 answer 來取得提示""")


def hint_write_my_sheet():
    print("請試著尋找官方文件，試試看搜尋 pandas 會有什麼結果？")
    
def answer_write_my_sheet():
    print("worksheet.update([answers_df.columns.values.tolist()] + answers_df.values.tolist())")

def check_replace_sheet():
    df = pd.DataFrame(worksheet.get_all_records())
    if df.equals(answers_df):
        print("恭喜你完成本單元的測試！")
    else:
        print("""測試失敗，其他不是 answer_df 的內容都要被排除喔～\n你可以執行 hint 或 answer 來取得提示""")


def hint_replace_sheet():
    print("試試看先清空 worksheet 再把 answer_df 寫入。")


def answer_replace_sheet():
    print("""# 先清空 worksheet 再把 answer_df 寫入
worksheet.clear()
worksheet.update([answers_df.columns.values.tolist()] + answers_df.values.tolist())""")

def check_titanic_data_load():
    worksheets = my_sheet.worksheets()

    titanic_sheet = list(filter(lambda x: x.title == 'Titanic', worksheets))[0]

    if pd.DataFrame(titanic_sheet.get_all_records()).equals(get_titanic_data()):
        print("恭喜你完成本實作！")
    else:
        print("檢查不通過，請將 titanic_df 寫進去剛剛建立的 Title 名叫 Titanic 的 WorkSheet")
        
def hint_titanic_data_load():
    print("查看 gspread 的 document，如何實作 Creating a Worksheet？")
    
def answer_titanic_data_load():
    print("""titanic_sheet = list(filter(lambda x: x.title == 'Titanic', worksheets))[0]
titanic_sheet.update([titanic_df.columns.values.tolist()] + titanic_df.values.tolist())""")

def check_titanic_create_sheet():
    worksheets = my_sheet.worksheets()
    
    if len(list(filter(lambda x: x.title == 'Titanic', worksheets))):
        print("恭喜你完成本實作！")
    else:
        print("檢查不通過，請建立一個 Sheet 將其 title 設為 Titanic")
        
def hint_titanic_create_sheet():
    print("查看 gspread 的 document，如何實作 Creating a Worksheet？")
    
def answer_titanic_create_sheet():
    print("""my_sheet.add_worksheet(title="Titanic", rows=titanic_df.shape[0], cols=titanic_df.shape[1])""")

def check_etl():
    worksheets = my_sheet.worksheets()
    titanic_sheet = list(filter(lambda x: x.title == 'Titanic', worksheets))[0]
    if (np.array(titanic_df.Name.apply(lambda x: '✞' in x)) != np.array(titanic_df.Survived == 0)).sum() == 0:
        print("恭喜你通過！")
    else:
        print("檢查失敗，如果資料已經亂掉，可以試著重新執行前一段落「將 titanic_df 寫進去」的內容")
        
def hint_etl():
    print("""這題屬於 Pandas 進階功能操作。\n提示：你可以把兩個資料型態為 `str` 的 `pandas.core.series.Series` 相加在一起""")
    
def answer_etl():
    print("""# 範例程式碼
cross_symbol = '✞'
titanic_sheet = list(filter(lambda x: x.title == 'Titanic', worksheets))[0]
titanic_df = pd.DataFrame(titanic_sheet.get_all_records())
need_cross = titanic_df['Survived'].apply(lambda x: cross_symbol if x == 0 else '')
titanic_df.Name = need_cross + titanic_df.Name

titanic_sheet.clear()
titanic_sheet.update([titanic_df.columns.values.tolist()] + titanic_df.values.tolist())""")'''
