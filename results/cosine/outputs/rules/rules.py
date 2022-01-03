def findDecision(obj): #obj[0]: distance
	# {"feature": "distance", "instances": 344, "metric_value": 0.6612, "depth": 1}
	if obj[0]>0.3371320978837079:
		return 'No'
	elif obj[0]<=0.3371320978837079:
		return 'Yes'
	else: return 'Yes'
