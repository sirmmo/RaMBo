from resources.models import *
from django.contrib.auth.models import User

def do_get_resources(user):
	r = Resource.objects.filter(owner__username = user)

	return [{'name':n.name, 'url':n.url()} for n in r]

def do_get_resource(user, resource_name):
	r = Resource.objects.get(owner__username = user, name = resource_name)

	ps = r.properties.all()
	
	pr = {}
	for p in ps:
		pr[p.name] = p.value
	pu = {
		'category':str(r.category),
		'owner':str(r.owner),
		'name':str(r.name),
		'icon':str(r.icon),
		'url':r.url(),
		'properties':pr,
	}
	return pu
def get_template():
	return {'name':'', 'icon':'','category':''}

def do_add_resource(user, data):
	r = Resource()
	r.owner = User.objects.get(username = user)
	r.name = data['name']
	r.icon = data['icon']
	r.category = ResourceCategory.objects.get(slug=data['category'])
	r.save()
	return r.id

def do_get_categories():
	return [{'name':x.name, 'slug':x.slug, 'count':x.resource_set.count()} for x in ResourceCategory.objects.all()]

def do_add_category(user, name, parent = None):
	c = ResourceCategory()
	c.name = name
	try:
		p = ResourceCategory.objects.get(slug=parent)
		c.parent = p
	except:
		pass
	c.save()
	return c.id





def do_remove_category(user, name):
	ResourceCategory.objects.filter(slug=name).delete()
	return "done"





def do_get_shared_resources(user):
	r_set = set()
	for uc in UserConnection.objects.filter(target__username = user):
		r_set.update(uc.shared_resources.all())
	return [{'name':n.name, 'url':n.url(), 'owner':n.owner.username} for n in r_set]
	
