#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys ,os
sys.path.append( os.pardir )
import requests
import json
import types

class DdialogueDriver:

    def __init__( self , _filename = 'config.json' ):
        self._data = None
        self._token = None

        #エンドポイントの設定
        self._endpoint_qa = 'https://api.apigw.smt.docomo.ne.jp/knowledgeQA/v1/ask'

        self._header = {'Content-type': 'application/json'}

        self._response = ''
        self.get_api_param( _filename )

        
    '''
    config.jsonからAPIキーの取得
    '''
    def get_api_param( self  , _filename ):
        json = self.load_json( _filename )
        data = json["docomo"]
        self._token = data['api_key']

    '''
    jsonファイルの読み込み
    '''
    def load_json( self ,  _filename):
            f = open( _filename )
            json_data = json.load( f )

            f.close()
            return json_data

    def listen( self , talk ):
        self._response = ''
        self.listen_qa(talk)
        # Q&Aのリクエストを受け取ったとき
        if self._data['message']['textForDisplay'] not in 'わかりませんでした。':
            self._response += str(self._data['message']['textForDisplay'])
            if self._data['answers'] is not None:
                for answer in self._data['answers']:
                    self._response += '\n'
                    self._response += 'rank:' + answer['rank'] + answer['answerText'] + answer['linkText'] + '\n URL: ' + answer['linkUrl']
        else:
            self._response = self._data['message']['textForDisplay']

    # Q&AにAPIリクエストを飛ばす
    def listen_qa( self , talk ):
        params = {'q': talk , 'APIKEY': self._token }
        #送信
        r = requests.get(self._endpoint_qa , params )
        self._data = r.json()

    def speak( self ):
        return self._response

if __name__ == '__main__':
    dd = DdialogueDriver()


    #1回目の会話の入力
    utt_content = input('>>')

    dd.listen(utt_content)
    #表示
    print("response: %s" %(dd.speak()))

    #2回目以降の会話(Ctrl+Cで終了)
    while True:
        utt_content = input('>>')
        dd.listen(utt_content)

        print("response: %s" %(dd.speak()))
