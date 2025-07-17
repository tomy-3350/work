import gspread
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

# Streamlit SecretsからTOML形式で情報を取得
google_cloud_secret = st.secrets["google_cloud"]

# Secretsから必要な情報を構築
service_account_info = {
    "type": google_cloud_secret["type"],
    "project_id": google_cloud_secret["project_id"],
    "private_key_id": google_cloud_secret["private_key_id"],
    "private_key": google_cloud_secret["private_key"],  # 改行が含まれる
    "client_email": google_cloud_secret["client_email"],
    "client_id": google_cloud_secret["client_id"],
    "auth_uri": google_cloud_secret["auth_uri"],
    "token_uri": google_cloud_secret["token_uri"],
    "auth_provider_x509_cert_url": google_cloud_secret["auth_provider_x509_cert_url"],
    "client_x509_cert_url": google_cloud_secret["client_x509_cert_url"],
    "universe_domain": google_cloud_secret["universe_domain"]
}

# サービスアカウント認証情報を`ServiceAccountCredentials`に渡す
creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account_info,
    ["https://spreadsheets.google.com/feeds",
     "https://www.googleapis.com/auth/spreadsheets",
     "https://www.googleapis.com/auth/drive.file",
     "https://www.googleapis.com/auth/drive"])

# gspreadを使ってGoogle Sheets APIに認証
gc = gspread.authorize(creds)

###################################
customer = '選択してください'
new_customer = '選択してください'
genre = '選択してください'
number = ''
time = 0

customer2 = '選択してください'
new_customer2 = '選択してください'
genre2 = '選択してください'
number2 = ''
time2 = 0

customer3 = '選択してください'
new_customer3 = '選択してください'
genre3 = '選択してください'
number3 = ''
time3 = 0

customer4 = '選択してください'
new_customer4 = '選択してください'
genre4 = '選択してください'
number4 = ''
time4 = 0

customer5 = '選択してください'
new_customer5 = '選択してください'
genre5 = '選択してください'
number5 = ''
time5 = 0

#######################################################
# タイトル
st.title('北青 機械課 作業日報')
st.caption("メーカー名、工番、作業内容、時間を入力してください。")
day = st.date_input("日付を選択してください")

# 名前
name = st.selectbox(
    '名前',
    ('選択してください','大地','山岸','坂本','一條','松本','将','出繩'))

# メーカー
if name != '選択してください':
    customer = st.selectbox(
    'メーカー',
    ('選択してください','ジーテクト','ヨロズ','城山','タチバナ','浜岳','三池','東プレ',
     '千代田','武部','インフェック','その他'))
else:
    pass

# 新規メーカー
if customer == 'その他':
    new_customer = st.text_input('メーカー名を入力')
else:
    pass

# 作業区分
if customer != '選択してください':
    genre = st.selectbox(
    '作業内容',
    ('選択してください','新規','改修','その他'))
else:
    pass

# 工番入力
if genre != '選択してください':
    number = st.text_input('工番を入力')
else:
    pass

# 時間
if number != '':
    time = st.number_input('時間を入力')
else:
    pass

###################################
# メーカー2
if time != 0:
    customer2 = st.selectbox(
    'メーカー2',
    ('選択してください', 'ジーテクト', 'ヨロズ', '城山', 'タチバナ', '浜岳', '三池', '東プレ',
     '千代田', '武部', 'インフェック', 'その他'))
else:
    pass

# 新規メーカー2
if customer2 == 'その他':
    new_customer2 = st.text_input('メーカー名を入力')
else:
    pass

# 作業区分2
if customer2 != '選択してください':
    genre2 = st.selectbox(
    '作業内容2',
    ('選択してください','新規','改修','その他'))
else:
    pass

# 工番入力2
if genre2 != '選択してください':
    number2 = st.text_input('工番を入力2')
else:
    pass

# 時間2
if number2 != '':
    time2 = st.number_input('時間を入力2')
else:
    pass

######################################
# メーカー3
if time2 != 0:
    customer3 = st.selectbox(
    'メーカー3',
    ('選択してください', 'ジーテクト', 'ヨロズ', '城山', 'タチバナ', '浜岳', '三池', '東プレ',
    '千代田', '武部', 'インフェック'))
else:
    pass

# 作業区分3
if customer3 != '選択してください':
    genre3 = st.selectbox(
    '作業内容3',
    ('選択してください','新規','改修','その他'))
else:
    pass

# 工番入力3
if genre3 != '選択してください':
    number3 = st.text_input('工番を入力3')
else:
    pass

# 時間3
if number3 != '':
    time3 = st.number_input('時間を入力3')
else:
    pass

###############################
# メーカー4
if time3 != 0:
    customer4 = st.selectbox(
    'メーカー4',
    ('選択してください', 'ジーテクト', 'ヨロズ', '城山', 'タチバナ', '浜岳', '三池', '東プレ',
    '千代田', '武部', 'インフェック'))
else:
    pass

# 作業区分4
if customer4 != '選択してください':
    genre4 = st.selectbox(
    '作業内容4',
    ('選択してください','新規','改修','その他'))
else:
    pass

# 工番入力4
if genre4 != '選択してください':
    number4 = st.text_input('工番を入力4')
else:
    pass

# 時間4
if number4 != '':
    time4 = st.number_input('時間を入力4')
else:
    pass

###########################
# メーカー5
if time4 != 0:
    customer5 = st.selectbox(
    'メーカー5',
    ('選択してください', 'ジーテクト', 'ヨロズ', '城山', 'タチバナ', '浜岳', '三池', '東プレ',
    '千代田', '武部', 'インフェック'))
else:
    pass

# 作業区分5
if customer5 != '選択してください':
    genre5 = st.selectbox(
    '作業内容5',
    ('選択してください','新規','改修','その他'))
else:
    pass

# 工番入力5
if genre5 != '選択してください':
    number5 = st.text_input('工番を入力5')
else:
    pass

# 時間5
if number5 != '':
    time5 = st.number_input('時間を入力5')
else:
    pass

##################
total1 = time
if time != 0:
    st.text('合計' + str(total1) + '時間')

########### シートを開く ##############
sheet = gc.open("python").sheet1

############ ボタン #################
submit_btn = st.button('送信')
if submit_btn:
    st.text('お疲れ様でした！')

if submit_btn and new_customer == '選択してください' and customer2 == '選択してください':
    sheet.append_row([str(day)+name,customer,genre,number,time])
elif submit_btn and new_customer != '選択してください' and customer2 == '選択してください':
    sheet.append_row([str(day)+name, new_customer, genre, number, time])

elif submit_btn and new_customer == '選択してください' and customer2 != '選択してください':
    sheet.append_row([str(day)+name,customer,genre,number,time,customer2,genre2,number2,time2])
elif submit_btn and new_customer != '選択してください' and new_customer2 != '選択してください':
    sheet.append_row([str(day)+name,new_customer,genre,number,time,new_customer2,genre2,number2,time2])

elif submit_btn and new_customer == '選択してください' and customer3 != '選択してください':
    sheet.append_row([str(day)+name,customer,genre,number,time,customer2,genre2,number2,time2,customer3,genre3,number3,time3])
elif submit_btn and new_customer != '選択してください' and new_customer2 != '選択してください' and customer3 != '選択してください':
    sheet.append_row([str(day)+name,new_customer,genre,number,time,new_customer2,genre2,number2,time2,customer3,genre3,number3,time3])

elif submit_btn and new_customer == '選択してください' and customer4 != '選択してください':
    sheet.append_row([str(day)+name,customer,genre,number,time,customer2,genre2,number2,time2,customer3,genre3,number3,time3,customer4,genre4,number4,time4])
elif submit_btn and new_customer != '選択してください' and new_customer2 != '選択してください' and customer4 != '選択してください':
    sheet.append_row([str(day)+name,new_customer,genre,number,time,new_customer2,genre2,number2,time2,customer3,genre3,number3,time3,customer4,genre4,number4,time4])

elif submit_btn and new_customer == '選択してください' and customer5 != '選択してください':
    sheet.append_row([str(day)+name,customer,genre,number,time,customer2,genre2,number2,time2,customer3,genre3,number3,time3,customer4,genre4,number4,time4,customer5,genre5,number5,time5])
elif submit_btn and new_customer != '選択してください' and new_customer2 != '選択してください' and customer5 != '選択してください':
    sheet.append_row([str(day)+name,new_customer,genre,number,time,new_customer2,genre2,number2,time2,customer3,genre3,number3,time3,customer4,genre4,number4,time4,customer5,genre5,number5,time5])