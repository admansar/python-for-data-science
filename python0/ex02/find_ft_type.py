


def all_thing_is_obj(object: any) -> int:
	store = type (object);
	da_ty = (str(store).split ("'"))[1];
	da_ty = da_ty[0].upper() + da_ty[1:];
	if da_ty == "Str":
		print (f"{object} is in the kitchen : {store}");
	elif da_ty == "List" or da_ty == "Tuple" or da_ty == "Set" or da_ty == "Dict":
		print (f"{da_ty} : {store}");
	else:
		print ("Type not found");
	return 42;
