from datetime import datetime, timedelta
import os
import cv2

# 画像ファイルの保存パスの作成
now = datetime.now()
save_path = './images/' + now.strftime('%Y%m%d-%H%M%S') + '/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 動画ファイルの保存パスの作成
# save_path = './videos/'
# if not os.path.exists(save_path):
#     os.makedirs(save_path)
# 動画ファイルのファイル名の指定
# now = datetime.now()
# v_file_name = save_path + now.strftime("%Y%m%d-%H%M%S") + '.mp4'

def main():
    cap = cv2.VideoCapture(0)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # print('fps: ' + str(fps))
    # print('width: ' + str(w))
    # print('height: ' + str(h))

    # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')   # 動画保存時のfourcc設定（mp4用）
    # video = cv2.VideoWriter(v_file_name, fourcc, fps, (w, h))   # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

    save_interval = 0   # フレームの保存間隔（1〜60[秒]の整数のうち60の約数）
    while True:
        input_num = input('フレームの保存間隔を入力（1〜60[秒]の整数のうち60の約数）: ')
        if input_num in ['1', '2', '3', '4', '5', '6', '10', '12', '15', '20', '30', '60']:
            save_interval = int(input_num)
            break
    
    num = 0   # 保存したフレームの番号
    last = datetime.now() - timedelta(seconds=1)   # 1つ前に保存した時刻
    
    # 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
    while True:
        now = datetime.now()

        ret, frame = cap.read()   # フレームを取得
        frame = cv2.resize(frame, (600, 400))
        frame = cv2.putText(frame, now.strftime("%Y/%m/%d %H:%M:%S"), (0,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)   # フレームに日時を表示
        cv2.imshow('video_capturer (push "Q" to end capturing)', frame)   # フレームを画面に表示

        # save_interval 秒ごとにフレームを保存
        if int(now.strftime("%S")) % save_interval == 0 and now.strftime("%S") != last.strftime("%S"):
            last = now
            num += 1
            i_file_name = save_path + str(num) + "_" + now.strftime("%Y%m%d-%H%M%S") + ".jpg"
            cv2.imwrite(i_file_name, frame)   # フレームを画像ファイルとして保存
            # video.write(frame)   # 動画を1フレームずつ保存
    
        # キー操作があればwhileループを抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # 撮影用オブジェクトとウィンドウの解放
    cap.release()
    cv2.destroyAllWindows()

main()