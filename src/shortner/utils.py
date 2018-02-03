import random

def url_generator(instance,size=6):
	chars = '0123456789'
	for i in range(26):
		chars = chars + chr(ord('a')+i)
	cls = instance.__class__
	#print(instance)
	if cls.objects.filter(url=instance).exists():
		return cls.objects.get(url=instance).shortcode,0  # 0 indicates, already saved
	return ''.join(random.choice(chars) for _ in range(size)),1  