def findDecision(obj): #obj[0]: distance
	# {"feature": "distance", "instances": 300, "metric_value": 0.5482, "depth": 1}
	if obj[0]>11.642065556898602:
		return 'No'
	elif obj[0]<=11.642065556898602:
		return 'Yes'
	else: return 'Yes'
