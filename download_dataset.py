import zipfile
import os

if not os.path.exists('dataset'):
	os.mkdir('dataset')
os.system("kaggle competitions download -c elo-merchant-category-recommendation -p dataset")
for filename in os.listdir('dataset'):
	if filename[-3:] == 'zip':
		zip_ref = zipfile.ZipFile(os.path.join('dataset', filename), 'r')
		zip_ref.extractall('dataset')
		os.remove(os.path.join('dataset', filename))
