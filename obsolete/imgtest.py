gallery = {'images/Lodges/dining_area.jpg': 'caption 1', 'images/Lodges/living_area.jpg': 'caption 2', 'images/Lodges/porch.jpg': 'caption3'}


for image, caption in gallery.items():
	print ("<a href='{{url_for('static', filename='" + image + "'') }}'> \n """
	      "<img src='{{url_for('static', filename='" + image + "'') }}' caption='" + caption + "'/> \n """
	 	  "</a>")