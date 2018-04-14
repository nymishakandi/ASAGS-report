from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
import numpy as np
import random
import time



X_train = np.empty((0,336))
Y_train = np.array([])
X_test = np.empty((0,336))
Y_test = np.array([])
count = 0
data = range(1,130)
random.shuffle(data)
trained_list = []
tested_list = []

start_time = time.time()

for i in data:
    try:
        file_name = 'violent_features_NON_VIOLENT/nonvio_' + str(i) + '.txt'
        file_obj = open(file_name, 'r')
        vif = np.loadtxt(file_obj)
        if vif.shape[0] == 630:  # avoiding hd videos
            continue
        vif = np.reshape(vif, (-1, vif.shape[0]))
        if count < 92:
            X_train = np.vstack((X_train,vif))
            Y_train = np.append(Y_train,0)
	    trained_list.append(i)
        else:
            X_test = np.vstack((X_test,vif))
            Y_test = np.append(Y_test,0)
	    tested_list.append(i)
        file_obj.close()
        count += 1
    except:
        continue
        print 'error in reading nonvio_%d.txt' % i

# reading violent video features
count = 0
for i in data:
    try:
        file_name = 'violent_features_VIOLENT/vio_' + str(i) + '.txt'
        file_obj = open(file_name, 'r')
        vif = np.loadtxt(file_obj)
        if vif.shape[0] == 630:  # avoiding hd videos
            continue
        vif = np.reshape(vif, (-1, vif.shape[0]))
        if count < 92:
            X_train = np.vstack((X_train, vif))
            Y_train = np.append(Y_train, 1)
	    trained_list.append(i)
        else:
            X_test = np.vstack((X_test, vif))
            Y_test = np.append(Y_test, 1)
	    tested_list.append(i)
        file_obj.close()
        count += 1
    except:
        continue
        print 'error in reading vio_%d.txt' % i




seed = 7
np.random.seed(seed)
model = Sequential()
model.add(Dense(350, activation="relu", kernel_initializer="uniform", input_dim=336))
model.add(Dense(336, activation='relu', kernel_initializer="uniform"))
model.add(Dense(1, activation="sigmoid", kernel_initializer="uniform"))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=150, batch_size=2,  verbose=0)

predictions = model.predict(X_test)

pred = [round(x[0]) for x in predictions]

acc_count = 0
for k in range(0,len(pred)):
    if pred[k] == Y_test[k]:
        acc_count += 1

accuracy = float(acc_count)/len(pred)
print 'accuracy is : ' + str(accuracy)
print("--- %s seconds ---" % (time.time() - start_time))



cm = confusion_matrix(Y_test,pred)
print ""
print "confusion matrix"
print cm

#acc_cm = float(cm[0][0]+cm[1][1])/float(np.sum(cm))

#print acc_cm
print ""
print "trained videos list"
print trained_list
print ""
print "tested videos list"
print tested_list
