def NULL_not_found(object: any) -> int:
	store = type (object);
	da_ty = (str(store).split ("'"))[1];
	if da_ty == "NoneType":
		print (f"Nothing : {object} {store}");
	elif da_ty == "float":
		print (f"Cheese : {object} {store}");
	elif da_ty == "int":
		print (f"Zero : {object} {store}");
	elif da_ty == "str" and len (object) == 0:
		print (f"Empty : {store}");
	elif da_ty == "bool":
		print (f"Fake : {object} {store}");
	else:
		print ("Type not Found");
		return 1;
	return 0;

