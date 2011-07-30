from resources.models import *


def do_get_resources(user):
	r = Resource.objects.filter(owner__username = user)

	return [{'name':n.name, 'url':n.url()} for n in r]

def do_get_resource(user, resource_name):
	r = Resource.objects.get(owner__username = user, name = resource_name)

	ps = r.prorperties.all()
	
	pr = {}
	for p in ps:
		pr[p.name] = p.value
	pu = {
		'category':str(r.category),
		'owner':str(r.owner),
		'name':str(r.name),
		'icon':str(r.icon),

		'properties':pr,
	}
def do_add_resource(user, data):
	r = Resource()
	r.owner = user
	r.name = data['name']
	r.icon = data['icon']
	r.category = ResourceCategory.objects.get(slug=data['category'])
	r.save()
	return r.id

def do_get_categories(user):
	return [x for x in Resource.objects.filter(owner__username = user).values('category')]

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
	pass






