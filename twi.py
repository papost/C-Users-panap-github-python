import tweepy 
import json
import re
from collections import Counter
from tweepy import OAuthHandler

consumer_key = 'h2t48iEeudgzJwM2slgE0nlEd'
consumer_secret = 'WkVFKtYnzXtY8X2dvg62Bn17jtRL4BRXum0fkT15TRAgSgAMr4'
access_token = '3353314221-G13JX4dS9UupqCut639aXVmlyMMixKRjGIxsd9U'
access_secret = 'XNWHPZkF94Y6yf3PBe2cQXwiH6S4wNVDe0HW4zYAh6aT'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
while True:
	try:
		screename = (raw_input("����� �� ������ ��� ������ ��� ���������: "))
		#������ �� 10 ��������� tweets
		keim = " "
		for status in tweepy.Cursor(api.user_timeline, screen_name=screename).items(10):
			keim = keim+" "+ status._json['text']
		break
	except Exception:
		print ("\n")
		print("�� ������ ��� ������� ��� ����� ������.")
#������ ��������
keim = ''.join([i for i in keim if not i.isdigit()])
keim = ' '.join(re.sub("(#[A-Za-z0-9]+)|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",keim).split())
lista = keim.split (' ')
#�������� ����� ����� ����������� � ���� ����
counter = collections.Counter(lista)
popular = str((counter.most_common(1)))
#������ ���� �������� (����)
popular = re.sub('[^a-zA-Z]+', '', popular)

print ("� ������������� ���� ����� �: "+popular+".")

