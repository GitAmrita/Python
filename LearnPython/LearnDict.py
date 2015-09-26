def DictWork():
	data_from_client = {2: False, 1: True, 3: False, 4: True}
	old_data = ["1", "2", "7"]
	merged_data = [i for i in old_data if data_from_client.get(int(i), True) == True]
	merged_data.extend([str(j) for j,k  in data_from_client.items() if k == True and str(j) not in old_data])
	print merged_data

def DiaSolnOne():
	merged_dict = {int(key): True for key in old_data}  
	# Reformat the `old_data` into a dict like `data_from_client`
	merged_dict.update(data_from_client)  
	# Use the `data_from_client` to override the old data in `merged_dict`
	result = [str(key) for key, value in merged_dict.iteritems() if value]  
	# Reformat the `merged_dict` into an array of string, just like we currently store

def DiaSolnTwo():
	new_set = set(int(x) for x in old_data) + set(data_from_client.iterkeys())  
	# Merge all the items from 2 list, avoid duplications using `set` data structure
	result = [str(x) for x in new_set if data_from_client.get(x, True)]  
	# Only keep the item that not in the client list or being `True`


def DictPop():
	dict ={1: True, 2: False, 3: False, 4: True}
	print (dict.pop(7,False))

DictPop()
#DictWork()