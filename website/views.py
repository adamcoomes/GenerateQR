from models import *
from django.contrib.auth.models import User, AnonymousUser
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.validators import email_re, URLValidator
import random, string

def home(request):
	if request.is_ajax():
		text = request.POST.get('q').strip()
		size = request.POST.get('size', 'l')
		link_id = request.POST.get('name', '')
		type = 's'
		contact = False
		
		if len(text) <= 200:
			if text.find("@") == 0:
				type = 't'
				text = "http://twitter.com/%s" % text[1:]
			elif text.find("@") > 0 and email_re.match(text):
				type = 'e'
			else:
				if text.find("http") < 0: text = "http://" + text
				validate = URLValidator()
				try:
					validate(text)
					type = 'w'
				except: None
		
		
		if (link_id):
			while QRCode.objects.filter(link_id=link_id):
				link_id = "%s%d" % (link_id, random.randint(10,1000))
		else:
			char_set = string.ascii_letters + string.digits
			link_id=''.join(random.sample(char_set,6))
			while QRCode.objects.filter(link_id=link_id):
				link_id=''.join(random.sample(char_set,6))
		
		qrcode = QRCode(user=None, text=text, link_id=link_id, type=type)
		qrcode.save()
		
		return render_to_response('qr_list.html', {'type': qrcode.get_type_display(), 'link_id': link_id},
		context_instance = RequestContext(request))
	
	else:
		return render_to_response('home.html', context_instance = RequestContext(request))

def view_qr(request, link_id):
	qr = get_object_or_404(QRCode, link_id=link_id)
	size = request.GET.get('size', 'l')	
	return render_to_response('view_qr.html', {'qr': qr, 'size': size}, context_instance = RequestContext(request))