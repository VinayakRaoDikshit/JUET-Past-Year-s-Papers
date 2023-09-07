import os
repository_root = "D:\Vinayak\JUET-Past-Year-s-Papers\CSE"
count1=0
count2=0
for root, dirs, files in os.walk(repository_root):
        for folder in dirs:
                # print(count1,folder)
                count1+=1
        for file in files:
                # print(count2,file)
                count2+=1                
print(count1,count2)