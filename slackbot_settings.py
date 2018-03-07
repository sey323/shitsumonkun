# coding: utf-8
import json
'''
jsonファイルの読み込み用
'''
def load_json( _filename):
        f = open( _filename )
        json_data = json.load( f )

        f.close()
        return json_data


json = load_json( 'config.json' )
# botアカウントのトークンを指定
API_TOKEN = json['slack_bot']['api_key']
# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "なんだこいつ"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
