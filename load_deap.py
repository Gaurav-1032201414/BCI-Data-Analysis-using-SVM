import pickle

chan = ['Fp1', 'AF3', 'F3', 'F7', 'FC5', 'FC1', 'C3', 'T7', 'CP5', 'CP1', 'P3', 'P7', 'PO3', 'O1', 'Oz', 'Pz', 'Fp2', 'AF4', 'Fz', 'F4', 'F8', 'FC6', 'FC2', 'Cz', 'C4', 'T8', 'CP6', 'CP2', 'P4', 'P8', 'PO4', 'O2']
nLabel, nTrial, nUser, nChannel, nTime = 4, 40, 32, 32, 8064
print("DEAP Dataset \n")
fout_labels_valence = open("labels_valence01.txt", 'w')
fout_labels_arousal = open("labels_arousal01.txt", 'w')
fout_labels_dominance = open("labels_dominance01.txt", 'w')
fout_labels_liking = open("labels_liking01.txt", 'w')
for i in range(nUser):      								# 4, 40, 32, 32, 8064
	if i < 10:
		name = '%0*d' % (2, i+1)
	else:
		name = i+1
	# fname = "C:/Users/untaw/Downloads/data_preprocessed_python/data_preprocessed_python/s01.dat"
	fname = "C:/Users/untaw/Downloads/data_preprocessed_python/data_preprocessed_python/s"+str(name)+".dat"

	with open(fname, 'rb') as f:
		x = pickle.load(f, encoding='latin1')
	print("File Location and Name is:")
	print(fname)

	for tr in range(nTrial):
		fout_data = open("C:/Users/untaw/Downloads/data_preprocessed_python/data_preprocessed_python/user1&2.csv", 'w')
		for ch in chan:
			fout_data.write(ch+",")
		fout_data.write("\n")
		for dat in range(nTime):
			for ch in range(nChannel):
				if ch < 32:
					if ch == 31:
						fout_data.write(str(x['data'][tr][ch][dat]))
					else:					
						fout_data.write(str(x['data'][tr][ch][dat])+",")
			fout_data.write("\n")
		fout_labels_valence.write(str(x['labels'][tr][0]) + "\n")
		fout_labels_arousal.write(str(x['labels'][tr][1]) + "\n")
		fout_labels_dominance.write(str(x['labels'][tr][2]) + "\n")
		fout_labels_liking.write(str(x['labels'][tr][3]) + "\n")
		fout_data.close()

		print("User " + str(i+1) + " Trail " + str(tr+1))
	print("\n")
fout_labels_valence.close()
fout_labels_arousal.close()
fout_labels_dominance.close()
fout_labels_liking.close()
print("Data Extracted Successfully")
