# Losowanie ze zbioru próbek z unikalnym id

tmp = data[data.id_customer == 1].take(np.random.permutation(len(data[data.id_customer == 1]))[:1])
for id in data['id_customer'].unique():
    tmp = tmp.append(data[data.id_customer == id].take(np.random.permutation(len(data[data.id_customer == id]))[:1]), ignore_index=True)
data = tmp.iloc[1:]