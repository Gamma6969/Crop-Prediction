from ydata_profiling import ProfileReport
import pandas as pd

df = pd.read_csv("indiancrop_dataset.csv")
profile = ProfileReport(df, title="Crop Prediction Report")
profile.to_notebook_iframe()
profile.to_file("DataANA.html")

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pickle
# df=pd.read_csv("indiancrop_dataset.csv")
# df.drop(['STATE'],axis=1,inplace=True)
# from sklearn.preprocessing import LabelEncoder
# le=LabelEncoder()
# df['CROP']=le.fit_transform(df['CROP'])
# corr = df.corr().abs()
# plt.figure(figsize=(10, 8))
# sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 12})
# plt.title('Absolute Correlation Heatmap')
# plt.show()
# x=df.iloc[:,0:8]
# y=df.iloc[:,8]
# x.head()
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# x = sc.fit_transform(x)
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# print("Training data",x_train.shape)
# print("Training data",x_test.shape)
# from sklearn.naive_bayes import GaussianNB
# model = GaussianNB()
# model.fit(x_train,y_train)
# y_prediction=model.predict(x_test)
# from sklearn.metrics import accuracy_score
# accuracy_score(y_test,y_prediction)
# plt.figure(figsize=(10, 8))
# from sklearn.metrics import confusion_matrix
# cm_Sig = confusion_matrix(y_test, y_prediction)
# sns.heatmap(cm_Sig, annot=True,fmt="d")
# filename='trained_model.pkl'
# pickle.dump(model,open(filename,'wb'))