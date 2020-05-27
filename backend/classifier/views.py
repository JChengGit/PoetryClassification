from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins, generics, status
from gensim.models import word2vec
import requests,re,pymysql
import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib
from langconv import *

CONN = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='topic')
cur = CONN.cursor()

model = word2vec.Word2Vec.load('G:\\PoetryAnalysis\\project\\backend\\classifier\\Zi_vec.bin')
SVM = joblib.load("G:\\PoetryAnalysis\\project\\backend\\classifier\\SVM_Classifier.m")

def T2S(sentence):
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

def S2T(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence

class classify(generics.GenericAPIView):
    
    # 悲伤
    words = "悲 哀 伤 悽 凄 嗟 惋 恸 怨 哭 泪 诉 泣 涕 恨 叹 惜 念 憾 奈 悼 恻 惋 怆" 
    sad = words.split(' ')

    # 喜悦
    words = "喜 欢 贺 悦 好 欣 乐 忻 适 享 暖 赏 春 意 娱 幸 怡 愉 洽 嬉 戏 优 畅 恬 熙 惬"
    happy = words.split(' ')

    # 忧愁
    words = "愁 苦 闷 恹 懊 恼 酸 甚 损 怕 呻 役 厌 病 疾 惫 忧 患 怠 艰 恤 惧 艰 遑 殚 叹 萧"
    sorrow = words.split(' ')

    # 豪迈
    words = "豪 雄 杰 俊 髦 侠 英 才 概 霸 伟 慨 笑 醉 酒 慷"
    heroic = words.split(' ')

    # 愤怒
    words = "怒 霆 狞 吼 汹 愤 哮 怖 轰 澎 慑 懑 忿 痛 妒 惩 恨"
    angry = words.split(' ')

    topic_dic = {
        'history':  "咏史怀古",
        'war':      "战争边塞",
        'scene':    "山水景致",
        'farewell': "离别送别",
        'travel':   "行旅思乡",
        'love':     "爱情闺怨",
    }

    def cutp(self,poet):
        return [letter for letter in poet if letter not in ['，','。',' ','！','；','？']]

    def count(self,target,topic):
        simi = []
        wid = int(len(target)/4)
        if wid == 0:
            wid = 10
        for i in target:
            distance = []
            for t in topic:
                try:
                    distance.append(min(model.wv.similarity(i,t),0.99))
                except KeyError:
                    distance.append(0)
            dis = 0
            distancelist = sorted(distance)[-10:]
            for wt in range(10):
                dis += (wt/10+1)*distancelist[wt] # 按顺序分配权重
            simi.append(dis)
        similarity = (sum(sorted(simi)[:wid])+sum(sorted(simi)[-wid:]))/wid*10 # 最近和最远
        #similarity = sum(sorted(simi)[-wid:])/wid*10
        return round(similarity,2)

    def classify(self,poet):
        target = self.cutp(poet)
        re = {'悲伤':self.count(target,self.sad),
        '喜悦':self.count(target,self.happy),
        '忧愁':self.count(target,self.sorrow),
        '豪迈':self.count(target,self.heroic),
        '愤怒':self.count(target,self.angry),}
        return re

    def EmotionAnalysis(self,poet):
        d = self.classify(poet)
        return sorted(d.items(),key = lambda x:x[1],reverse=True)[0][0]

    def wv2dv(self,t):
        text=""
        for uchar in t:
            if (uchar >= '\u4e00' and uchar <= '\u9fa5'):
                text+=uchar
        lth = len(text)
        dv = np.zeros(100)
        for i in text:
            try:
                dv += model.wv[i]
            except:
                lth-=1
        l = max(1,lth)
        dv = dv/l
        return dv

    def poet_analysis(self,poet):
        feature = poet[:7]
        sql = "select topic,emotion from temp where content like '%"+feature+"%';"
        cur.execute(sql)
        re = cur.fetchall()
        if re:
            topic,emotion = re[0]
        else:
            topic = SVM.predict([self.wv2dv(poet),])[0]
            emotion = self.EmotionAnalysis(poet)
        return topic,emotion

    def rec(self,feature, topic, emotion):
        sql = "SELECT title,dynasty,author,content FROM TEMP WHERE topic='%s' AND emotion='%s' \
            AND content NOT LIKE '%%%s%%' ORDER BY rand() LIMIT 5;"%(topic,emotion,feature)
        #sql = "SELECT title,dynasty,author,content FROM TEMP WHERE topic='%s' AND emotion='%s' \
        #    ORDER BY rand() LIMIT 5;"%(topic,emotion)
        cur.execute(sql)
        text = cur.fetchall()
        result = []
        for p in text:
            pt = {
                'title':S2T(p[0]),
                'author':S2T(p[1])+'·'+S2T(p[2]),
                'content':S2T(p[3])
            }
            result.append(pt)
        return result

    def post(self, request, *args, **kwargs):
        poet = T2S(request.data['poet'])
        result = self.poet_analysis(poet)
        topic,emotion = result
        recommend = self.rec(poet[:5],topic,emotion)
        return Response({'analysis':[self.topic_dic[topic],emotion],'recommend':recommend})


class retrievelist(generics.GenericAPIView):
    
    emotion_dic = {
        'sad':      "悲伤",
        'happy':    "喜悦",
        'sorrow':   "忧愁",
        'heroic':   "豪迈",
        'angry':    "愤怒",
    }

    def get(self, request, *args, **kwargs):
        topic = request.GET['topic']
        emotion = self.emotion_dic[request.GET['emotion']]
        page = request.GET['page']
        f = (int(page)-1)*5+1
        sql = "SELECT title,dynasty,author,content FROM TEMP WHERE topic='%s' AND emotion='%s' LIMIT %d,%d;"%(topic,emotion,f,8)
        cur.execute(sql)
        text = cur.fetchall()
        result = []
        for p in text:
            pt = {
                'title':S2T(p[0]),
                'author':S2T(p[1])+'·'+S2T(p[2]),
                'content':S2T(p[3])
            }
            result.append(pt)
        
        return Response(result)


class test(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return Response('大漠孤烟直，长河落日圆。')


           
